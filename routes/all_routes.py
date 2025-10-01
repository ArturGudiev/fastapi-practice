from fastapi import APIRouter
from .t1.a import router1
from .t2.a import router as t2

combined_router = APIRouter()

combined_router.include_router(router1)
combined_router.include_router(t2)



