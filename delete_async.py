from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Define model Item
class Item(BaseModel):
    name: str

app = FastAPI()

items = {"rock", "paper", "scissors"}


@app.delete("/items")
# Make asynchronous
async def root(item: Item):
    name = item.name
    # Check if name is in items
    if name not in items:
        # Return the status code for not found
        raise HTTPException(status_code=404, detail="Item not found.")
    items.remove(name)
    return {"message": "Item deleted"}


# to run server
# fastapi dev delete_async.py

# to check using curl
"""
curl -X DELETE \
  -H 'Content-Type: application/json' \
  -d '{"name": "rock"}' \
  http://localhost:8000/items

curl -X DELETE \
  -H 'Content-Type: application/json' \
  -d '{"name": "roll"}' \
  http://localhost:8000/items

  
"""