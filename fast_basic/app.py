from enum import Enum
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Category(Enum):
    TOOLS = "tools"
    CONSUMABLES = "consumables"


class Item(BaseModel):
    name: str
    price: float
    count: int
    id: int
    category: Category


items = {
    0: Item(name="Hammer", price=9.99, count=20, id=0, category=Category.TOOLS),
    1: Item(name="Pliers", price=5.99, count=20, id=1, category=Category.TOOLS),
    2: Item(name="Nails", price=1.99, count=100, id=2, category=Category.CONSUMABLES),
}


@app.get("/")
def index() -> dict[str, dict[int, Item]]:
    return {"items": items}


@app.get("/items/{id}")
def query_item_by_id(id: int) -> Item:
    if id not in items:
        raise HTTPException(status_code=404, detail=f"Item with {id} does not exist.")
    return items[id]


@app.get("/items")
def query_item_by_parameter(
    name: str | None = None, category: str | None = None
) -> dict[str, dict | list[Item]]:
    def check_item(item: Item):
        return all(
            (
                name is None or item.name == name,
                category is None or item.category is category,
            )
        )

    selection = [item for item in items.values() if check_item(item)]
    return {"query": {"name": name, "category": category}, "selection": selection}


@app.post("/items")
def create_item(item: Item) -> dict[str, str]:
    items[item.id] = item
    return {"status": "ok"}

