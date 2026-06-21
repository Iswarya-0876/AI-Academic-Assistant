from fastapi import APIRouter

from database.connection import SessionLocal

from database.models import User

from security.password import hash_password

from security.jwt import create_token



router = APIRouter()



@router.post("/register")

def register(
    username:str,
    email:str,
    password:str
):


    db=SessionLocal()


    user=User(

        username=username,

        email=email,

        password=
        hash_password(password)

    )


    db.add(user)

    db.commit()


    return {
        "message":
        "User created"
    }




@router.post("/login")

def login(
    email:str,
    password:str
):


    token=create_token(
        {
            "email":email
        }
    )


    return {

        "access_token":
        token

    }