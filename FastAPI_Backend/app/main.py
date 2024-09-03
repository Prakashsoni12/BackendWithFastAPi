from fastapi import FastAPI
from app.routers import process_url

app = FastAPI()

app.include_router(process_url.router)


@app.get("/")
def read_post():
    return {"message": "Welcome to the FastAPI backend service!"}

