"# Menu_Restaurant" 
# Restaurant Menu API

A simple **FastAPI practice project** that provides restaurant menu data through REST API endpoints.

The project uses **Python, FastAPI, Pydantic**, and an in-memory menu list. It does not use a database.

## Features

* Get the complete restaurant menu
* Filter menu items by category
* Get a single menu item by ID
* Pydantic response validation
* 404 error handling
* CORS enabled
* Simple HTML frontend for displaying the menu
* Search dishes and filter by category in the frontend

## Tech Stack

* Python 3.11+
* FastAPI
* Pydantic
* Uvicorn
* HTML
* CSS
* JavaScript

## Project Structure

```text
fastapi-practice/
│
├── main.py              # FastAPI application and API routes
├── data.py              # In-memory restaurant menu data
├── interface.py         # Pydantic response models
├── index.html            # Frontend menu
├── index_old.html        # Older frontend version
├── copy_code.py          # Utility to collect project code
├── pyproject.toml        # Project configuration and dependencies
└── README.md             # Project documentation
```

## How It Works

The basic flow is:

```text
Client / Postman
       ↓
FastAPI Endpoint
       ↓
main.py
       ↓
MENU data from data.py
       ↓
Pydantic Response Model
       ↓
JSON Response
```

The menu data is stored in the `MENU` list inside `data.py`, so no database is required.

## API Endpoints

### 1. Get Complete Menu

```http
GET /menu
```

Returns all menu items.

Example:

```text
http://127.0.0.1:8000/menu
```

Response:

```json
{
  "status": "success",
  "count": 18,
  "items": []
}
```

### 2. Filter Menu by Category

```http
GET /menu?category=Pizza
```

Example:

```text
http://127.0.0.1:8000/menu?category=Pizza
```

The API filters the menu using the requested category.

Available categories:

* Pizza
* Pasta
* Salad
* Burger
* Dessert
* Beverage

If no items are found for the category, the API returns **404**.

### 3. Get Menu Item by ID

```http
GET /menu/{id}
```

Example:

```text
http://127.0.0.1:8000/menu/4
```

This returns the menu item whose ID matches the given ID.

If the ID does not exist, the API returns **404**.

## Response Models

The project uses Pydantic models to define the structure of API responses.

### MenuItem

```python
class MenuItem(BaseModel):
    id: int
    name: str
    description: str
    category: str
    price: int
    available: bool
```

### MenuResponse

```python
class MenuResponse(BaseModel):
    status: str = "success"
    count: int
    items: List[MenuItem]
```

These models make sure the returned data follows the expected structure and types.

## Error Handling

The API uses FastAPI's `HTTPException`.

For example, when a category has no matching items:

```json
{
  "detail": "NO menu items found for this category, Unknown"
}
```

The status code is:

```text
404 Not Found
```

The same approach is used when a menu item ID does not exist.

## Running the Project

### 1. Install dependencies

```bash
pip install "fastapi[standard]" "uvicorn[standard]"
```

### 2. Start the FastAPI server

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

### 3. FastAPI Documentation

Once the server is running, open:

```text
http://127.0.0.1:8000/docs
```

This opens FastAPI's interactive Swagger documentation where you can test the endpoints.

## Testing with Postman

You can test these requests:

```text
GET http://127.0.0.1:8000/menu
```

```text
GET http://127.0.0.1:8000/menu?category=Pizza
```

```text
GET http://127.0.0.1:8000/menu/4
```

For an invalid ID:

```text
GET http://127.0.0.1:8000/menu/999
```

Expected result:

```text
404 Not Found
```

## Frontend

`index.html` provides a simple restaurant menu interface.

It includes:

* Dish search
* Category buttons
* Menu cards
* Prices
* Availability status
* Responsive layout

The current frontend contains its own `MENU` JavaScript data and renders the menu in the browser.

## Data

The project currently contains **18 menu items** across six categories:

```text
Pizza
Pasta
Salad
Burger
Dessert
Beverage
```

Each item contains:

```text
id
name
description
category
price
available
```

## Project Configuration

The project requires Python **3.11 or newer** and lists FastAPI and Uvicorn as dependencies in `pyproject.toml`.

## Learning Concepts

This project demonstrates:

* FastAPI application creation
* GET endpoints
* Path parameters
* Query parameters
* Optional parameters
* Pydantic models
* Response models
* List comprehension
* `for` loops
* In-memory data
* HTTP 404 errors
* CORS middleware
* JSON responses
* API testing with Postman
* Basic frontend rendering

## Future Improvements

Possible next steps:

* Add a real database
* Add POST, PUT, and DELETE endpoints
* Add request models
* Add authentication
* Add database ORM
* Connect the frontend directly to the FastAPI API
* Add better validation and error handling
