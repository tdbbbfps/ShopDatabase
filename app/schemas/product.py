from pydantic import BaseModel, Field
from typing import Optional

# Base model for an Product, used for reading/returning Product data
class Product(BaseModel):
    product_id: int
    name: str
    price: int

# Schema for creating a new Product.
class ProductCreate(BaseModel):
    name : str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="The name of the Product."
    )
    price : int = Field(
        ...,
        ge=0,
        description="The price of the Product. Must be non-negative."
    )

# Schema for updating an Product (input)
# All fields are optional for partial updates
class ProductUpdate(BaseModel):
    product_id : int = Field(
        ...,
        description="The unique identifier of the Product to be updated."
    )
    name : Optional[str] = Field(
        None,
        min_length=1,
        max_length=100,
        description="The new name of the Product."
    )
    price : Optional[int] = Field(
        None,
        ge=0,
        description="The new price of the Product. Must be non-negative."
    )

# Schema for removing an Product (input)
class ProductRemove(BaseModel):
    product_id : int