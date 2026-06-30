from fastapi import FastAPI

from app.api.chat import router as chat_router
from app.api.health import router as health_router
from app.api.index import router as index_router
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",      # local Next.js
        "https://your-frontend.vercel.app", 
        "https://personal-rag-web.vercel.app",# production frontend
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(chat_router)
app.include_router(index_router)
