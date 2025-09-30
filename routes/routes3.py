from fastapi import APIRouter

router3 = APIRouter()

@router3.get("/root3")
async def root2():
    return {"message": "Hello World333"}