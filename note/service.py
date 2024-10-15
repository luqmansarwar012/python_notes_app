from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from .models import Note
from .schemas import NoteCreate
from user.models import User
from helpers.id_generator import id_generator


def create_note_service(note: NoteCreate, db: Session):
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


def get_notes_service(user_id: int, db: Session):
    notes = db.query(Note).filter(Note.user_id == user_id).all()
    if not notes:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No notes found"
        )
    return notes
