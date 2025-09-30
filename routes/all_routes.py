from fastapi import APIRouter
from .t1.a import router1

combined_router = APIRouter()

combined_router.include_router(router1)



