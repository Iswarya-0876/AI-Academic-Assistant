from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from database.connection import engine

from sqlalchemy.orm import declarative_base


Base = declarative_base()



class User(Base):

    __tablename__="users"


    id = Column(
        Integer,
        primary_key=True
    )


    username = Column(
        String(50)
    )


    email = Column(
        String(100),
        unique=True
    )


    password = Column(
        String(200)
    )




class ChatHistory(Base):

    __tablename__="chat_history"


    id = Column(
        Integer,
        primary_key=True
    )


    user_id = Column(
        Integer
    )


    question = Column(
        Text
    )


    answer = Column(
        Text
    )



Base.metadata.create_all(
    bind=engine
)