from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .models import Note
from .schemas import NoteCreate, NoteResponse
from user.models import User
from database import get_db
from helpers.id_generator import id_generator

router = APIRouter()


# Create note
@router.post("/create", response_model=NoteResponse, status_code=status.HTTP_200_OK)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == note.user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    newNote = Note(
        id=id_generator(),
        title=note.title,
        description=note.description,
        user_id=note.user_id,
    )
    db.add(newNote)
    db.commit()
    db.refresh(newNote)
    return newNote


# Get notes by user ID
@router.get(
    "/get/{user_id}", response_model=list[NoteResponse], status_code=status.HTTP_200_OK
)
def get_user_notes(user_id: int, db: Session = Depends(get_db)):
    notes = db.query(Note).filter(Note.user_id == user_id).all()
    if not notes:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No notes found"
        )
    return notes
