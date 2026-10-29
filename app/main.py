from fastapi import FastAPI

app = FastAPI()

bread_menu = [
    {"id": 1, "name": "White Bread", "price": 60},
    {"id": 2, "name": "Brown Bread", "price": 75},
    {"id": 3, "name": "Wholemeal Bread", "price": 90},
]


@app.get("/bread")
def get_bread():
    return {"bread": bread_menu}