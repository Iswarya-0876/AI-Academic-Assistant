from services.pdf_parser import extract_text
from services.chunker import chunk_text
from services.embedding_service import create_embeddings
from services.vectordb_service import store_data



def ingest_pdf(path):

    print("Reading PDF...")

    text = extract_text(path)


    print("Creating chunks...")

    chunks = chunk_text(text)


    print("Creating embeddings...")

    embeddings = create_embeddings(chunks)


    ids = [
        f"chunk_{i}"
        for i in range(len(chunks))
    ]


    store_data(
        chunks,
        embeddings,
        ids
    )


    print("Ingestion Complete")