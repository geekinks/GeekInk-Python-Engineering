# Day 055: Database Design and Relationships

## Learning Objectives

- Understand database normalization (1NF, 2NF, 3NF) and why it matters.
- Design one-to-many and many-to-many relationships between tables.
- Implement foreign key constraints to enforce referential integrity.
- Read and create simple Entity-Relationship (ER) diagrams.
- Design and implement a normalized database for a bookstore.

## Introduction

Good database design is like good architecture: it determines how easy your system is to build, maintain, and extend. A poorly designed database leads to duplicated data, inconsistencies, and queries that are slow or impossible to write. A well-designed database is clean, efficient, and adaptable.

Normalization is the process of organizing your tables to reduce redundancy and protect data integrity. It follows a set of progressive rules (normal forms) that guide you toward a clean structure. While academic normalization can go to the fifth or sixth normal form, in practice the first three normal forms (1NF, 2NF, 3NF) cover the vast majority of real-world needs.

Today you will also learn about the different types of relationships between tables and how to implement them using foreign keys and junction tables.

## Concepts

### Types of Relationships

**One-to-Many (1:N)**: one record in table A relates to many records in table B.
- A department has many students.
- A customer places many orders.
- Implemented with a foreign key in the "many" table.

**Many-to-Many (M:N)**: many records in table A relate to many records in table B.
- A student enrolls in many courses; a course has many students.
- A book has many authors; an author writes many books.
- Implemented with a junction (bridge) table.

**One-to-One (1:1)**: one record in table A relates to exactly one record in table B.
- A user has one profile.
- Less common; often these can be combined into a single table.

### Normalization

**First Normal Form (1NF)**:
- Each column contains only atomic (indivisible) values.
- No repeating groups or arrays in a single column.

Bad: `courses = "Math, English, Science"` in one column.
Good: separate rows in an enrollments table.

**Second Normal Form (2NF)**:
- Meets 1NF.
- Every non-key column depends on the entire primary key (relevant for composite keys).

**Third Normal Form (3NF)**:
- Meets 2NF.
- No non-key column depends on another non-key column (no transitive dependencies).

Bad: storing `department_name` in the students table alongside `department_id`.
Good: store only `department_id` and look up the name via JOIN.

### Foreign Keys

A foreign key creates a link between tables and enforces that referenced records exist:

```sql
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);
```

In SQLite, you must enable foreign key enforcement:

```python
conn.execute("PRAGMA foreign_keys = ON")
```

### Entity-Relationship Diagrams

ER diagrams visually represent tables, their columns, and relationships:

```
[departments]        [students]           [courses]
 id (PK)       <---  department_id (FK)
 name                id (PK)
                     name                  id (PK)
                     level                 title
                     gpa                   credits
                                           department_id (FK) ---> [departments]

                     [enrollments]
                      id (PK)
                      student_id (FK) ---> [students]
                      course_id (FK)  ---> [courses]
                      semester
                      grade
```

## Practical Examples

```python
import sqlite3
import os

db_path = "bookstore.db"
if os.path.exists(db_path):
    os.remove(db_path)

conn = sqlite3.connect(db_path)
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

# Normalized schema for a bookstore
cursor.executescript("""
    -- Authors table
    CREATE TABLE authors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        nationality TEXT
    );

    -- Books table
    CREATE TABLE books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        isbn TEXT UNIQUE NOT NULL,
        title TEXT NOT NULL,
        genre TEXT,
        publication_year INTEGER,
        price REAL NOT NULL,
        stock INTEGER DEFAULT 0
    );

    -- Junction table for many-to-many relationship
    CREATE TABLE book_authors (
        book_id INTEGER NOT NULL,
        author_id INTEGER NOT NULL,
        PRIMARY KEY (book_id, author_id),
        FOREIGN KEY (book_id) REFERENCES books(id),
        FOREIGN KEY (author_id) REFERENCES authors(id)
    );

    -- Customers table
    CREATE TABLE customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        joined_date TEXT DEFAULT (date('now'))
    );

    -- Orders table (one-to-many: customer -> orders)
    CREATE TABLE orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER NOT NULL,
        order_date TEXT DEFAULT (date('now')),
        total REAL DEFAULT 0.0,
        FOREIGN KEY (customer_id) REFERENCES customers(id)
    );

    -- Order items (one-to-many: order -> items, many-to-many: orders <-> books)
    CREATE TABLE order_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER NOT NULL,
        book_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL DEFAULT 1,
        price_each REAL NOT NULL,
        FOREIGN KEY (order_id) REFERENCES orders(id),
        FOREIGN KEY (book_id) REFERENCES books(id)
    );
""")

print("Bookstore database schema created.")
```

