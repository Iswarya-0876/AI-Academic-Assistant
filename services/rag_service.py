from services.vector_service import search_vectors
from services.llm_service import ask_llm

from services.memory_service import (
    save_chat,
    get_history
)



def rag_answer(question, user_id="default"):


    # Get PDF chunks

    docs = search_vectors(question)



    if not docs:

        return "I could not find this information in your PDF."



    context = "\n\n".join(docs)



    # Get previous chats

    history = get_history(user_id)



    memory = ""


    for chat in reversed(history):

        memory += f"""

User:
{chat.question}

AI:
{chat.answer}

"""



    prompt = f"""

You are an AI Academic Assistant.

Use the document context to answer.

Previous conversation:

{memory}


Document:

{context}


Question:

{question}


Give a clear human explanation.

"""



    answer = ask_llm(prompt)



    save_chat(

        user_id,

        question,

        answer

    )



    return answer