from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from data import MENU
from interface import MenuItem, MenuResponse


app = FastAPI(title = "Restaurant Menu")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI(title = "Restaurant Menu")

@app.get("/menu", response_model = MenuResponse)
def get_menu(category: Optional[str] = Query(
    default = None,
    description = "Filter menu items by category e.g. Pizza, Pasta, Salad")
    ):

    if category is None:
        return MenuResponse(
            count = len(MENU),
            items = MENU
        )

    #comprehension
    filtered = [item for item in MENU if item["category"] == category]

    if not filtered:
        raise HTTPException(
            status_code = 404,
            detail = f"NO menu items found for this category, {category}"
        )
    return MenuResponse(
        count = len(filtered),
        items = filtered
    )
    

@app.get("/menu/{id}", response_model = MenuResponse)
def get_menu_item(id:int):
    for item in MENU:
        if item["id"] == id:
            return MenuResponse(
                count = len([item]),
                items = [item]
            )
        
    raise HTTPException(
        status_code = 404,
        detail = f"Menu item with id {id} not found"
    )