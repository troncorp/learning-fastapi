from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# SQLALCHEMY_DATABASE_URL = "mysql://root:@127.0.0.1/fastapi"
SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://root:@127.0.0.1/fastapi"
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:4253@127.0.0.1/fastapi"



engine = create_engine(SQLALCHEMY_DATABASE_URL, future=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
