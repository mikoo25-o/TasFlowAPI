from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI()
class BreadCreate(BaseModel):
    name: str
    price: float = Field(gt=0)

bread_menu = [
    {"id": 1, "name": "White Bread", "price": 60},
    {"id": 2, "name": "Brown Bread", "price": 75},
    {"id": 3, "name": "Wholemeal Bread", "price": 90},
]


@app.get("/bread/{bread_id}")
def get_single_bread(bread_id: int):

    for bread in bread_menu:
        if bread["id"] == bread_id:
            return {"bread": bread}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Bread not found"
    )
@app.post("/bread")
def create_bread(bread: BreadCreate):
    new_bread = {
        "id": len(bread_menu) + 1,
        "name": bread.name,
        "price": bread.price
    }

    bread_menu.append(new_bread)

    return {
        "message": "Bread created successfully",
        "bread": new_bread
    }