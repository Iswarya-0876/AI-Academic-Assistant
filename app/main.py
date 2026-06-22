from fastapi import FastAPI
from database.connection import create_tables

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from pathlib import Path

from app.routes import auth
from app.routes import query
from app.routes import upload



app = FastAPI(
    title="AI Academic Assistant"
)

create_tables()

app.include_router(
    auth.router,
    prefix="/api/auth"
)


app.include_router(
    query.router,
    prefix="/api"
)


app.include_router(
    upload.router,
    prefix="/api"
)



BASE_DIR = Path(__file__).resolve().parent.parent



app.mount(

    "/static",

    StaticFiles(
        directory=BASE_DIR / "frontend"
    ),

    name="static"

)



@app.get("/")

def home():

    return FileResponse(

        BASE_DIR / "frontend" / "chat.html"

    )