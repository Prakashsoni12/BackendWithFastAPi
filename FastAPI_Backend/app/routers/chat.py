from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
from app.db.database import retrive_content
from app.utils.embedding import get_relevant_response


router = APIRouter()

class ChatRequest(BaseModel):
    chat_id: str
    question: str

class ChatResponse(BaseModel):
    response: str

@router.post("/chat",response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        stored_content = retrive_content(request.chat_id)

        if not stored_content:
            raise HTTPException(status_code=404, detail="Content could not find from given chat id")
        
        response = get_relevant_response(stored_content['content'],request.question)

        return ChatResponse(response=response)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    