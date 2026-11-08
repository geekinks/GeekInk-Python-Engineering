# Day 068: Connecting GUI to Database

## Learning Objectives

- Integrate SQLite with a Tkinter application for persistent data storage.
- Use the Treeview widget to display tabular data.
- Implement full CRUD (Create, Read, Update, Delete) operations through a GUI.
- Build a contact manager application with a database backend.

## Introduction

Most useful applications need to store data beyond a single session. Until now, our GUI applications lost all their data when the window closed. By connecting a GUI to a database, data persists between sessions and can be searched, filtered, and sorted.

SQLite is an ideal database for desktop applications — it is built into Python, stores everything in a single file, and requires no server setup. Combined with Tkinter, it lets you build standalone applications that manage real data.

The Treeview widget from Tkinter's `ttk` module is specifically designed for displaying rows and columns of data, making it the natural choice for showing database records in a table format.

## Concepts

### SQLite in a GUI Application

The typical pattern for database-backed GUI applications:

1. Connect to the database when the application starts.
2. Create tables if they do not exist.
3. Load data from the database into the display widgets.
4. When the user adds, edits, or deletes a record, update both the database and the display.
5. Close the connection when the application exits.

### Treeview Widget

`ttk.Treeview` displays data in rows and columns:

```python
from tkinter import ttk

tree = ttk.Treeview(root, columns=("name", "email", "phone"), show="headings")
tree.heading("name", text="Name")
tree.heading("email", text="Email")
tree.heading("phone", text="Phone")
tree.column("name", width=150)
tree.column("email", width=200)
tree.column("phone", width=120)
tree.pack(fill="both", expand=True)
```

Adding rows:

```python
tree.insert("", tk.END, values=("Ali Muhammad", "ali@example.com", "08012345678"))
```

Getting the selected row:

```python
selected = tree.selection()  # Returns a tuple of item IDs
if selected:
    values = tree.item(selected[0], "values")
```

Deleting a row:

```python
tree.delete(selected[0])
```

### Database Helper Pattern

Separate database operations from GUI code:

```python
import sqlite3

def get_connection():
    conn = sqlite3.connect("contacts.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT,
            phone TEXT
        )
    """)
    return conn
```

## Practical Examples

### Complete Contact Manager

