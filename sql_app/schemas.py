from pydantic import BaseModel


class ArticleSchema(BaseModel):
    # id: int auto incremnetend
    title: str
    description: str

class MyArticleSchema(ArticleSchema):
    class Config:
        orm_mode = True