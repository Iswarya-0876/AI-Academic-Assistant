from fastapi import APIRouter, UploadFile, File

import shutil


from services.ingest_service import ingest_pdf


router = APIRouter()



@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):

    file_path = (
        f"data/{file.filename}"
    )


    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )


    ingest_pdf(
        file_path
    )


    return {

        "status":"success",

        "filename":
        file.filename

    }