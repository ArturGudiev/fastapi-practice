from fastapi import APIRouter
from .t1.a import router1
from .t2.a import router as t2

combined_router = APIRouter()

combined_router.include_router(router1, tags=["T1 simple get request"])
combined_router.include_router(t2)



