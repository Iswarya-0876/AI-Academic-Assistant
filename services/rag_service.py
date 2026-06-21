from services.embedding_service import create_embeddings
from services.vectordb_service import collection
from services.llm_service import ask_llm



def query_rag(question):


    query_vector = create_embeddings(
        [question]
    )[0]


    results = collection.query(
        query_embeddings=[
            query_vector
        ],
        n_results=3
    )


    context = "\n".join(
        results["documents"][0]
    )


    prompt = f"""

You are an AI academic assistant.

Use this context:

{context}


Question:

{question}


Answer:

"""


    return ask_llm(prompt)