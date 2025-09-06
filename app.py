# app.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, HTMLResponse

app = FastAPI(title="Raja MagRex API")

# Allow your site to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://rajamagrex.com", "https://www.rajamagrex.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return JSONResponse({"message": "Raja MagRex API is live", "docs": "/docs"})

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/hello", response_class=HTMLResponse)
def hello():
    return """
    <!doctype html>
    <html><body style="font-family: system-ui">
      <h1>Raja MagRex API</h1>
      <p>API is live. See <a href="/docs">/docs</a>.</p>
    </body></html>
    """
