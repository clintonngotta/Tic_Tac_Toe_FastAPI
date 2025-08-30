from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter(tags=["play"])

@router.post("/play")
async def play():    
    return JSONResponse(status_code=200, content={"message": "Play"})