```python
# Populate with sample data
authors_data = [
    ("Chinua Achebe", "Nigerian"),
    ("Wole Soyinka", "Nigerian"),
    ("Chimamanda Ngozi Adichie", "Nigerian"),
    ("Ngugi wa Thiong'o", "Kenyan"),
]
cursor.executemany("INSERT INTO authors (name, nationality) VALUES (?, ?)", authors_data)

books_data = [
    ("978-0-385-47454-2", "Things Fall Apart", "Fiction", 1958, 12.99, 25),
    ("978-0-00-654762-3", "The Lion and the Jewel", "Drama", 1963, 9.99, 15),
    ("978-0-00-721870-5", "Half of a Yellow Sun", "Fiction", 2006, 14.99, 30),
    ("978-0-14-303943-3", "Americanah", "Fiction", 2013, 15.99, 20),
    ("978-0-435-90100-3", "A Grain of Wheat", "Fiction", 1967, 11.99, 10),
]
cursor.executemany(
    "INSERT INTO books (isbn, title, genre, publication_year, price, stock) VALUES (?, ?, ?, ?, ?, ?)",
    books_data
)

# Link books to authors (many-to-many)
book_author_links = [
    (1, 1),  # Things Fall Apart by Achebe
    (2, 2),  # Lion and the Jewel by Soyinka
    (3, 3),  # Half of a Yellow Sun by Adichie
    (4, 3),  # Americanah by Adichie
    (5, 4),  # A Grain of Wheat by Ngugi
]
cursor.executemany("INSERT INTO book_authors (book_id, author_id) VALUES (?, ?)", book_author_links)

customers_data = [
    ("Amina Ibrahim", "amina@example.com"),
    ("Usman Bello", "usman@example.com"),
]
cursor.executemany("INSERT INTO customers (name, email) VALUES (?, ?)", customers_data)

conn.commit()
print("Sample data inserted.")
```

```python
# Querying the many-to-many relationship
print("\nBooks with their authors:")
cursor.execute("""
    SELECT b.title, a.name as author, b.publication_year
    FROM books b
    INNER JOIN book_authors ba ON b.id = ba.book_id
    INNER JOIN authors a ON ba.author_id = a.id
    ORDER BY b.publication_year
""")
for row in cursor.fetchall():
    print(f"  {row[0]} by {row[1]} ({row[2]})")

# All books by a specific author
print("\nBooks by Chimamanda Ngozi Adichie:")
cursor.execute("""
    SELECT b.title, b.publication_year, b.price
    FROM books b
    INNER JOIN book_authors ba ON b.id = ba.book_id
    INNER JOIN authors a ON ba.author_id = a.id
    WHERE a.name = ?
""", ("Chimamanda Ngozi Adichie",))
for row in cursor.fetchall():
    print(f"  {row[0]} ({row[1]}) - ${row[2]}")

conn.close()
```

## Guided Practice

Simulate a purchase and verify referential integrity.

