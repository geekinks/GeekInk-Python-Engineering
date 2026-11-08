# Day 070: Module 7 Project -- Desktop Inventory Management Application

## Learning Objectives

- Design and build a complete desktop application from requirements to working software.
- Apply all GUI concepts from this module: widgets, layout, events, menus, dialogs, database integration, and error handling.
- Practice engineering skills: code organization, separation of concerns, and user experience design.

## Introduction

This is the culminating project for Module 7. You will build a Desktop Inventory Management Application — a practical tool that a small business could use to track their products, stock levels, and sales.

This project brings together every concept from the past ten days: Tkinter widgets and layout, event handling, forms with validation, menus and dialogs, database integration with SQLite, and error handling and polish. The result should be a self-contained application that works reliably, handles user errors gracefully, and stores data persistently.

Approach this as a real engineering task. Plan before coding. Organize your code into logical sections. Test as you build. Polish before you submit.

## Project Requirements

### Core Features

1. **Product Management (CRUD)**
   - Add new products with: name, category, quantity, unit price, supplier.
   - View all products in a sortable Treeview table.
   - Edit existing product details.
   - Delete products with confirmation.

2. **Data Storage**
   - Use SQLite to store all product data.
   - Data must persist between application sessions.
   - Create the database and tables automatically on first run.

3. **Search and Filter**
   - A search bar that filters products by name or category.
   - A category filter dropdown to show products in a specific category.

4. **User Interface**
   - A menu bar with File (Export, Exit), Edit (Add, Delete), and Help (About) menus.
   - A status bar showing record count and operation feedback.
   - Keyboard shortcuts for common operations.

5. **Validation and Error Handling**
   - Product name is required.
   - Quantity must be a non-negative integer.
   - Price must be a positive number.
   - Inline validation feedback on the form.
   - All database operations wrapped in try/except.

### Stretch Goals (Optional)

- Export inventory to CSV.
- Low stock alerts (highlight products with quantity below a threshold).
- Total inventory value displayed in the status bar.

## Suggested Architecture

```
inventory_app.py          # Main application file
inventory_db.py           # Database helper functions
```

Or as a single file organized with classes:

```python
class InventoryDB:
    """Handles all database operations."""

class InventoryApp:
    """The main GUI application."""
```

## Starter Code

```python
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
import csv


class InventoryDB:
    def __init__(self, db_path="inventory.db"):
        self.conn = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT DEFAULT '',
                quantity INTEGER DEFAULT 0,
                price REAL DEFAULT 0.0,
                supplier TEXT DEFAULT ''
            )
        """)
        self.conn.commit()

    def add_product(self, name, category, quantity, price, supplier):
        self.conn.execute(
            "INSERT INTO products (name, category, quantity, price, supplier) VALUES (?, ?, ?, ?, ?)",
            (name, category, quantity, price, supplier)
        )
        self.conn.commit()

    def get_all_products(self):
        cursor = self.conn.execute(
            "SELECT id, name, category, quantity, price, supplier FROM products ORDER BY name"
        )
        return cursor.fetchall()

    def search_products(self, query):
        cursor = self.conn.execute(
            "SELECT id, name, category, quantity, price, supplier FROM products "
            "WHERE name LIKE ? OR category LIKE ? ORDER BY name",
            (f"%{query}%", f"%{query}%")
        )
        return cursor.fetchall()

    def update_product(self, product_id, name, category, quantity, price, supplier):
        self.conn.execute(
            "UPDATE products SET name=?, category=?, quantity=?, price=?, supplier=? WHERE id=?",
            (name, category, quantity, price, supplier, product_id)
        )
        self.conn.commit()

    def delete_product(self, product_id):
        self.conn.execute("DELETE FROM products WHERE id=?", (product_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()


class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("850x600")
        self.db = InventoryDB()

        self._create_menu()
        self._create_search_bar()
        self._create_form()
        self._create_treeview()
        self._create_buttons()
        self._create_status_bar()
        self._load_products()

        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    def _create_menu(self):
        # TODO: Create menu bar with File, Edit, Help menus
        pass

    def _create_search_bar(self):
        # TODO: Create search entry with live filtering
        pass

    def _create_form(self):
        # TODO: Create input form for product details
        pass

    def _create_treeview(self):
        # TODO: Create Treeview to display products
        pass

    def _create_buttons(self):
        # TODO: Create Add, Update, Delete, Clear buttons
        pass

    def _create_status_bar(self):
        # TODO: Create status bar at the bottom
        pass

    def _load_products(self, products=None):
        # TODO: Load products into Treeview
        pass

    def _on_close(self):
        self.db.close()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()
```

## Implementation Milestones

Work through these milestones in order:

1. **Database layer**: Complete the `InventoryDB` class (provided above). Test it in isolation by adding and retrieving products from a Python script.

2. **Basic GUI**: Create the window, form fields, and Treeview. Get the Add and display operations working first.

3. **Full CRUD**: Implement Update and Delete operations. Add row selection that fills the form.

4. **Search**: Add the search bar with live filtering using `trace_add` on a `StringVar`.

5. **Menus and shortcuts**: Add the menu bar and keyboard shortcuts.

6. **Validation and error handling**: Add field validation, disable buttons when appropriate, show status messages.

7. **Polish**: Add the status bar with record count, handle edge cases, test thoroughly.

## Testing Requirements

Test your application by performing these operations:

1. Add 5 products across at least 2 categories.
2. Search for a product by partial name.
3. Edit a product's price and quantity.
4. Delete a product (verify confirmation dialog).
5. Close and reopen the application (verify data persists).
6. Try submitting a form with missing required fields.
7. Try entering a negative price or non-numeric quantity.

## Evaluation Criteria

| Criteria | Weight | Description |
|----------|--------|-------------|
| Functionality | 30% | All CRUD operations work correctly |
| User Interface | 20% | Clean layout, logical organization |
| Error Handling | 20% | Validation, error messages, no crashes |
| Code Quality | 20% | Organized code, meaningful names, separation of concerns |
| Documentation | 10% | Comments where necessary, README for your submission |

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-07/day-070/`

Include:
- Your application file(s).
- A brief README describing your application and how to run it.

## Additional Resources

- [SQLite3 Documentation](https://docs.python.org/3/library/sqlite3.html)
- [TkDocs Complete Tutorial](https://tkdocs.com/tutorial/index.html)

## Reflection

- What was the most challenging aspect of building a complete application?
- If you were to rebuild this application, what would you do differently from the start?
- How does this project compare in complexity to the console applications you built in earlier modules?
