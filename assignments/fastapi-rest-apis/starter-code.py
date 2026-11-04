from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Items API")


class ItemCreate(BaseModel):
    name: str
    description: str
    price: float


class Item(ItemCreate):
    id: int


items: dict[int, Item] = {
    1: Item(id=1, name="Notebook", description="Caderno pautado", price=12.5),
    2: Item(id=2, name="Caneta", description="Caneta azul", price=3.0),
}
next_item_id = 3

# TODO: Add GET /items to return all items.
# TODO: Add GET /items/{item_id}; return HTTP 404 when the item is missing.
# TODO: Add POST /items using ItemCreate and return HTTP 201.
# TODO: Add PUT /items/{item_id} to replace an existing item.
# TODO: Add DELETE /items/{item_id} to remove an existing item.