```python
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.root.geometry("700x500")

        self.conn = sqlite3.connect("contacts.db")
        self._create_table()

        self._create_form()
        self._create_treeview()
        self._create_buttons()
        self._load_contacts()

    def _create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT,
                phone TEXT,
                city TEXT
            )
        """)
        self.conn.commit()

    def _create_form(self):
        form = tk.Frame(self.root)
        form.pack(fill="x", padx=10, pady=10)

        fields = [("Name:", 0), ("Email:", 1), ("Phone:", 2), ("City:", 3)]
        self.entries = {}

        for label_text, col in fields:
            tk.Label(form, text=label_text).grid(row=0, column=col * 2, padx=5, pady=5)
            entry = tk.Entry(form, width=15)
            entry.grid(row=0, column=col * 2 + 1, padx=5, pady=5)
            self.entries[label_text.rstrip(":")] = entry

    def _create_treeview(self):
        tree_frame = tk.Frame(self.root)
        tree_frame.pack(fill="both", expand=True, padx=10)

        scrollbar = tk.Scrollbar(tree_frame)
        scrollbar.pack(side="right", fill="y")

        self.tree = ttk.Treeview(tree_frame, columns=("id", "name", "email", "phone", "city"),
                                  show="headings", yscrollcommand=scrollbar.set)

        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="Name")
        self.tree.heading("email", text="Email")
        self.tree.heading("phone", text="Phone")
        self.tree.heading("city", text="City")

        self.tree.column("id", width=40)
        self.tree.column("name", width=150)
        self.tree.column("email", width=180)
        self.tree.column("phone", width=120)
        self.tree.column("city", width=100)

        self.tree.pack(fill="both", expand=True)
        scrollbar.config(command=self.tree.yview)

        self.tree.bind("<<TreeviewSelect>>", self._on_select)

    def _create_buttons(self):
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(fill="x", padx=10, pady=10)

        tk.Button(btn_frame, text="Add", width=10, command=self.add_contact).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Update", width=10, command=self.update_contact).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Delete", width=10, command=self.delete_contact).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Clear", width=10, command=self.clear_form).pack(side="left", padx=5)

    def _load_contacts(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        cursor = self.conn.execute("SELECT id, name, email, phone, city FROM contacts ORDER BY name")
        for record in cursor:
            self.tree.insert("", tk.END, values=record)

    def _on_select(self, event):
        selected = self.tree.selection()
        if not selected:
            return
        values = self.tree.item(selected[0], "values")
        self.clear_form()
        self.entries["Name"].insert(0, values[1])
        self.entries["Email"].insert(0, values[2])
        self.entries["Phone"].insert(0, values[3])
        self.entries["City"].insert(0, values[4])

    def clear_form(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def add_contact(self):
        name = self.entries["Name"].get().strip()
        if not name:
            messagebox.showwarning("Validation", "Name is required.")
            return
        email = self.entries["Email"].get().strip()
        phone = self.entries["Phone"].get().strip()
        city = self.entries["City"].get().strip()

        self.conn.execute("INSERT INTO contacts (name, email, phone, city) VALUES (?, ?, ?, ?)",
                          (name, email, phone, city))
        self.conn.commit()
        self.clear_form()
        self._load_contacts()

    def update_contact(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selection", "Select a contact to update.")
            return
        contact_id = self.tree.item(selected[0], "values")[0]
        name = self.entries["Name"].get().strip()
        if not name:
            messagebox.showwarning("Validation", "Name is required.")
            return
        email = self.entries["Email"].get().strip()
        phone = self.entries["Phone"].get().strip()
        city = self.entries["City"].get().strip()

        self.conn.execute("UPDATE contacts SET name=?, email=?, phone=?, city=? WHERE id=?",
                          (name, email, phone, city, contact_id))
        self.conn.commit()
        self.clear_form()
        self._load_contacts()

    def delete_contact(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selection", "Select a contact to delete.")
            return
        if not messagebox.askyesno("Confirm", "Delete this contact?"):
            return
        contact_id = self.tree.item(selected[0], "values")[0]
        self.conn.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
        self.conn.commit()
        self.clear_form()
        self._load_contacts()


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
```

## Guided Practice

Type out the Contact Manager example above yourself. Test each operation:

1. Add three contacts and verify they appear in the table.
2. Click a contact in the table and verify the form fills with their data.
3. Edit a field and click Update — verify the table changes.
4. Select a contact and delete it — verify the confirmation dialog and removal.
5. Close and reopen the application — verify your contacts are still there.

## Daily Challenge

Build a **Book Library Manager** with the following requirements:

1. Database table: `books` with columns: id, title, author, year, genre, status (Available/Borrowed).
2. A form at the top to enter book details with a Combobox for genre and status.
3. A Treeview showing all books with all columns visible.
4. Buttons: Add Book, Update Book, Delete Book, Clear Form.
5. A search entry above the table that filters books by title or author as you type.
6. Clicking a row in the table fills the form with that book's data.
7. Data must persist between sessions (SQLite).

Save the file as `library_manager.py`.

## Expected Output

A window with a form at the top, a searchable table in the middle, and action buttons at the bottom. Books are stored in SQLite and survive application restarts. Searching filters the displayed list in real time.

## Assessment

1. Why is it important to use parameterized queries (with `?` placeholders) instead of string formatting when building SQL statements?
2. How does `tree.selection()` help you know which row the user has selected?
3. What happens to the data if you delete the `.db` file? How would you handle this in a production application?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-07/day-068/`

Include your `library_manager.py` file.

## Additional Resources

- [SQLite3 Python Documentation](https://docs.python.org/3/library/sqlite3.html)
- [TkDocs: Treeview](https://tkdocs.com/tutorial/tree.html)

## Reflection

- How does connecting a GUI to a database change the usefulness of an application?
- What patterns from this lesson could you apply to any CRUD application, regardless of the data it manages?
