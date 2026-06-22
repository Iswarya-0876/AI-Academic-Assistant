from fastapi import APIRouter
from pydantic import BaseModel

from database.connection import SessionLocal
from database.models import User

from security.password import *
from security.jwt import *


router=APIRouter()


class UserData(BaseModel):

    username:str
    email:str
    password:str



@router.post("/register")
def register(data:UserData):

    db=SessionLocal()


    user=User(

    username=data.username,

    email=data.email,

    password=hash_password(data.password)

    )


    db.add(user)

    db.commit()


    return {
        "message":"registered"
    }



@router.post("/login")
def login(data:UserData):

    db=SessionLocal()


    user=db.query(User).filter(
        User.email==data.email
    ).first()



    if not user:

        return {
            "error":"invalid"
        }



    token=create_token(
        {
        "email":user.email
        }
    )


    return {

    "token":token

    }