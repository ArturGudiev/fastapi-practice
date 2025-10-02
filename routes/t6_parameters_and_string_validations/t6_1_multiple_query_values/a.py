from typing import Annotated

from fastapi import APIRouter, Query
router = APIRouter()


@router.get("/t6_1/")
async def read_items(q: Annotated[list[str] | None, Query(title="Query string 111")] = None):
    query_items = {"q": q}
    return query_items