from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

from app.services.chat_service import chat

app = FastAPI(
    title="SHL Assessment Recommendation API",
    version="1.0.0",
    description="AI-powered SHL Assessment Recommendation System"
)


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]


@app.get("/")
def home():
    return {
        "message": "SHL AI Recommendation API is running 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/chat")
def chat_api(request: ChatRequest):
    return chat(request.messages)