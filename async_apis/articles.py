from fastapi import APIRouter,status,HTTPException,Depends
from typing import List
from .db import database,articel_table
from .schemas import Article,ArticleIn, User
from .token import get_current_user

router = APIRouter(
    tags=['Articles']
)

@router.get('/articles/', response_model=List[Article])
async def get_articles(current_user: User = Depends(get_current_user)):
    query = articel_table.select()
    return await database.fetch_all(query)


@router.get('/article/{id}', response_model=Article)
async def get_articles(id: int,current_user: User = Depends(get_current_user)):
    query = articel_table.select().where(articel_table.c.id == id)
    myArticle = await database.fetch_one(query)
    if myArticle is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Article with id {id} not found!!!')
    return myArticle


@router.post('/article/', status_code=status.HTTP_201_CREATED, response_model=Article)
async def create_article(article: ArticleIn,current_user: User = Depends(get_current_user)):
    query = articel_table.insert().values(
        title=article.title, description=article.description)
    last_record_id = await database.execute(query=query)
    return {**article.dict(), 'id': last_record_id}


@router.put('/article/{id}', response_model=Article)
async def update_article(id: int, article: ArticleIn,current_user: User = Depends(get_current_user)):
    # if get_articles(id) is not None:
    query = articel_table.update().where(articel_table.c.id == id).values(
        title=article.title, description=article.description)
    await database.execute(query=query)
    return {**article.dict(),'id':id}
    # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                     detail=f'Article with id {id} not found!!!')


@router.delete('/articles/{id}', status_code= status.HTTP_204_NO_CONTENT)
async def delete_article(id,current_user: User = Depends(get_current_user)):
    query = articel_table.delete().where(articel_table.c.id == id)
    await database.execute(query=query)