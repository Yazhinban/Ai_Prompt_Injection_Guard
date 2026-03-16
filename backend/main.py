from fastapi import FastAPI
from backend.api.prompt_api import router as prompt_router
from backend.api.logs_api import router as logs_router
from backend.api.stats_api import router as stats_router
from backend.api.chat_api import router as chat_router
from backend.api.admin_api import router as admin_router
from backend.database.db import init_db

app = FastAPI()

init_db()

app.include_router(prompt_router)
app.include_router(logs_router)
app.include_router(stats_router)
app.include_router(chat_router)
app.include_router(admin_router)