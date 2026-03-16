from fastapi import FastAPI
from backend.api import chat_api, prompt_api, logs_api, stats_api

app = FastAPI(
    title="AI Prompt Injection Guard"
)

@app.get("/")
def home():
    return {"message": "AI Prompt Injection Guard API Running"}

app.include_router(prompt_api.router)
app.include_router(chat_api.router)
app.include_router(logs_api.router)
app.include_router(stats_api.router)