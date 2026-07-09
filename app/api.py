from fastapi import FastAPI
from pydantic import BaseModel
from app.models import Flashcard
from datetime import date


class FlashcardResponse(BaseModel):
    front: str
    back: str
    deck: str
    interval_days: int
    next_review_date: date

class FlashcardCreate(BaseModel):
    front: str
    back: str
    deck: str

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status" : "ok"}

@app.get("/")
def welcome_message():
    return {"message" : "nihongo-srs API"}

@app.post("/flashcards", response_model= FlashcardResponse)
def create_flashcard(card: FlashcardCreate):
    new_card = Flashcard(front=card.front, back=card.back, deck=card.deck)
    return new_card