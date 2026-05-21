"use client"

import { useState } from "react"
import axios from "axios"

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"

const TABS = [
  { id: "code", emoji: "💻", label: "Code", placeholder: "Paste your code here...\n\nExample:\ndef fibonacci(n):\n    if n <= 0: return []\n    if n == 1: return [0]\n    fib = [0, 1]\n    for i in range(2, n): fib.append(fib[-1] + fib[-2])\n    return fib" },
  { id: "bio", emoji: "👤", label: "Bio", placeholder: "Paste a bio/about me section...\n\nExample:\nPassionate full-stack developer & lifelong learner.\nCEO @ MySideHustle | Forbes 30 Under 30 (pending)\nBuilding the future, one line of code at a time 🚀" },
  { id: "tweet", emoji: "🐦", label: "Tweet", placeholder: "Paste a tweet...\n\nExample:\nHot take: water is wet. Let that sink in. 🚿\n#DeepThoughts #MindBlown" },
  { id: "custom", emoji: "🎯", label: "Custom", placeholder: "Paste ANYTHING you want roasted...\n\nYour resume, a message from your ex, a product review,\nyour grandma\'s Facebook post, a corporate email...\nNo limits. Let chaos reign." },
]

const INTENSITY_LABELS: Record<number, { label: string; emoji: string; color: string }> = {
  1: { label: "Mild", emoji: "😊", color: "text-yellow-400" },
  2: { label: "Medium", emoji: "😏", color: "text-orange-400" },
  3: { label: "Spicy", emoji: "🔥", color: "text-orange-500" },
  4: { label: "Savage", emoji: "💀", color: "text-red-500" },
  5: { label: "ABSOLUTELY BRUTAL", emoji: "☠️", color: "text-red-600" },
}

interface RoastResult {
  roast: string
  mode: string
  model: string
  intensity?: number
  category?: string
  disclaimer?: string
  usage?: { prompt_tokens: number; completion_tokens: number }
}

