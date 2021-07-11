from .database import Base
# from sqlalchemy import Column, Integer, String
from sqlalchemy import Table, Column, Integer, String,MetaData
metadata = MetaData()

class Articles(Base):
    __tablename__ = "articles"
    id = Column(type_=Integer, primary_key=True, index=True)
    title = Column(type_=String(length=100))
    description = Column(type_=String(length=1000))

#     user_table = Table(
#      "articles",
#      metadata,
#      Column('id', Integer, primary_key=True, index=True),
#      Column('title', String(30)),
#      Column('description', String)
# )
    