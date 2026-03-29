from fastapi import FastAPI
from app.routes.generate import router

app = FastAPI(
    title="RAG Question Generator",
    version="1.0"
)

app.include_router(router, prefix="/api")
