from fastapi import APIRouter

from pydantic import BaseModel


from services.rag_service import query_rag



router = APIRouter()



class Question(BaseModel):

    question:str




@router.post("/query")

def ask_question(
    data:Question
):


    answer = query_rag(
        data.question
    )


    return {

        "question":
        data.question,


        "answer":
        answer

    }