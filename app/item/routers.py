from fastapi import APIRouter
from . import database
from . import schemas

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.post("/add")
async def create_item(item: schemas.ItemCreate):
    success = database.add_item(item)
    if success:
        return {f"message": "Item {item.name} added successfully"}
    else:
        return {f"message": "Failed to add item {item.name}"}
