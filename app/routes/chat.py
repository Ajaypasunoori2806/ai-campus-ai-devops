from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
from app.services.ai_engine import get_ai_response
from app.services.ocr import extract_text
from app.services.memory import Memory

router = APIRouter()
memory = Memory()

# ✅ Request model (modern API)
class ChatRequest(BaseModel):
    user_id: str
    message: str

# ✅ Response model
class ChatResponse(BaseModel):
    response: str

@router.post("/chat", response_model=ChatResponse)
async def chat(data: ChatRequest):
    context = memory.get(data.user_id)
    response = get_ai_response(data.message, context)
    memory.update(data.user_id, data.message, response)
    return {"response": response}

@router.post("/image")
async def image_chat(user_id: str, file: UploadFile = File(...)):
    text = extract_text(file)
    return await chat(ChatRequest(user_id=user_id, message=text))