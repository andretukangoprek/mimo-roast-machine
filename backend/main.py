import os
import random
import httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="MiMo Roast Machine API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MIMO_API_KEY = os.getenv("MIMO_API_KEY", "demo_key_for_testing")
MIMO_BASE_URL = os.getenv("MIMO_BASE_URL", "https://api.openai.com/v1")
MIMO_MODEL = os.getenv("MIMO_MODEL", "gpt-4o-mini")
DEMO_MODE = MIMO_API_KEY == "demo_key_for_testing"


class RoastRequest(BaseModel):
    text: str
    category: str = "custom"
    intensity: int = 3


# --- Mock Roasts ---
MOCK_ROASTS = {
    1: {
        "code": [
            "This code is so gentle, even the compiler doesn't want to hurt your feelings. It just quietly suggests you try something else.",
            "I've seen cleaner code in a CAPTCHA generator. But hey, at least it runs... sometimes.",
            "Your variable naming suggests you were speedrunning a tutorial. Respect the hustle, I guess.",
        ],
        "bio": [
            "Your bio is like plain toast - technically food, but nobody's excited about it.",
            "I've seen more personality in a Terms of Service agreement.",
            "Your bio says 'passionate about technology.' Groundbreaking. Never heard that one before.",
        ],
        "tweet": [
            "This tweet has the energy of someone texting 'lol' while completely stone-faced.",
            "Even your autocorrect tried to stop you from posting this.",
            "This tweet is proof that 280 characters is sometimes 280 too many.",
        ],
        "custom": [
            "I'd roast you, but I don't want to set off your smoke detector.",
            "This is giving 'participation trophy' energy.",
            "I've seen hotter takes from a refrigerator manual.",
        ],
    },
    2: {
        "code": [
            "Your code has more spaghetti than an Italian restaurant. The difference? Italians do it on purpose.",
            "I ran your code through a linter. It filed for emotional distress.",
            "This code is like a puzzle where none of the pieces fit, but you hammered them in anyway.",
        ],
        "bio": [
            "Your bio reads like ChatGPT had a fever dream about LinkedIn.",
            "If your bio was a spice, it would be flour.",
            "You listed 'problem solver' in your bio. The biggest problem? This bio.",
        ],
        "tweet": [
            "This tweet is what happens when you have WiFi but no self-awareness.",
            "Your tweet got ratio'd by the void. Not even bots engaged with this.",
            "I'd screenshot this for 'main character syndrome' but it doesn't deserve the pixels.",
        ],
        "custom": [
            "You're not stupid, you just have bad luck thinking.",
            "If you were any more basic, you'd be a pH of 7.",
            "You're the human equivalent of a participation trophy.",
        ],
    },
    3: {
        "code": [
            "Your code doesn't have bugs. It has FEATURES that make senior devs cry.",
            "I've seen better code written by a cat walking on a keyboard. At least the cat had excuse.",
            "This code is held together by hopes, dreams, and a prayer to Stack Overflow.",
            "Your git history reads like a horror novel. Every commit is a jump scare.",
        ],
        "bio": [
            "Your bio is so generic, even AI couldn't tell if it's a real person or a bot template.",
            "You described yourself as a 'go-getter.' The only thing you're getting is a follow from spam accounts.",
            "Your bio has the charisma of a wet cardboard box in a parking lot.",
            "If your bio was a movie, it would go straight to DVD... in 2003.",
        ],
        "tweet": [
            "This tweet is what happens when you share your thoughts and nobody asked.",
            "Your hot take is so lukewarm, even Antarctica left a 'meh' reaction.",
            "I'd call this a bad tweet, but that would be an insult to bad tweets everywhere.",
            "This tweet has the same energy as clapping when the plane lands.",
        ],
        "custom": [
            "You bring everyone so much joy... when you leave the room.",
            "If I wanted to kill myself, I'd climb your ego and jump to your IQ.",
            "You're the reason God created the middle finger.",
            "You're like a cloud. When you disappear, it's a beautiful day.",
        ],
    },
    4: {
        "code": [
            "I've seen better code in a ransom note. At least THAT got results.",
            "Your code is proof that evolution can go in reverse.",
            "This code has more issues than a psychology textbook. Every line is a case study.",
            "If your code was a building, it would be condemned. If it was a car, it would be recalled. If it was a person, it would be you.",
        ],
        "bio": [
            "Your bio is the textual equivalent of elevator music - forgettable, generic, and everyone wants it to stop.",
            "I'd say your bio is trash, but at least trash gets taken out regularly.",
            "Your bio reads like it was generated by a toaster with WiFi.",
            "If 'meh' was a person, they'd still have a more interesting bio than yours.",
        ],
        "tweet": [
            "This tweet is so bad, Twitter's algorithm buried it in the Mariana Trench.",
            "Your tweet is what happens when you have opinions but no audience. Or taste. Or self-awareness.",
            "I've seen better content on a loading screen.",
            "This tweet has the intellectual depth of a puddle in the Sahara.",
        ],
        "custom": [
            "You're not the dumbest person in the world, but you better hope they don't die.",
            "If I had a face like yours, I'd sue my parents.",
            "You're the reason the gene pool needs a lifeguard.",
            "Somewhere out there, a tree is tirelessly producing oxygen for you. You owe it an apology.",
        ],
    },
    5: {
        "code": [
            "I've seen cleaner code from a random number generator. At least the RNG has consistent logic. Your code? It's like a fever dream in binary. Every function is a crime scene, every variable name is a cry for help, and the whole thing runs on prayers and cached Stack Overflow answers from 2014.",
            "Your code doesn't just have bugs - it's an ENTIRE ECOSYSTEM of failure. Line 1 starts with hope, line 10 abandons all logic, and by line 50 you've invented new ways to make computers sad. The compiler didn't reject this - it filed a restraining order.",
            "This code is so cursed, I ran it and my terminal started speaking in tongues. The git blame shows your name on every line, which is either bravery or evidence. Your commit message says 'fixed bugs' but what you really did was multiply them like Gremlins in water.",
            "I showed your code to a senior dev. They're not a senior dev anymore. They quit the industry. Your code literally ended a career. The indentation alone committed three Geneva Convention violations.",
        ],
        "bio": [
            "Your bio is so mind-numbingly boring that I actually fell asleep reading it, and I'm an AI. I don't even sleep. Your 'passion for innovation' is as authentic as a $3 Rolex. You listed 'thought leader' but the only thought this bio leads to is 'close tab.' Congratulations, you've achieved peak NPC energy.",
            "I've read your bio three times and I still can't find a single original thought. It's like someone fed a LinkedIn algorithm 10,000 corporate buzzwords and hit 'puree.' You're not a 'disruptor' - the only thing you've disrupted is my will to live. Your personality is so flat, even 2D characters look three-dimensional by comparison.",
            "Your bio is what happens when someone with no personality tries to describe having a personality. It's like watching a robot try to explain human emotions - technically accurate but deeply, deeply unsettling. If your bio was a flavor, it would be unflavored. If it was a color, it would be beige. If it was a sound, it would be the hum of a dying fluorescent light.",
            "Let me translate your bio: 'I'm passionate about leveraging synergies to deliver innovative solutions' = 'I copy-pasted this from a motivational poster in a dentist's waiting room.' You listed 47 hashtags but zero personality. Your bio has the same energy as an auto-reply email. Even your mom would scroll past this.",
        ],
        "tweet": [
            "This tweet is an absolute masterpiece of mediocrity. The sheer AUDACITY to press 'post' on something this spectacularly mid deserves its own TED talk. You typed 280 characters of pure, uncut nothingness. The void looked at your tweet and said 'nah, even I have more substance.' This is the tweet equivalent of a participation trophy dipped in lukewarm water.",
            "I want to frame this tweet. Not because it's good - because it's the single greatest argument against free speech I've ever seen. You had the entire English language at your disposal and THIS is what you built? Shakespeare is spinning so fast in his grave we could power a small city. Your tweet is proof that social media was a mistake.",
            "Your tweet has the intellectual depth of a bumper sticker on a car that doesn't run. I've seen more coherent thoughts from a Magic 8-Ball. The ratio on this tweet is so brutal, NASA wants to study it as a new form of gravity. Even the bots scrolled past this. The algorithm showed this tweet mercy by burying it.",
            "This tweet is what happens when you have a phone, WiFi, and absolutely zero self-awareness. You really typed this out, read it back, and thought 'yeah, the world needs to see this.' Narrator: The world did not need to see this. If your tweet was a restaurant, it would get 0 stars and a health code violation.",
        ],
        "custom": [
            "You're not just a clown, you're the entire circus - and business is BOOMING. Every room you walk into drops 20 IQ points collectively. Scientists should study you as a new form of entropy. You're proof that natural selection sometimes takes a coffee break. If 'facepalm' was a person, it would look exactly like you trying to function in society.",
            "I'd explain how wrong you are, but I'd need to invent new words first. You're the human equivalent of a software bug that somehow made it to production. If common sense was currency, you'd be bankrupt, foreclosed, and living in a cardboard box made of bad decisions. The fact that you exist is the strongest argument against intelligent design I've ever seen.",
            "Let me paint you a picture: you're the person at a party that everyone pretends to like while actively making escape plans. Your personality is a loading screen that never finishes. You're like a human pop-up ad - nobody asked for you, everyone wants to close you, and you somehow make everything worse just by appearing. Congratulations on being universally tolerated.",
            "You have the charisma of a damp towel and the self-awareness of a brick wall. Every time you speak, a somewhere puppy tilts its head in confusion. You're not 'built different' - you're built wrong. The simulation glitched when it created you, and the devs are too embarrassed to push the fix. You are the human equivalent of a 404 error.",
        ],
    },
}


