from pydantic import BaseModel, Field
from typing import Optional

# Base model for an item, used for reading/returning item data
class Item(BaseModel):
    id: int
    name: str
    price: int

# Schema for creating a new item.
class ItemCreate(BaseModel):
    name : str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="The name of the item."
    )
    price : int = Field(
        ...,
        ge=0,
        description="The price of the item. Must be non-negative."
    )

# Schema for updating an item (input)
# All fields are optional for partial updates
class ItemUpdate(BaseModel):
    id : int = Field(
        ...,
        description="The unique identifier of the item to be updated."
    )
    name : Optional[str] = Field(
        None,
        min_length=1,
        max_length=100,
        description="The new name of the item."
    )
    price : Optional[int] = Field(
        None,
        ge=0,
        description="The new price of the item. Must be non-negative."
    )

# Schema for removing an item (input)
class ItemRemove(BaseModel):
    id : int