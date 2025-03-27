from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint
    
class PostBase(BaseModel):
    title:str
    content: str
    published: bool = True


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
class PostCreate(PostBase):
    pass


# Posts
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserCreateResponse
    class Config:
        orm_mode = True

class PostResponse(BaseModel):
    Post: Post
    votes: int
    class Config:
        orm_mode = True

# Votes

class Vote(BaseModel):
    post_id : int
    direction : conint(le=1)