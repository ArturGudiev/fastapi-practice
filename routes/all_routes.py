from fastapi import APIRouter
from .t1.a import router1
from .t2.a import router as t2
from .t3.a import router as t3

combined_router = APIRouter()

combined_router.include_router(router1, tags=["T1 simple get request"])
combined_router.include_router(t2)
combined_router.include_router(t3, tags=["T3 predefinted values"])
