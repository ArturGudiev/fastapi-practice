from fastapi import APIRouter
router = APIRouter()

@router.get("/t2/{item_id}")
async def path_operation_function(item_id: int = 'Default Value'):
    return {"item_id": f'Here what I get item_id {item_id}'}
