from pydantic import BaseModel, Field
from typing import Optional
from item.models import Item

class sale(BaseModel):
    id : int
    items : list[Item]