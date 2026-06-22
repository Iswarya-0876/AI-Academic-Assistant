import chromadb
import os

from services.embedding_service import create_embedding


BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)


CHROMA_PATH = os.path.join(
    BASE_DIR,
    "chroma_db"
)


client = chromadb.PersistentClient(
    path=CHROMA_PATH
)


collection = client.get_or_create_collection(
    name="academic_docs"
)



def add_vectors(chunks):

    embeddings = []


    for chunk in chunks:

        embeddings.append(
            create_embedding(chunk)
        )


    ids = [
        str(i)
        for i in range(len(chunks))
    ]


    collection.add(

        documents=chunks,

        embeddings=embeddings,

        ids=ids

    )



def search_vectors(query):


    embedding = create_embedding(query)


    result = collection.query(

        query_embeddings=[
            embedding
        ],

        n_results=5

    )


    return result["documents"][0]