from fastapi import APIRouter

router = APIRouter()

@router.post("/chat")
def chat(data: dict):

    prompt = data["prompt"]

    # Placeholder LLM response
    response = f"LLM response to: {prompt}"

    return {"response": response}