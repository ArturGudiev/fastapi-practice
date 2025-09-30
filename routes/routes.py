from fastapi import APIRouter

router = APIRouter()

@router.get("/root2")
async def root2():
    return {"message": "Hello World222"}