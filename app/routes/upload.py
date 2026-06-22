from fastapi import APIRouter, UploadFile, File


router = APIRouter()



@router.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...)
):

    return {

        "message":
        f"{file.filename} uploaded successfully"

    }