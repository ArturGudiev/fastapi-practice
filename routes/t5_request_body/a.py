from pydantic import BaseModel
from fastapi import APIRouter

class Item(BaseModel):
    id: int
    name: str
    description: str | None = None

router = APIRouter()

@router.post('/t5')
def send_item_body(item: Item):
    return {"your_item": item}