from fastapi import APIRouter, status
from .schemas import NoteCreate, NoteResponse
from .service import create_note_service, get_notes_service

router = APIRouter()


@router.post("/", response_model=NoteResponse, status_code=status.HTTP_200_OK)
def create_note(note: NoteCreate):
    return create_note_service(note)


@router.get(
    "/{user_id}",
    response_model=list[NoteResponse],
    status_code=status.HTTP_200_OK,
)
def get_notes_by_user_id(user_id: int):
    return get_notes_service(user_id)
