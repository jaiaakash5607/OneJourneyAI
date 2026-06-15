from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from .routes import router
from . import models

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="OneJourney AI")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "Welcome to OneJourney AI 🚀"
    }