from fastapi import APIRouter, status, Depends
from .schemas import NoteCreate, NoteResponse
from auth.service import get_current_user
from .service import get_notes_service, create_note_service
from typing import Annotated
from user.models import User

router = APIRouter()


@router.post("/", response_model=NoteResponse, status_code=status.HTTP_200_OK)
def create_note(
    note: NoteCreate, current_user: Annotated[User, Depends(get_current_user)]
):
    return create_note_service(note, current_user)


@router.get(
    "/",
    response_model=list[NoteResponse],
    status_code=status.HTTP_200_OK,
)
def get_notes_by_user_id(current_user: Annotated[User, Depends(get_current_user)]):
    return get_notes_service(current_user)