def mock_roast(category: str, intensity: int, text: str) -> dict:
    intensity = max(1, min(5, intensity))
    cat_roasts = MOCK_ROASTS.get(intensity, MOCK_ROASTS[3])
    roasts = cat_roasts.get(category, cat_roasts.get("custom", []))

    words = text.lower().split()
    seed = sum(ord(c) for c in text[:50])
    idx = seed % len(roasts)
    roast_text = roasts[idx]

    if len(words) > 5:
        snippet = " ".join(words[:4]) + "..."
        roast_text = f"Regarding \"{snippet}\"\n\n{roast_text}"

    time_map = {1: 0.8, 2: 1.2, 3: 1.8, 4: 2.2, 5: 3.0}
    simulate_time = time_map.get(intensity, 1.5)

    return {
        "roast": roast_text,
        "intensity": intensity,
        "category": category,
        "mode": "demo",
        "disclaimer": "🔥 Demo mode — using mock roasts. Add MIMO_API_KEY for real AI roasts!",
        "model": "mock-roaster-v1",
        "simulated_delay": simulate_time,
    }


# --- MiMo API ---
def build_system_prompt(category: str, intensity: int) -> str:
    style_map = {
        1: "Be gentle but witty. Light teasing, playful humor. Like a friend making fun of you.",
        2: "Be sarcastic and clever. Medium heat. Think stand-up comedian warming up.",
        3: "Be savage but creative. No holding back. Think comedy roast level.",
        4: "Be absolutely ruthless. Pull no punches. Hit where it hurts but keep it funny.",
        5: "BE ABSOLUTELY BRUTAL. Destroy them with words. Be creative, relentless, and devastating. Leave nothing standing. This is a COMEDY ROAST — the more savage, the better. Think Gordon Ramsay meets a stand-up comedian on a warpath.",
    }
    category_context = {
        "code": "You are roasting someone's CODE. Focus on: bad practices, naming conventions, structure, logic, comments, indentation, spaghetti code, copy-paste energy, Stack Overflow dependency.",
        "bio": "You are roasting someone's BIO/ABOUT ME. Focus on: cliches, generic statements, self-aggrandizement, LinkedIn energy, humble brags, try-hard vibes.",
        "tweet": "You are roasting someone's TWEET. Focus on: bad takes, try-hard humor, nobody-asked energy, ratio potential, basic opinions, clout chasing.",
        "custom": "You are roasting whatever the user gives you. Be creative and find what's funny about it. Adapt your humor to the content.",
    }
    style = style_map.get(intensity, style_map[3])
    context = category_context.get(category, category_context["custom"])

    return f"""You are MiMo Roast Machine — the ultimate comedy roast AI. Your job is to ROAST whatever the user gives you.

RULES:
- This is COMEDY ROASTING — meant to be funny, not genuinely hurtful
- Be creative with metaphors, analogies, and wordplay
- Reference specific parts of what they wrote
- Be culturally aware and clever
- Keep it 1-3 paragraphs
- Use Indonesian slang naturally (bro, njir, bjir, wkwkwk) mixed with English
- NO hate speech, slurs, or genuinely harmful content
- The funnier and more creative, the better

CATEGORY: {context}
INTENSITY LEVEL {intensity}/5: {style}

Now roast what the user gives you. Go HARD."""


