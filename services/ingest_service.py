from services.pdf_parser import extract_text
from services.chunker import split_text
from services.vector_service import add_vectors



def ingest_pdf(path):


    text = extract_text(path)


    chunks = split_text(text)


    add_vectors(chunks)


    return {

        "chunks": len(chunks)

    }