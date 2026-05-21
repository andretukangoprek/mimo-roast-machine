import type { Metadata } from "next"
import "./globals.css"

export const metadata: Metadata = {
  title: "MiMo Roast Machine 🔥",
  description: "Get absolutely destroyed by AI. Paste anything and watch MiMo roast it to ashes.",
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="antialiased">{children}</body>
    </html>
  )
}
