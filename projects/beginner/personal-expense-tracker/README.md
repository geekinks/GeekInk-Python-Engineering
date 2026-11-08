# Personal Expense Tracker

**Module:** 3 — Functions, Modules and File Handling
**Day:** 30
**Difficulty:** Beginner

---

## Problem Statement

Managing personal finances requires tracking where money goes. This project builds a command-line expense tracker that records expenses with categories and dates, persists data to files, and provides spending summaries. It reinforces functions, file I/O, and data processing with CSV and JSON.

## Objectives

- Design and implement a modular program using functions.
- Read and write data using CSV and JSON formats.
- Organize code into reusable modules.
- Implement CRUD operations (Create, Read, Update, Delete) on file-backed data.
- Calculate and display spending summaries and category breakdowns.

## Requirements

### Functional Requirements

1. **Expense recording:**
   - Each expense has: date, amount, category, and description.
   - Categories include: Food, Transport, Education, Utilities, Entertainment, Health, Other.
   - Date defaults to today if not provided.

2. **Data persistence:**
   - Store expenses in a CSV file (`expenses.csv`).
   - Store application settings or summary cache in a JSON file (`config.json`).
   - Data must survive program restarts.

3. **Operations:**
   - **Add** a new expense.
   - **View** all expenses (optionally filtered by category or date range).
   - **Search** expenses by keyword in description.
   - **Delete** an expense by its ID.
   - **Summary** showing total spending, spending by category, and monthly totals.

4. **Display:**
   - Expenses displayed in a formatted table.
   - Summary shows category breakdown with percentages.

### Non-Functional Requirements

- The program must handle empty data files gracefully.
- Currency should be displayed with two decimal places.
- Code must be organized into at least two modules (e.g., `main.py` and `expense_utils.py`).

## Features

| Feature | Description |
| :--- | :--- |
| Add expense | Record an expense with amount, category, date, description |
| View expenses | Display all or filtered expenses in a table |
| Search | Find expenses by keyword |
| Delete | Remove an expense by ID |
| Category summary | Show totals and percentages per category |
| Monthly summary | Show spending totals per month |
| File persistence | Data saved to and loaded from CSV |

## Suggested Architecture

```
personal-expense-tracker/
├── main.py              — Entry point, menu loop, user interaction
├── expense_utils.py     — Functions for CRUD, calculations, formatting
├── expenses.csv         — Data file (created at runtime)
└── config.json          — Settings file (created at runtime)
```

Key functions in `expense_utils.py`:

- `load_expenses(filepath)` — Read expenses from CSV, return list of dicts.
- `save_expenses(filepath, expenses)` — Write expenses to CSV.
- `add_expense(expenses, amount, category, description, date)` — Append a new record.
- `delete_expense(expenses, expense_id)` — Remove by ID.
- `filter_by_category(expenses, category)` — Return filtered list.
- `filter_by_date_range(expenses, start_date, end_date)` — Return filtered list.
- `calculate_summary(expenses)` — Return totals by category.
- `display_table(expenses)` — Print formatted table.

## Technologies

- Python 3.10+
- Standard library only (`csv`, `json`, `datetime`, `os`)

## Implementation Milestones

| Milestone | Description |
| :--- | :--- |
| 1. Data model | Define expense structure, create load/save functions |
| 2. Add and view | Implement adding expenses and displaying them |
| 3. File persistence | Save to and load from CSV |
| 4. Search and delete | Implement search by keyword and delete by ID |
| 5. Summaries | Calculate and display category and monthly summaries |
| 6. Polish | Input validation, edge cases, clean formatting |

## Testing Requirements

Manually verify:

| Scenario | Expected Behavior |
| :--- | :--- |
| Add an expense, restart program, view | Expense is still there (file persistence works) |
| Add expenses in multiple categories | Summary shows correct totals and percentages |
| Delete an expense | Expense removed, IDs remain consistent |
| Search for "lunch" | Only expenses with "lunch" in description shown |
| Empty data file | Program starts normally, no crash |
| Non-numeric amount input | Error message and re-prompt |

## Expected Deliverables

1. `main.py` — Entry point with menu loop.
2. `expense_utils.py` — Utility functions module.
3. Sample `expenses.csv` with at least 10 example records.
4. Sample output showing the expense table and a category summary.

## Evaluation Criteria

| Criterion | Weight | Description |
| :--- | :--- | :--- |
| File I/O | 25% | CSV read/write works correctly, data persists |
| Code modularity | 20% | Functions are well-defined, code split into modules |
| Correct calculations | 20% | Summaries and totals are accurate |
| Error handling | 15% | Invalid input and edge cases handled |
| User experience | 10% | Menu is clear, output is formatted |
| Completeness | 10% | All required operations implemented |
