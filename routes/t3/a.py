from enum import Enum
from fastapi import APIRouter

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

router = APIRouter()

@router.get("/t3/{model_name}")
async def get_model(model_name: ModelName):
    return {"message": f"you sent predefined value {model_name}" }