export default function RoastMachine() {
  const [activeTab, setActiveTab] = useState("code")
  const [inputText, setInputText] = useState("")
  const [intensity, setIntensity] = useState(3)
  const [isLoading, setIsLoading] = useState(false)
  const [result, setResult] = useState<RoastResult | null>(null)
  const [error, setError] = useState("")

  const currentTab = TABS.find((t) => t.id === activeTab)!

  const handleRoast = async () => {
    if (!inputText.trim()) { setError("Bro, paste something dulu dong 😤"); return }
    setIsLoading(true); setError(""); setResult(null)
    try {
      const { data } = await axios.post(`${API_URL}/api/roast`, {
        text: inputText, category: activeTab, intensity,
      })
      if (data.error) { setError(data.error); return }
      setResult(data)
    } catch (err: any) {
      setError(err.response?.data?.detail || "MiMo lagi istirahat 🔥💤 Coba lagi ntar ya!")
    } finally { setIsLoading(false) }
  }

  const handleRandom = async () => {
    try {
      const { data } = await axios.get(`${API_URL}/api/roast/random`)
      setInputText(data.text); setActiveTab(data.category); setIntensity(data.intensity)
    } catch { setError("Gagal load sample. Server jalan? 🤔") }
  }

  const handleCopy = () => { if (result?.roast) navigator.clipboard.writeText(result.roast) }
  const handleClear = () => { setInputText(""); setResult(null); setError("") }

  return (
    <div className="space-y-6">
      {/* Tabs */}
      <div className="flex flex-wrap gap-2 justify-center">
        {TABS.map((tab) => (
          <button
            key={tab.id}
            onClick={() => { setActiveTab(tab.id); setResult(null); setError("") }}
            className={`px-5 py-2.5 rounded-xl font-bold text-sm transition-all duration-300 ${
              activeTab === tab.id
                ? "bg-gradient-to-r from-orange-500 to-red-600 text-white shadow-lg shadow-orange-500/30 scale-105"
                : "bg-white/5 text-orange-300/70 hover:bg-white/10 hover:text-orange-300 border border-white/5"
            }`}
          >
            {tab.emoji} {tab.label}
          </button>
        ))}
      </div>

      {/* Input Area */}
      <div className="bg-black/40 backdrop-blur-xl rounded-2xl border border-orange-500/20 p-6 shadow-2xl">
        <textarea
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
          placeholder={currentTab.placeholder}
          rows={8}
          className="w-full bg-transparent text-orange-100 placeholder-orange-400/30 resize-none focus:outline-none text-sm leading-relaxed font-mono"
        />

        {/* Intensity Slider */}
        <div className="mt-4 flex flex-col sm:flex-row items-center gap-4">
          <div className="flex items-center gap-3 flex-1 w-full">
            <span className="text-orange-400/60 text-xs whitespace-nowrap">Heat Level</span>
            <input
              type="range" min={1} max={5} value={intensity}
              onChange={(e) => setIntensity(Number(e.target.value))}
              className="flex-1 h-2 rounded-full appearance-none cursor-pointer"
              style={{ background: `linear-gradient(to right, #fbbf24 0%, #f97316 40%, #ef4444 70%, #dc2626 100%)` }}
            />
            <span className={`text-sm font-bold ${INTENSITY_LABELS[intensity].color} min-w-[140px] text-right`}>
              {INTENSITY_LABELS[intensity].emoji} {INTENSITY_LABELS[intensity].label}
            </span>
          </div>
        </div>

        {/* Buttons */}
        <div className="mt-4 flex flex-wrap gap-3">
          <button
            onClick={handleRoast}
            disabled={isLoading || !inputText.trim()}
            className="flex-1 min-w-[140px] py-3 bg-gradient-to-r from-orange-500 via-red-500 to-red-600 text-white font-black rounded-xl hover:from-orange-600 hover:via-red-600 hover:to-red-700 transition-all disabled:opacity-40 disabled:cursor-not-allowed shadow-lg shadow-red-500/20 hover:shadow-red-500/40 text-sm"
          >
            {isLoading ? (
              <span className="flex items-center justify-center gap-2">
                <svg className="animate-spin h-5 w-5" viewBox="0 0 24 24"><circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" fill="none"/><path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"/></svg>
                Roasting...
              </span>
            ) : "🔥 ROAST IT 🔥"}
          </button>
          <button onClick={handleRandom} className="px-5 py-3 bg-white/5 text-orange-300/70 rounded-xl hover:bg-white/10 hover:text-orange-300 transition-all border border-white/10 text-sm">🎲 Random</button>
          <button onClick={handleClear} className="px-5 py-3 bg-white/5 text-orange-300/70 rounded-xl hover:bg-white/10 hover:text-orange-300 transition-all border border-white/10 text-sm">🗑️ Clear</button>
        </div>
      </div>

      {/* Error */}
      {error && (
        <div className="bg-red-500/10 border border-red-500/30 rounded-xl p-4 text-red-400 text-center animate-fade-in">
          ⚠️ {error}
        </div>
      )}

      {/* Result */}
      {result && (
        <div className="bg-black/40 backdrop-blur-xl rounded-2xl border border-orange-500/30 p-6 shadow-2xl animate-fade-in">
          {/* Badge */}
          <div className="flex items-center justify-between mb-4 flex-wrap gap-2">
            <div className="flex items-center gap-2">
              <span className="px-3 py-1 bg-orange-500/20 text-orange-400 rounded-full text-xs font-bold">
                {result.mode === "live" ? "🤖 AI Roast" : "🎭 Demo Roast"}
              </span>
              {result.mode === "live" && result.model && (
                <span className="px-3 py-1 bg-purple-500/20 text-purple-400 rounded-full text-xs font-mono">{result.model}</span>
              )}
            </div>
            <div className="flex items-center gap-2">
              <span className="text-orange-400/50 text-xs">
                Heat: {INTENSITY_LABELS[result.intensity || 3].emoji} {INTENSITY_LABELS[result.intensity || 3].label}
              </span>
              <button onClick={handleCopy} className="px-3 py-1 bg-white/5 text-orange-300/60 rounded-lg hover:bg-white/10 hover:text-orange-300 text-xs transition-all" title="Copy roast">📋 Copy</button>
            </div>
          </div>

          {/* Roast Text */}
          <div className="text-orange-100 leading-relaxed whitespace-pre-wrap text-[15px]">{result.roast}</div>

          {/* Disclaimer */}
          {result.disclaimer && (
            <div className="mt-4 pt-3 border-t border-orange-500/10 text-orange-400/40 text-xs">{result.disclaimer}</div>
          )}

          {/* Usage */}
          {result.usage && (
            <div className="mt-2 text-orange-400/30 text-xs">
              Tokens: {result.usage.prompt_tokens} in / {result.usage.completion_tokens} out
            </div>
          )}
        </div>
      )}

      {/* Disclaimer */}
      <div className="text-center text-xs text-orange-400/30 mt-4">
        ⚡ All roasts are AI-generated comedy. No feelings were harmed... maybe. ⚡
      </div>
    </div>
  )
}
