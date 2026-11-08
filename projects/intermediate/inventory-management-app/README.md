# Desktop Inventory Management Application

**Module:** 7 — GUI and Application Development
**Day:** 70
**Difficulty:** Intermediate

---

## Problem Statement

Small businesses need simple, desktop-based tools to manage their inventory without relying on internet connectivity. This project builds a complete desktop application using Tkinter and SQLite that allows users to add, view, edit, delete, and search inventory items through a graphical interface.

## Objectives

- Build a multi-window desktop application with Tkinter.
- Implement event-driven programming with callbacks and bindings.
- Connect a GUI to a SQLite database for persistent storage.
- Display tabular data in a Treeview widget.
- Implement form validation and user-friendly error messages.
- Create menus, dialogs, and a polished user experience.

## Requirements

### Functional Requirements

1. **Item management:**
   - Each item has: name, category, quantity, unit price, supplier (optional), date added.
   - Categories: Electronics, Clothing, Food, Stationery, Furniture, Other.

2. **CRUD through the GUI:**
   - Add new items via a form.
   - View all items in a sortable table.
   - Edit an item by selecting it in the table.
   - Delete an item with confirmation dialog.

3. **Search and filter:**
   - Search items by name or category.
   - Filter by category using a dropdown.
   - Filter by low stock (quantity below a threshold).

4. **Reports:**
   - Total inventory value (sum of quantity * price for all items).
   - Item count per category.
   - Low stock alerts.

5. **Menu bar:**
   - File: Export to CSV, Exit.
   - Edit: Add Item, Delete Selected.
   - Help: About.

### Non-Functional Requirements

- The application must not crash on invalid input.
- The table must be scrollable for large inventories.
- The layout must be clean and organized.

## Technologies

- Python 3.10+
- Tkinter (standard library)
- SQLite3 (standard library)
- csv (standard library, for export)

## Suggested Architecture

```
inventory-management-app/
├── main.py           — Application entry point, main window
├── database.py       — Database operations (create, read, update, delete)
├── gui/
│   ├── main_window.py   — Main window layout with table and menu
│   ├── item_form.py     — Add/Edit item form dialog
│   └── reports.py       — Reports display
└── inventory.db      — SQLite database (created at runtime)
```

## Implementation Milestones

| Milestone | Description |
| :--- | :--- |
| 1. Database layer | Create SQLite database and CRUD functions |
| 2. Main window | Build the main window with Treeview table |
| 3. Add item form | Create the add item dialog with validation |
| 4. Edit and delete | Enable editing and deleting from the table |
| 5. Search and filter | Add search bar and category filter |
| 6. Menus and reports | Add menu bar, CSV export, summary reports |

## Testing Requirements

- Add items and verify they appear in the table.
- Edit an item and verify changes persist after restart.
- Delete an item and verify it is removed.
- Search for items and verify correct results.
- Enter invalid data (negative quantity, empty name) and verify rejection.
- Export to CSV and verify the file content.

## Expected Deliverables

1. Complete application source code.
2. Screenshots showing the main window, add form, and search results.
3. A README with instructions to run the application.

## Evaluation Criteria

| Criterion | Weight | Description |
| :--- | :--- | :--- |
| GUI design | 20% | Clean layout, proper widget usage |
| Database integration | 25% | CRUD operations work, data persists |
| Functionality | 25% | All features working as specified |
| Error handling | 15% | Invalid input handled, no crashes |
| Code organization | 15% | Separation of GUI and database logic |
