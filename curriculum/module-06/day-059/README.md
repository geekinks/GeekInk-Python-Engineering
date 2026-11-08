# Day 059: Authentication Fundamentals

## Learning Objectives

- Understand why authentication is essential for APIs.
- Hash passwords securely using bcrypt (via passlib).
- Implement user registration and login endpoints.
- Create and verify JWT (JSON Web Tokens) for stateless authentication.
- Protect API endpoints so only authenticated users can access them.

## Introduction

The APIs you have built so far are open to anyone. Any person or program can create, read, update, and delete data without identifying themselves. In a real application, this is unacceptable. You need to know who is making each request and whether they are authorized to perform the action.

Authentication is the process of verifying identity: "Who are you?" Authorization is the process of checking permissions: "Are you allowed to do this?" Today you will focus on authentication -- building a system where users register with a username and password, log in to receive a token, and include that token with subsequent requests.

**Security is not optional.** Storing passwords as plain text is one of the most dangerous mistakes in software engineering. You will learn to hash passwords so that even if your database is compromised, the actual passwords remain protected.

## Concepts

### Password Hashing

Never store passwords in plain text. Use a one-way hashing algorithm:

- **bcrypt**: the standard for password hashing. It is deliberately slow, making brute-force attacks impractical.
- `passlib` provides a clean Python interface to bcrypt.

```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])
hashed = pwd_context.hash("my_password")
is_valid = pwd_context.verify("my_password", hashed)  # True
```

### JSON Web Tokens (JWT)

A JWT is a compact, self-contained token that carries user identity information. It has three parts separated by dots:

```
header.payload.signature
```

- **Header**: algorithm and token type.
- **Payload**: data (user ID, expiration time).
- **Signature**: ensures the token has not been tampered with.

Install: `pip install python-jose[cryptography] passlib[bcrypt]`

### Authentication Flow

1. User registers with username and password.
2. Server hashes the password and stores it.
3. User logs in with username and password.
4. Server verifies the password against the stored hash.
5. Server creates a JWT and returns it.
6. Client includes the JWT in the `Authorization: Bearer <token>` header.
7. Server verifies the token on each request.

## Practical Examples

```python
# Password hashing with passlib
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hash a password
password = "secure_password_123"
hashed = pwd_context.hash(password)
print(f"Original: {password}")
print(f"Hashed:   {hashed}")
print(f"Hash length: {len(hashed)}")

# Verify a password
print(f"\nCorrect password: {pwd_context.verify('secure_password_123', hashed)}")
print(f"Wrong password:   {pwd_context.verify('wrong_password', hashed)}")
```

```python
# Creating and verifying JWTs
from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your-secret-key-keep-this-safe"
ALGORITHM = "HS256"


def create_token(data: dict, expires_minutes: int = 30) -> str:
    payload = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes)
    payload.update({"exp": expire})
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        print("Token has expired.")
        return None
    except jwt.JWTError:
        print("Invalid token.")
        return None


# Create a token
token = create_token({"sub": "amina", "role": "student"})
print(f"Token: {token[:50]}...")

# Verify the token
decoded = verify_token(token)
print(f"Decoded: {decoded}")
```

```python
# Complete FastAPI auth example
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

app = FastAPI(title="Auth Demo API")

SECRET_KEY = "your-secret-key-change-in-production"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()

# In-memory user storage (use a database in production)
users_db = {}


class UserRegister(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


def create_access_token(username: str) -> str:
    expire = datetime.utcnow() + timedelta(hours=1)
    payload = {"sub": username, "exp": expire}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> str:
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None or username not in users_db:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


@app.post("/register", status_code=201)
def register(user: UserRegister):
    """Register a new user."""
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already taken")
    
    users_db[user.username] = {
        "username": user.username,
        "hashed_password": pwd_context.hash(user.password),
    }
    return {"message": f"User '{user.username}' registered successfully."}


@app.post("/login", response_model=TokenResponse)
def login(user: UserLogin):
    """Login and receive an access token."""
    db_user = users_db.get(user.username)
    if not db_user or not pwd_context.verify(user.password, db_user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    token = create_access_token(user.username)
    return {"access_token": token}


@app.get("/profile")
def get_profile(username: str = Depends(get_current_user)):
    """Get the current user's profile (requires authentication)."""
    return {
        "username": username,
        "message": f"Welcome, {username}! You are authenticated.",
    }


@app.get("/public")
def public_endpoint():
    """A public endpoint that anyone can access."""
    return {"message": "This is public. No authentication needed."}
```

