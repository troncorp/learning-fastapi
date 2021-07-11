import databases
import sqlalchemy

# SQLAlchemy specific code, as with any other app
# DATABASE_URL = "sqlite:///./test.db"
DATABASE_URL = "mysql://root:@127.0.0.1/articleDB"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

articel_table = sqlalchemy.Table(
    "article",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String(100)),
    sqlalchemy.Column("description", sqlalchemy.String(500)),
)


user_table = sqlalchemy.Table(
    "user",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String(100)),
    sqlalchemy.Column("password", sqlalchemy.String(300)),
)


engine = sqlalchemy.create_engine(
    DATABASE_URL
)

metadata.create_all(engine)
