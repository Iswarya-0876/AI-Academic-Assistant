from fastapi import APIRouter
from pydantic import BaseModel

from services.rag_service import rag_answer


router=APIRouter()



class Question(BaseModel):

    question:str

    user_id:str="default"



@router.post("/query")

def query(data:Question):


    answer = rag_answer(

        data.question,

        data.user_id

    )


    return {

        "answer":answer

    }