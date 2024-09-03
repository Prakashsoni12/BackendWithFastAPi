from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import uuid



router = APIRouter()



class URLRequest(BaseModel):
    url: str

class URLResponse(BaseModel):
    chat_id:str
    message:str


@router.post("/process_url",response_model=URLResponse)
async def process_url(request: URLRequest):
    try:
        content = scrape_content(request.url)

        if not content:
            raise HTTPException(status_code=404,detail="Unable to scrape content from provided url")
        
        chat_id = str(uuid.uuid4())

        store_content(chat_id,content)
        return URLResponse(chat_id=chat_id,message="URL content processed and stored successfully.")
    except Exception as e:
        return HTTPException(status_code=500,detail=str(e))
    
