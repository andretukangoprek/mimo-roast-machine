import type { Config } from "tailwindcss"

const config: Config = {
  content: ["./app/**/*.{js,ts,jsx,tsx,mdx}", "./components/**/*.{js,ts,jsx,tsx,mdx}"],
  theme: {
    extend: {
      colors: {
        fire: { 50: "#fff7ed", 100: "#ffedd5", 200: "#fed7aa", 300: "#fdba74", 400: "#fb923c", 500: "#f97316", 600: "#ea580c", 700: "#c2410c", 800: "#9a3412", 900: "#7c2d12" },
        ember: { 50: "#fef2f2", 100: "#fee2e2", 200: "#fecaca", 300: "#fca5a5", 400: "#f87171", 500: "#ef4444", 600: "#dc2626", 700: "#b91c1c", 800: "#991b1b", 900: "#7f1d1d" },
      },
      animation: { "flame-pulse": "flamePulse 2s ease-in-out infinite", "shake": "shake 0.5s ease-in-out" },
      keyframes: {
        flamePulse: { "0%, 100%": { opacity: "1" }, "50%": { opacity: "0.7" } },
        shake: { "0%, 100%": { transform: "translateX(0)" }, "25%": { transform: "translateX(-5px)" }, "75%": { transform: "translateX(5px)" } },
      },
    },
  },
  plugins: [],
}
export default config
