from fastapi import status, HTTPException
from .models import Note
from .schemas import NoteCreate
from user.models import User
from database.service import get_db


def create_note_service(note: NoteCreate, current_user: User):
    db = get_db()
    newNote = Note(
        title=note.title,
        description=note.description,
        user_id=current_user.id,
    )
    db.add(newNote)
    db.commit()
    db.refresh(newNote)
    db.close()
    return newNote


def get_notes_service(current_user: User):
    db = get_db()
    notes = db.query(Note).filter(Note.user_id == current_user.id).all()
    db.close()
    if not notes:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No notes found"
        )
    return notes
