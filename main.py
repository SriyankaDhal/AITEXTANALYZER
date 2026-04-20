from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Load AI model
sentiment = pipeline("sentiment-analysis")

# Input schema
class TextInput(BaseModel):
    text: str

# Home page
@app.get("/", response_class=HTMLResponse)
def home():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

# API
@app.post("/analyze")
def analyze(data: TextInput):
    result = sentiment(data.text)
    return result[0]
