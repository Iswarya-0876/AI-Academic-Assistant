import chromadb


client = chromadb.PersistentClient(
    path="../chroma_db"
)


collection = client.get_or_create_collection(
    "academic_docs"
)


def store_data(
    chunks,
    embeddings,
    ids
):

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids
    )