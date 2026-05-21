# 🔥 MiMo Roast Machine

Paste anything. Get destroyed by AI. No survivors.

A fun AI-powered roast generator built with **Next.js 14** + **FastAPI** + **MiMo AI**. Paste code, bios, tweets, or anything — and watch MiMo absolutely roast it to ashes.

![MiMo Roast Machine](https://via.placeholder.com/800x400/1a1a2e/f97316?text=🔥+MiMo+Roast+Machine+🔥)

## ✨ Features

- **4 Roast Categories** — Code 💻 | Bio 👤 | Tweet 🐦 | Custom 🎯
- **Heat Level Slider** — From Mild 😊 to ABSOLUTELY BRUTAL ☠️
- **60+ Curated Mock Roasts** — Works without API key in demo mode
- **MiMo AI Integration** — Set API key for real AI-generated roasts
- **Random Samples** — One-click sample text + random category
- **Copy to Clipboard** — Share your roasts anywhere
- **Dark Fire Theme** — Orange/red gradients, smoke particles, glow effects

## 🚀 Quick Start

### Backend

```bash
cd backend
cp .env.example .env
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:3000` in your browser.

## 🔑 Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `MIMO_API_KEY` | `demo_key_for_testing` | API key for MiMo AI |
| `MIMO_BASE_URL` | `https://api.openai.com/v1` | MiMo API endpoint |
| `MIMO_MODEL` | `gpt-4o-mini` | Model name |

**Demo mode** (default): Uses mock roasts — no API key needed.  
**Live mode**: Set a real `MIMO_API_KEY` in `backend/.env` for AI-generated roasts.

## 🛠️ Tech Stack

- **Frontend:** Next.js 14, React 18, TypeScript, Tailwind CSS
- **Backend:** FastAPI, Python 3.11, httpx, Pydantic
- **AI:** MiMo v2.5 Pro (xiaomi/mimo-v2.5-pro)
- **Theme:** Custom fire palette — orange/red gradients with smoke animations

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/health` | Server health check |
| `POST` | `/api/roast` | Generate a roast |
| `GET` | `/api/roast/random` | Get a random sample |

### POST /api/roast

```json
{
  "text": "Your text to roast",
  "category": "code | bio | tweet | custom",
  "intensity": 3
}
```

Intensity levels: `1` Mild → `2` Medium → `3` Spicy → `4` Savage → `5` BRUTAL

## 📁 Project Structure

```
mimo-roast-machine/
├── backend/
│   ├── main.py              # FastAPI + MiMo API + mock roasts
│   ├── requirements.txt     # Python dependencies
│   ├── .env                 # Environment config
│   └── .env.example         # Template
├── frontend/
│   ├── app/
│   │   ├── components/
│   │   │   └── RoastMachine.tsx   # Main UI component
│   │   ├── globals.css            # Fire theme + animations
│   │   ├── layout.tsx             # Root layout
│   │   └── page.tsx               # Home page
│   ├── tailwind.config.ts         # Custom color palette
│   ├── next.config.js
│   └── package.json
├── proofs/                        # Demo screenshots
└── README.md
```

## 📝 License

MIT

---

**Built with 🔥 by [andretukangoprek](https://github.com/andretukangoprek)**
