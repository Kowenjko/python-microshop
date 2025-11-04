from typing import Annotated, Union
from fastapi import APIRouter, Path

router = APIRouter(prefix="/items", tags=["Items"])


@router.get("/latest/")
def read_item_latests(name: str = "World"):
    name = name.strip().title()
    return {"helo": f"Hello {name}", "test": "This is a test"}


@router.get("/{item_id}/")
def read_item(
    item_id: Annotated[int, Path(ge=1, lt=1_000_000)], q: Union[str, None] = None
):
    return {"item_id": item_id, "q": q, "test": "This is a test"}
