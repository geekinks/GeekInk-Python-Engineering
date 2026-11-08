# Day 058: REST API Development

## Learning Objectives

- Understand RESTful API design principles and conventions.
- Implement all CRUD endpoints (GET, POST, PUT, DELETE) for a resource.
- Use appropriate HTTP status codes for each operation.
- Validate request data using Pydantic models.
- Build a complete CRUD API for a products catalog.

## Introduction

Yesterday you built your first FastAPI application with a few endpoints. Today you will learn to design a complete RESTful API following industry conventions. REST (Representational State Transfer) is a set of architectural principles that guide how APIs should be structured.

A well-designed REST API is predictable: another developer can guess how your API works just by looking at the URL patterns and HTTP methods. Resources are identified by nouns in the URL, and actions are expressed through HTTP methods. This consistency makes APIs easier to learn, use, and maintain.

Today you will build a complete CRUD (Create, Read, Update, Delete) API for a products catalog, demonstrating all four operations with proper status codes and validation.

## Concepts

### RESTful URL Design

| Action | HTTP Method | URL | Status Code |
|--------|-------------|-----|-------------|
| List all | GET | `/products` | 200 |
| Get one | GET | `/products/{id}` | 200 / 404 |
| Create | POST | `/products` | 201 |
| Update (full) | PUT | `/products/{id}` | 200 / 404 |
| Update (partial) | PATCH | `/products/{id}` | 200 / 404 |
| Delete | DELETE | `/products/{id}` | 204 / 404 |

### HTTP Status Codes in REST

- **200 OK** -- successful read or update.
- **201 Created** -- successful creation of a new resource.
- **204 No Content** -- successful deletion (no body returned).
- **400 Bad Request** -- invalid input data.
- **404 Not Found** -- resource does not exist.
- **422 Unprocessable Entity** -- validation error (FastAPI default).

### Request and Response Models

Separate your models for different operations:
- **Create model**: fields required to create a resource (no id).
- **Update model**: fields that can be updated (all optional for PATCH).
- **Response model**: the complete resource including id and computed fields.

## Practical Examples

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

app = FastAPI(title="Products Catalog API")

# Database simulation
products_db: dict[int, dict] = {}
next_id = 1


# --- Pydantic Models ---

class ProductCreate(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    description: str = Field(default="", max_length=1000)
    price: float = Field(gt=0, description="Price must be positive")
    category: str = Field(min_length=1)
    stock: int = Field(default=0, ge=0)


class ProductUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    price: Optional[float] = Field(default=None, gt=0)
    category: Optional[str] = None
    stock: Optional[int] = Field(default=None, ge=0)


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    category: str
    stock: int
    created_at: str
    updated_at: str


# --- Helper ---

def get_product_or_404(product_id: int) -> dict:
    if product_id not in products_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id {product_id} not found."
        )
    return products_db[product_id]


# --- Endpoints ---

@app.get("/")
def root():
    """API information and available endpoints."""
    return {
        "title": "Products Catalog API",
        "endpoints": {
            "list": "GET /products",
            "create": "POST /products",
            "read": "GET /products/{id}",
            "update": "PUT /products/{id}",
            "delete": "DELETE /products/{id}",
        }
    }


@app.get("/products", response_model=list[ProductResponse])
def list_products(
    category: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    in_stock: Optional[bool] = None,
    skip: int = 0,
    limit: int = 20,
):
    """List all products with optional filters."""
    results = list(products_db.values())
    
    if category:
        results = [p for p in results if p["category"].lower() == category.lower()]
    if min_price is not None:
        results = [p for p in results if p["price"] >= min_price]
    if max_price is not None:
        results = [p for p in results if p["price"] <= max_price]
    if in_stock is not None:
        results = [p for p in results if (p["stock"] > 0) == in_stock]
    
    return results[skip : skip + limit]


@app.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int):
    """Get a single product by ID."""
    return get_product_or_404(product_id)


@app.post("/products", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate):
    """Create a new product."""
    global next_id
    
    now = datetime.now().isoformat()
    product_dict = product.model_dump()
    product_dict.update({
        "id": next_id,
        "created_at": now,
        "updated_at": now,
    })
    
    products_db[next_id] = product_dict
    next_id += 1
    
    return product_dict


