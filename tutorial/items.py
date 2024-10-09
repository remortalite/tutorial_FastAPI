from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"hello": "world"}

@app.get("/items")
async def get_items(skip: int | None = None, limit: int | None = None):
    return {"page": "items", "skip": skip, "limit": limit}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

