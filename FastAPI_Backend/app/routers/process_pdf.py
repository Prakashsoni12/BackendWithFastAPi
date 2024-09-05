from fastapi import APIRouter,UploadFile,File,HTTPException
import uuid
import PyPDF2
from app.db.database import store_content


router = APIRouter()

@router.post("/process_pdf")
async def process_pdf(file: UploadFile = File(...)):
    try:
        pdf_reader = PyPDF2.PdfReader(file.file)
        content = ''

        for pages in pdf_reader.pages:
            content +=pages.extract_text()

        cleaned_content = ' '.join(content.split())

        chat_id = str(uuid.uuid4())

        store_content(chat_id, cleaned_content)

        return {
            "chat_id": chat_id,
            "message": "PDF content processed and stored successfully."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


