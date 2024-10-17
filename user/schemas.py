from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    username: str

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    success: bool
    token: str
