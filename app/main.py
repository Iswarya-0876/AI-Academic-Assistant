from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware


from app.routes import auth
from app.routes import upload
from app.routes import query



# Create FastAPI application

app = FastAPI(

    title="AI Academic Assistant API",

    description="RAG based AI Assistant with Authentication",

    version="1.0.0"

)



# CORS Configuration
# Allows frontend (HTML/JS) to communicate with backend

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],

)



# Authentication APIs

app.include_router(

    auth.router,

    prefix="/api/auth",

    tags=["Authentication"]

)



# PDF Upload APIs

app.include_router(

    upload.router,

    prefix="/api",

    tags=["Document Upload"]

)



# AI Query APIs

app.include_router(

    query.router,

    prefix="/api",

    tags=["AI Query"]

)




# Home route

@app.get("/")

def home():

    return {

        "message":
        "AI Academic Assistant Running",

        "status":
        "online"

    }



# Health check route

@app.get("/health")

def health():

    return {

        "database":
        "connected",

        "rag":
        "ready",

        "model":
        "llama3.1:8b"

    }