from fastapi import FastAPI
from pydantic import BaseModel

# Define model Item
class Item(BaseModel):
    name : str
    description : str

# Define items at application start
items = {"bananas": "Yellow fruit."}

app = FastAPI()


@app.put("/items")
def update_item(item: Item):
    name = item.name
    # Update the description
    items[name] = item.description
    return item


# to run server
# fastapi dev put.py

# to check using curl
"""
curl -X PUT \
  -H 'Content-Type: application/json' \
  -d '{"name": "bananas", "description": "Delicious!"}' \
  http://1270.0.1:8000/items
"""