# api/main.py
from fastapi import FastAPI, Request
import importlib

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Wrong accesss!!"}

@app.post("/{character}")
async def handle_character(character: str, request: Request):
    data = await request.json()
    try:
        module = importlib.import_module(f"api.{character}")
        reply = module.handle(data["message"])
    except ModuleNotFoundError:
        reply = f"{character} は存在しません"
    return {"reply": reply}
