from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=72, pattern=r'^(?=.*[A-Za-z])(?=.*\d).+$')

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    is_active: bool
    is_admin: bool

class Token(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
