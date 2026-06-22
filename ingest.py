from services.ingest_service import ingest_pdf



pdf_path="data/MACHINE LEARNING.pdf"



result=ingest_pdf(
    pdf_path
)



print(result)