from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .schemas import NoteCreate, NoteResponse
from database.service import get_db
from .service import create_note_service, get_notes_service

router = APIRouter()


# Create note
@router.post("/create", response_model=NoteResponse, status_code=status.HTTP_200_OK)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    newNote = create_note_service(note, db)
    return newNote


# Get notes by user ID
@router.get(
    "/get/{user_id}", response_model=list[NoteResponse], status_code=status.HTTP_200_OK
)
def get_notes(user_id: int, db: Session = Depends(get_db)):
    notes = get_notes_service(user_id, db)
    return notes
