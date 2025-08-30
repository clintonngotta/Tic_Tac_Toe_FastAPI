from fastapi import FastAPI
from app.api.main import api_router

app = FastAPI(
    title="TiC TAC TOE",   
)


app.include_router(api_router)