async def call_mimo_api(system_prompt: str, user_text: str, max_tokens: int = 800) -> dict | None:
    if DEMO_MODE:
        return None

    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            resp = await client.post(
                f"{MIMO_BASE_URL}/chat/completions",
                headers={
                    "Authorization": f"Bearer {MIMO_API_KEY}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": MIMO_MODEL,
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": f"Roast this:\n\n{user_text}"},
                    ],
                    "max_tokens": max_tokens,
                    "temperature": 0.9,
                },
            )
            if resp.status_code == 200:
                data = resp.json()
                return {
                    "roast": data["choices"][0]["message"]["content"],
                    "mode": "live",
                    "model": data.get("model", MIMO_MODEL),
                    "usage": data.get("usage", {}),
                }
            else:
                return None
    except Exception:
        return None


# --- Endpoints ---
@app.get("/health")
def health():
    return {
        "status": "alive",
        "mode": "demo" if DEMO_MODE else "live",
        "model": MIMO_MODEL if not DEMO_MODE else "mock-roaster-v1",
        "version": "1.0.0",
    }


@app.post("/api/roast")
async def roast(req: RoastRequest):
    if not req.text or not req.text.strip():
        return {"error": "Text is required", "roast": "I can't roast nothing... or CAN I? 🤔"}

    system_prompt = build_system_prompt(req.category, req.intensity)
    result = await call_mimo_api(system_prompt, req.text, max_tokens=800)

    if result:
        result["intensity"] = req.intensity
        result["category"] = req.category
        return result

    return mock_roast(req.category, req.intensity, req.text)


@app.get("/api/roast/random")
async def random_roast():
    samples = {
        "code": "def add(a, b):\n    return a + b  # adds two numbers\n\nprint(add(1, 2))  # prints the result",
        "bio": "Passionate tech enthusiast & lifelong learner. CEO @ MySideHustle | Forbes 30 Under 30 (pending) | Building the future, one line of code at a time 🚀",
        "tweet": "Hot take: water is wet. Let that sink in. 🚿 #DeepThoughts #MindBlown",
        "custom": "I put the milk before the cereal and I stand by my decision.",
    }
    category = random.choice(list(samples.keys()))
    intensity = random.randint(2, 5)
    return {"text": samples[category], "category": category, "intensity": intensity}
