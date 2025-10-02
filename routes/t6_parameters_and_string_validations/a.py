from fastapi import APIRouter, Query
from typing import Annotated

router = APIRouter()

@router.get("/t6/min_max_string")
def t6_handler(q: Annotated[str | None, Query(min_length=3, max_length=10)]):
    return {"your validated q": q}



@router.get("/t6/regex")
def t6_handler_regex(q: Annotated[str, Query(regex=r"^ab[a-z]+z$")]):
    return {"your regex q": q}
