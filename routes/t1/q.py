from fastapi import APIRouter

router1 = APIRouter()

@router1.get("/1")
async def t1():
    return {"message": "Hello World"}