## Guided Practice

Test the authentication flow by running the API and using curl or a test script.

```python
import requests

BASE = "http://127.0.0.1:8000"

# Step 1: Register
print("=== Register ===")
r = requests.post(f"{BASE}/register", json={"username": "amina", "password": "secure123"})
print(f"  {r.status_code}: {r.json()}")

# Step 2: Login
print("\n=== Login ===")
r = requests.post(f"{BASE}/login", json={"username": "amina", "password": "secure123"})
token_data = r.json()
token = token_data["access_token"]
print(f"  Token received: {token[:40]}...")

# Step 3: Access protected endpoint
print("\n=== Access Profile (with token) ===")
headers = {"Authorization": f"Bearer {token}"}
r = requests.get(f"{BASE}/profile", headers=headers)
print(f"  {r.status_code}: {r.json()}")

# Step 4: Try without token
print("\n=== Access Profile (no token) ===")
r = requests.get(f"{BASE}/profile")
print(f"  {r.status_code}: {r.json()}")

# Step 5: Try with wrong password
print("\n=== Login with wrong password ===")
r = requests.post(f"{BASE}/login", json={"username": "amina", "password": "wrong"})
print(f"  {r.status_code}: {r.json()}")
```

## Daily Challenge

**Add Authentication to the Products API**

Take the products API from Day 058 and add authentication:

1. Add user registration (`POST /register`) and login (`POST /login`) endpoints.
2. Protect write operations (POST, PUT, DELETE) so only authenticated users can perform them.
3. Keep read operations (GET) public -- anyone can browse products.
4. Include the username of who created or last updated a product.
5. Add a `GET /me` endpoint that returns the current user's profile.

Requirements:
- Hash all passwords with bcrypt via passlib.
- Use JWT tokens with a configurable expiration time.
- Use FastAPI's `Depends()` for dependency injection of the current user.
- Return proper 401 status codes for unauthorized access.
- Never expose password hashes in any response.
- Load the secret key from an environment variable (fall back to a default for development only).

Write a test script that demonstrates the full flow: register, login, create a product with auth, try to create without auth.

## Expected Output

```
=== Auth + Products API Test ===

Register user: 201 - User 'amina' registered.
Login: 200 - Token received.

Create product (with auth): 201 - Created 'Laptop Stand'
Create product (no auth): 403 - Not authenticated

List products (public): 200 - 1 product(s) found

Update product (with auth): 200 - Updated successfully
Delete product (with auth): 204 - Deleted

Profile: 200 - {"username": "amina", "products_created": 1}
```

## Assessment

1. Why must passwords be hashed before storing them? Why is bcrypt specifically recommended?
2. What information does a JWT contain, and how does the server verify that it has not been tampered with?
3. What is the difference between authentication and authorization?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-06/day-059/`

Include your API code, test script, and a `README.md`. Do not include any secret keys or real passwords.

## Additional Resources

- [FastAPI security tutorial](https://fastapi.tiangolo.com/tutorial/security/)
- [passlib documentation](https://passlib.readthedocs.io/)
- [JWT introduction](https://jwt.io/introduction/)
- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

## Reflection

- What would happen if your JWT secret key was leaked? How would you recover?
- How does token-based authentication differ from session-based authentication?
