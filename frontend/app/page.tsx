import RoastMachine from "./components/RoastMachine"

export default function Home() {
  return (
    <main className="min-h-screen relative overflow-hidden">
      {/* Background fire particles */}
      <div className="fixed inset-0 pointer-events-none">
        {[...Array(6)].map((_, i) => (
          <div key={i} className="smoke" style={{ left: `${10 + i * 15}%`, animationDelay: `${i * 0.5}s`, bottom: "0" }} />
        ))}
      </div>

      <div className="relative z-10 max-w-4xl mx-auto px-4 py-8">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-5xl md:text-7xl font-black mb-2 fire-glow">
            🔥 MiMo Roast Machine 🔥
          </h1>
          <p className="text-lg text-orange-300/80 font-medium">
            Paste anything. Get destroyed. No survivors.
          </p>
        </div>

        <RoastMachine />

        {/* Footer */}
        <div className="text-center mt-8 text-sm text-orange-400/40">
          Powered by MiMo AI • Built with Next.js + FastAPI • No feelings were spared
        </div>
      </div>
    </main>
  )
}
