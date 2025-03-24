from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
    
class PostBase(BaseModel):
    title:str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

# Posts
class Post(PostBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True

# User Registration
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserCreateResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True

# Login

class UserLogin(BaseModel):
    email: EmailStr
    password: str

# JWT TOken
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id : int