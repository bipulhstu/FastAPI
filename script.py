# Import date
from datetime import date 

# Import BaseModel
from pydantic import BaseModel

#Define Model Item
class Item(BaseModel):
    name: str 
    quantity: int = 0
    expiration: date = None 