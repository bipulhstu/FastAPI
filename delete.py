from fastapi import FastAPI
from pydantic import BaseModel

# Define model Item
class Item(BaseModel):
    name: str

# Define items at application start
items = {"apples", "oranges", "bananas"}

app = FastAPI()


@app.delete("/items")
def delete_item(item: Item):
    name = item.name
    # Delete the item
    items.remove(name)
    return {}


# to run server
# fastapi dev delete.py

# to check using curl
"""
curl -X DELETE \
  -H 'Content-Type: application/json' \
  -d '{"name": "bananas"}' \
  http://localhost:8000/items
"""