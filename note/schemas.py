from pydantic import BaseModel


class NoteCreate(BaseModel):
    title: str
    description: str


class NoteResponse(BaseModel):
    id: int
    title: str
    description: str
    user_id: int

    class Config:
        orm_mode = True
