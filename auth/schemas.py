from pydantic import BaseModel


class Login(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    success: bool
    token: str


class TokenData(BaseModel):
    user_id: int | None = None


class Token(BaseModel):
    access_token: str
    token_type: str
