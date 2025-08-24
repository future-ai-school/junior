# api/main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import importlib

app = FastAPI()

# --- CORS 設定 ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://future-ai-school.github.io"],  # GitHub Pages の URL
    allow_methods=["POST"],                    # 許可する HTTP メソッド
    allow_headers=["*"],                       # 許可するヘッダ
)

# ルートアクセス対策
@app.get("/")
async def root():
    return {"message": "Wrong access!!"}

# キャラクター API
@app.post("/{character}")
async def handle_character(character: str, request: Request):
    data = await request.json()
    try:
        module = importlib.import_module(f"api.{character}")
        reply = module.handle(data["message"])
    except ModuleNotFoundError:
        reply = f"{character} は存在しません"
    return {"reply": reply}
