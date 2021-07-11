from fastapi import APIRouter, status, HTTPException, Depends
from typing import List

from fastapi.security import OAuth2PasswordRequestForm
from .db import database, user_table
from .hashing import verify_password

from datetime import timedelta
from . import token


router = APIRouter(
    tags=['Auth']
)


@router.post('/login/')
async def login(request: OAuth2PasswordRequestForm = Depends()):
    # query = user_table.select.where(user_table.c.username == request.username)
    query = user_table.select().where(user_table.c.username == request.username)
    myuser = await database.fetch_one(query=query)
    if not myuser:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='user not found')
    # Sample test for password decreption
    # pbkdf2_sha256.verify("toomanysecrets", hash)
    if not verify_password(request.password, str(myuser.password)):
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail='invalid password')
    access_token_expires = timedelta(minutes=token.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token.create_access_token(
        data={"sub": myuser.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
    # return myuser

'''
{
  "username": "me",
  "password": "me@me",
  "id": 3
}
'''
