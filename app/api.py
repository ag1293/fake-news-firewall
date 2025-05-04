from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app.model import predict_credibility

app = FastAPI()

# Allow frontend (Streamlit) to talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class NewsInput(BaseModel):
    text: str

@app.post("/predict")
def predict_news(input_data: NewsInput):
    result = predict_credibility(input_data.text)
    return result
