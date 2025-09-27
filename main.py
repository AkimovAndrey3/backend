from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextData(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Backend is running!"}

@app.post("/save")
def save_data(data: TextData):
    with open("data.txt", "a", encoding="utf-8") as f:
        f.write(data.text + "\n")
    return {"message": "Data saved successfully!"}