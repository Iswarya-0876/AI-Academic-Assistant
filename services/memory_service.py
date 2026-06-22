from database.connection import SessionLocal
from database.models import ChatHistory



def save_chat(
    user_id,
    question,
    answer
):

    db=SessionLocal()


    chat=ChatHistory(

        user_id=user_id,

        question=question,

        answer=answer

    )


    db.add(chat)

    db.commit()

    db.close()




def get_history(
    user_id
):

    db=SessionLocal()


    chats=db.query(
        ChatHistory
    ).filter(

        ChatHistory.user_id==user_id

    ).order_by(

        ChatHistory.id.desc()

    ).limit(5).all()



    db.close()



    return chats