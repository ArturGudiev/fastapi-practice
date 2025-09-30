from fastapi import APIRouter
from .routes import router
from .routes3 import router3

combined_router = APIRouter()

combined_router.include_router(router)
combined_router.include_router(router3)



