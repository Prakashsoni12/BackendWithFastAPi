from fastapi import FastAPI
from app.routers import process_url,process_pdf,chat

app = FastAPI()

app.include_router(process_url.router)
app.include_router(process_pdf.router)
app.include_router(chat.router)


@app.get("/")
def read_post():
    return {"message": "Welcome to the FastAPI backend service!"}

