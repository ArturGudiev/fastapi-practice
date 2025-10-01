from fastapi import APIRouter

router = APIRouter()

@router.get("/t4/")
async def t4_handler(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}