```python
import sqlite3

conn = sqlite3.connect("bookstore.db")
conn.execute("PRAGMA foreign_keys = ON")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


def place_order(customer_id, items):
    """
    Place an order.
    items: list of (book_id, quantity) tuples.
    """
    # Calculate total
    total = 0.0
    for book_id, quantity in items:
        row = cursor.execute("SELECT price, stock FROM books WHERE id = ?", (book_id,)).fetchone()
        if not row:
            print(f"  Book {book_id} not found.")
            return
        if row["stock"] < quantity:
            print(f"  Insufficient stock for book {book_id}.")
            return
        total += row["price"] * quantity
    
    # Create order
    cursor.execute(
        "INSERT INTO orders (customer_id, total) VALUES (?, ?)",
        (customer_id, total)
    )
    order_id = cursor.lastrowid
    
    # Add items and update stock
    for book_id, quantity in items:
        price = cursor.execute("SELECT price FROM books WHERE id = ?", (book_id,)).fetchone()["price"]
        cursor.execute(
            "INSERT INTO order_items (order_id, book_id, quantity, price_each) VALUES (?, ?, ?, ?)",
            (order_id, book_id, quantity, price)
        )
        cursor.execute(
            "UPDATE books SET stock = stock - ? WHERE id = ?",
            (quantity, book_id)
        )
    
    conn.commit()
    print(f"  Order #{order_id} placed. Total: ${total:.2f}")


# Test referential integrity -- try to order with invalid customer
print("Testing referential integrity:")
try:
    cursor.execute("INSERT INTO orders (customer_id, total) VALUES (999, 10.00)")
    conn.commit()
    print("  ERROR: Should have been rejected!")
except sqlite3.IntegrityError as e:
    print(f"  Correctly rejected: {e}")

# Place a valid order
print("\nPlacing a valid order:")
place_order(1, [(1, 1), (3, 2)])  # Amina buys 1 copy of book 1, 2 copies of book 3

# Check updated stock
print("\nStock after order:")
for row in cursor.execute("SELECT title, stock FROM books WHERE id IN (1, 3)").fetchall():
    print(f"  {row['title']}: {row['stock']} remaining")

conn.close()
```

## Daily Challenge

**Design and Implement a Normalized Bookstore Database**

Write a script called `bookstore_db.py` that:

1. Creates a normalized database with tables: `authors`, `books`, `book_authors`, `customers`, `orders`, `order_items`.
2. Populates it with at least 5 books, 4 authors (with some authors having multiple books), and 3 customers.
3. Implements and demonstrates these operations:
   - List all books with their authors (handling the many-to-many relationship).
   - Search books by genre.
   - Place an order (creating the order, order items, and updating stock).
   - View a customer's order history with details.
   - List the top-selling books.
   - Find authors who have written more than one book.
4. Enforces foreign key constraints and handles integrity errors.
5. Demonstrates what happens when you try to violate a constraint.

Requirements:
- Enable foreign keys with `PRAGMA foreign_keys = ON`.
- Use parameterized queries everywhere.
- Use proper normalization (no repeated data, proper junction tables).
- Print clear, formatted output for each operation.

## Expected Output

```
=== Bookstore Database ===

Books and Authors:
  Things Fall Apart by Chinua Achebe (1958) - $12.99, 25 in stock
  Half of a Yellow Sun by Chimamanda Ngozi Adichie (2006) - $14.99, 30 in stock
  Americanah by Chimamanda Ngozi Adichie (2013) - $15.99, 20 in stock
  ...

Authors with multiple books:
  Chimamanda Ngozi Adichie: 2 books

Placing order for Amina...
  Order #1 placed. Total: $42.97

Amina's Order History:
  Order #1 (2025-03-15) - $42.97
    - Things Fall Apart x1 @ $12.99
    - Half of a Yellow Sun x2 @ $14.99
```

## Assessment

1. Explain the three normal forms (1NF, 2NF, 3NF) in your own words.
2. Why do many-to-many relationships require a junction table?
3. What happens if foreign key enforcement is disabled in SQLite? Why is it important to enable it?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-06/day-055/`

Include `bookstore_db.py` and a `README.md`.

## Additional Resources

- [Database normalization basics](https://docs.microsoft.com/en-us/office/troubleshoot/access/database-normalization-description)
- [SQLite foreign keys](https://www.sqlite.org/foreignkeys.html)

## Reflection

- How does normalization prevent data inconsistencies?
- What are the trade-offs between a fully normalized database and one that denormalizes for performance?
