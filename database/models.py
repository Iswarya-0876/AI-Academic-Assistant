from sqlalchemy import Column, Integer, String, Text
from database.connection import Base



# ======================
# USER TABLE
# ======================

class User(Base):

    __tablename__ = "users"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    email = Column(
        String,
        unique=True,
        index=True
    )


    password = Column(
        String
    )



# ======================
# CHAT MEMORY TABLE
# ======================

class ChatHistory(Base):

    __tablename__ = "chat_history"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    user_id = Column(
        String
    )


    question = Column(
        Text
    )


    answer = Column(
        Text
    )