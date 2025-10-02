from fastapi import APIRouter
from .t1.a import router1
from .t2.a import router as t2
from .t3.a import router as t3
from .t4.a import router as t4
from .t5_request_body.a import router as t5
from .t6_parameters_and_string_validations.a import router as t6

combined_router = APIRouter()

combined_router.include_router(router1, tags=["T1 simple get request"])
combined_router.include_router(t2)
combined_router.include_router(t3, tags=["T3 predefinted values for path parameters"])
combined_router.include_router(t4, tags=["T4 query parameters"])
combined_router.include_router(t5, tags=["T5 router"])
combined_router.include_router(t6, tags=["T6 parameters and string validations"])