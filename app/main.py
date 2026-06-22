from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.routes import auth
from app.routes import upload
from app.routes import query


app = FastAPI(
    title="AI Academic Assistant API",
    version="1.0"
)


# Serve frontend files
app.mount(
    "/frontend",
    StaticFiles(directory="frontend"),
    name="frontend"
)



app.include_router(
    auth.router,
    prefix="/api/auth"
)


app.include_router(
    upload.router,
    prefix="/api"
)


app.include_router(
    query.router,
    prefix="/api"
)



@app.get("/")
def home():

    return FileResponse(
        "frontend/index.html"
    )