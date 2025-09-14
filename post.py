from fastapi import FastAPI
from pydantic import BaseModel

#Define model item
class Item(BaseModel):
    name: str 

app = FastAPI()

@app.post("/")
def root(item: Item):
    name = item.name
    return {"message": f"We have {name}"}


# to run
# fastapi dev post.py

# to check
"""
curl -X POST "http://127.0.0.1:8000/" \
     -H "Content-Type: application/json" \
     -d '{"name": "Bipul Islam"}'

"""