@app.put("/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductUpdate):
    """Update an existing product (partial update)."""
    existing = get_product_or_404(product_id)
    
    update_data = product.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No fields to update."
        )
    
    existing.update(update_data)
    existing["updated_at"] = datetime.now().isoformat()
    
    return existing


@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int):
    """Delete a product by ID."""
    get_product_or_404(product_id)
    del products_db[product_id]
```

## Guided Practice

Test the API using Python's `requests` library (or curl). Create a file called `test_api.py`:

```python
import requests

BASE = "http://127.0.0.1:8000"

# Create products
print("=== Creating Products ===")
products_to_create = [
    {"name": "Python Textbook", "price": 29.99, "category": "Books", "stock": 50},
    {"name": "Mechanical Keyboard", "price": 89.99, "category": "Electronics", "stock": 20},
    {"name": "USB-C Cable", "price": 9.99, "category": "Electronics", "stock": 100},
    {"name": "Notebook", "price": 4.99, "category": "Stationery", "stock": 200},
]

for product in products_to_create:
    r = requests.post(f"{BASE}/products", json=product)
    data = r.json()
    print(f"  Created: [{data['id']}] {data['name']} - ${data['price']}")

# List all products
print("\n=== All Products ===")
r = requests.get(f"{BASE}/products")
for p in r.json():
    print(f"  [{p['id']}] {p['name']} (${p['price']}) - {p['stock']} in stock")

# Filter by category
print("\n=== Electronics ===")
r = requests.get(f"{BASE}/products", params={"category": "Electronics"})
for p in r.json():
    print(f"  [{p['id']}] {p['name']} - ${p['price']}")

# Update a product
print("\n=== Updating Product #1 ===")
r = requests.put(f"{BASE}/products/1", json={"price": 24.99, "stock": 45})
p = r.json()
print(f"  Updated: {p['name']} - now ${p['price']}, {p['stock']} in stock")

# Delete a product
print("\n=== Deleting Product #4 ===")
r = requests.delete(f"{BASE}/products/4")
print(f"  Status: {r.status_code}")

# Verify deletion
r = requests.get(f"{BASE}/products/4")
print(f"  Get deleted product: {r.status_code} - {r.json()['detail']}")
```

## Daily Challenge

**Build a Complete CRUD API for a Products Catalog**

Write a FastAPI application called `products_api.py` that provides a full CRUD API for managing products.

Requirements:

1. **Models**: Define `ProductCreate`, `ProductUpdate`, and `ProductResponse` Pydantic models.
2. **Endpoints**:
   - `GET /products` -- list all products with optional filters (category, price range, in-stock).
   - `GET /products/{id}` -- get a single product.
   - `POST /products` -- create a new product.
   - `PUT /products/{id}` -- update a product.
   - `DELETE /products/{id}` -- delete a product.
   - `GET /products/stats/summary` -- return total products, average price, products per category.
3. **Validation**: price must be positive, name must not be empty, stock must be non-negative.
4. **Status codes**: 201 for creation, 204 for deletion, 404 for not found.
5. **Error handling**: proper error messages for all failure cases.

Also write a `test_products.py` script that tests all endpoints using the `requests` library.

## Expected Output

Run the API, then run the test script:

```
=== Products API Test Suite ===

Testing CREATE...
  Created: Python Crash Course ($25.99) - Status: 201
  Created: USB Hub ($19.99) - Status: 201

Testing READ...
  All products: 2 found - Status: 200
  Single product: Python Crash Course - Status: 200
  Non-existent: Status: 404

Testing UPDATE...
  Updated price to $22.99 - Status: 200

Testing DELETE...
  Deleted product #2 - Status: 204

Testing FILTERS...
  Category 'Books': 1 found
  Price range $20-$30: 1 found

All tests passed.
```

## Assessment

1. Why should you use separate Pydantic models for create, update, and response?
2. What is the difference between PUT and PATCH in REST API design?
3. Why does a DELETE endpoint return 204 (No Content) instead of 200 (OK)?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-06/day-058/`

Include `products_api.py`, `test_products.py`, and a `README.md`.

## Additional Resources

- [FastAPI request body](https://fastapi.tiangolo.com/tutorial/body/)
- [HTTP status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [RESTful API design guide](https://restfulapi.net/)

## Reflection

- How does following REST conventions make your API easier for other developers to use?
- What would change if you replaced the in-memory storage with a real database?
