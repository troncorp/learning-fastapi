from typing import List
from fastapi import FastAPI, Depends, status, HTTPException
from starlette.types import Message
from sql_app.database import engine, SessionLocal
from sql_app import models, schemas
from sqlalchemy.orm import Session, session

models.Base.metadata.create_all(bind=engine)

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.get('/')
def root():
    return {'hello': 'root'}


@app.get('/articles/', response_model=List[schemas.MyArticleSchema])
def get_articles(db: Session = Depends(get_db)):
    my_articles = db.query(models.Articles).all()
    return my_articles


@app.get('/articles/{id}')
def get_article(id: int, db: Session = Depends(get_db)):
    # article = db.query(models.Articles).filter(models.Articles.id == id).first()
    article = db.query(models.Articles).get(id)
    if article is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The articel with id {id} not found!")
    return article


@app.post('/article/', status_code=status.HTTP_201_CREATED)
def create_article(article: schemas.ArticleSchema, db: Session = Depends(get_db)):
    new_article = models.Articles(
        title=article.title, description=article.description)
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


@app.put('/article/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_article(article: schemas.ArticleSchema, id: int, db: Session = Depends(get_db)):
    try:
        db.query(models.Articles).filter(models.Articles.id == id).update(
            {models.Articles.title: article.title, models.Articles.description: article.description})
        db.commit()
        return {'message': 'Article updated Succesfully'}
    except:
        HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail='Error Occoured!!!')

@app.delete('/article/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_article(id:int, db:Session = Depends(get_db)):
    db.query(models.Articles).filter(models.Articles.id == id).delete()
    db.commit()
    return {'message':f'article with id {id} deleted Succefully'}
