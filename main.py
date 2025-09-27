from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Настройка CORS для разрешения запросов с фронтенда
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В продакшене замените на конкретный домен фронтенда
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Модель для валидации входящих данных
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

@app.get("/read")
def read_data():
    try:
        with open("data.txt", "r", encoding="utf-8") as f:
            content = f.readlines()
        return {"data": [line.strip() for line in content]}
    except FileNotFoundError:
        return {"data": [], "message": "File data.txt not found"}