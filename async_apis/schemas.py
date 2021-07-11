from typing import Optional
from pydantic import BaseModel


class ArticleIn(BaseModel):
    title: str
    description: str


class Article(ArticleIn):
    id: int


class UserIn(BaseModel):
    username: str
    password: str


class User(UserIn):
    id: int
    username: str


class LoginSchema(UserIn):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None