from fastapi import APIRouter, HTTPException
from app.models.item import Item, ItemUpdate
from app.services.item_service import fetch_all_items, fetch_item_by_id, create_item, update_item, delete_item

router = APIRouter()

# Get all items
@router.get("/items", response_model=list[Item])
async def get_items():
    items = await fetch_all_items()
    return items

# Get a single item by ID
@router.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: str):
    item = await fetch_item_by_id(item_id)
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")

# Create a new item
@router.post("/items", response_model=Item)
async def create_new_item(item: Item):
    item_id = await create_item(item.dict())
    created_item = await fetch_item_by_id(item_id)
    return created_item

# Update an existing item
@router.put("/items/{item_id}", response_model=Item)
async def update_existing_item(item_id: str, item: ItemUpdate):
    existing_item = await fetch_item_by_id(item_id)
    if not existing_item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    updated_item = item.dict(exclude_unset=True)
    await update_item(item_id, updated_item)
    return await fetch_item_by_id(item_id)

# Delete an item
@router.delete("/items/{item_id}")
async def delete_existing_item(item_id: str):
    deleted_count = await delete_item(item_id)
    if deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}
