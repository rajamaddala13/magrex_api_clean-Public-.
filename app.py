from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Raja MagRex AI — API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://rajamagrexai.com",
        "https://www.rajamagrexai.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatIn(BaseModel):
    prompt: str
    mode: str = "core"

class ChatOut(BaseModel):
    ok: bool = True
    text: str
    mode: str

def reply_for_mode(mode: str, prompt: str) -> str:
    m = (mode or "core").lower().strip()
    if m == "core":
        return (f"🤖 MagRex Core — Balanced plan:\n"
                f"1) Clarify the goal.\n2) Find first unblocker.\n3) Take a 20-minute action.\n\nTopic: {prompt}")
    if m == "lite":
        return f"⚡ MagRex Lite — Quick tip for “{prompt}”: do the simplest next step in under 2 minutes."
    if m == "creativity":
        return (f"🎨 MagRex Creativity — For “{prompt}”:\n"
                f"- Combine two unlikely influences.\n- Draft one bold version.\n- Extract 1 realistic step.")
    if m == "logic":
        return (f"📐 MagRex Logic — For “{prompt}”:\n"
                f"1) Define inputs and assumptions.\n2) Work a tiny example.\n3) Check edge cases.")
    if m == "mentor":
        return (f"🧠 MagRex Mentor — Micro-goal for “{prompt}”:\n"
                f"- 20 min focus.\n- 5 min review.\n- Repeat ×3. You’ve got this.")
    if m == "explorer":
        return (f"🌍 MagRex Explorer — What-if for “{prompt}”:\n"
                f"- Change one assumption.\n- Compare Branch A vs B.\n- Choose by risk/payoff.")
    if m == "council":
        return ("👥 MagRex Council — Synthesis:\n"
                "- Core: direction\n- Logic: validation\n- Creativity: options\n- Mentor: micro-goal\n")
    return f"🤖 MagRex — Default response for: {prompt}"

@app.post("/chat", response_model=ChatOut)
def chat(payload: ChatIn):
    text = reply_for_mode(payload.mode, payload.prompt)
    return ChatOut(ok=True, text=text, mode=payload.mode)

@app.get("/health")
def health():
    return {"ok": True, "service": "MagRex API", "modes": ["core","lite","creativity","logic","mentor","explorer","council"]}
