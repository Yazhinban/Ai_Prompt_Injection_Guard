from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class ChatRequest(BaseModel):
    prompt: str


@router.post("/chat")
def chat(request: ChatRequest):

    prompt = request.prompt

    response = f"LLM response to: {prompt}"

    return {"response": response}