from pydantic import BaseModel
from typing import List

class MenuItem(BaseModel):
    id:int
    name:str
    description:str
    category:str
    price:int
    available:bool


class MenuResponse(BaseModel):
    status:str = "success"
    count:int
    items:List[MenuItem]