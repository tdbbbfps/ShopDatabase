from pydantic import BaseModel, Field
from typing import Optional


class SaleProduct(BaseModel):
    item_id : int = Field(
        ...,
        description="The unique identifier of the product being sold."
    )
    quantity : int = Field(
        ...,
        ge=0,
        description="The quantity of the product being sold. Must be non-negative."
    )
    # Product's unit price(must greater than or equal to 1).
    unit_price : int = Field(
        ...,
        ge=1,
        description="The unit price of the product being sold. Must be at least 1."
    )

class Sale(BaseModel):
    sale_id : int = Field(
        ...,
        description="The unique identifier of the sale."
    )
    products : list[SaleProduct] = Field(
        ...,
        description="A list of products included in the sale."
    )
    