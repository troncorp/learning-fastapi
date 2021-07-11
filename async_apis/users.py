from fastapi import APIRouter,status
from .db import database,user_table
from .schemas import UserIn,User
from .hashing import get_password_hash

router = APIRouter(
    tags=['Users']
)

@router.post('/user/', status_code=status.HTTP_201_CREATED, response_model=User)
async def create_user(user: UserIn):
    hashed_password = get_password_hash(user.password)
    query = user_table.insert().values(username=user.username, password=hashed_password)
    last_record_id = await database.execute(query=query)
    return {**user.dict(), 'id': last_record_id}