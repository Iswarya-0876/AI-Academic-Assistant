from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from database.connection import SessionLocal
from database.models import User

from security.password import hash_password, verify_password
from security.jwt import create_token



router = APIRouter()



# =====================
# Request Models
# =====================

from pydantic import BaseModel, Field



class RegisterRequest(BaseModel):

    username: str

    email: str

    password: str = Field(
        min_length=6,
        max_length=72
    )





class LoginRequest(BaseModel):

    email: str

    password: str





# =====================
# Register
# =====================

@router.post("/register")
def register(user: RegisterRequest):


    db = SessionLocal()



    existing_user = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )



    if existing_user:

        db.close()

        raise HTTPException(

            status_code=400,

            detail="Email already exists"

        )



    new_user = User(

        username=user.username,

        email=user.email,

        password=hash_password(
            user.password
        )

    )



    db.add(new_user)

    db.commit()

    db.close()



    return {

        "message":
        "User registered successfully"

    }





# =====================
# Login
# =====================


@router.post("/login")
def login(user: LoginRequest):


    db = SessionLocal()



    db_user = (

        db.query(User)

        .filter(
            User.email == user.email
        )

        .first()

    )



    if not db_user:


        db.close()


        raise HTTPException(

            status_code=401,

            detail="Invalid email"

        )





    if not verify_password(

        user.password,

        db_user.password

    ):


        db.close()


        raise HTTPException(

            status_code=401,

            detail="Invalid password"

        )




    token = create_token(

        {

            "email":
            db_user.email

        }

    )



    db.close()



    return {


        "access_token":
        token,


        "token_type":
        "bearer"


    }