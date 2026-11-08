# Day 030: Module 3 Project — Personal Expense Tracker

## Learning Objectives

- Apply functions, modules, and file handling to build a complete CLI application.
- Design a program with clear separation of concerns using multiple functions.
- Persist data using CSV or JSON files.
- Handle user input, validation, and edge cases.
- Practice project organization and documentation.

## Introduction

This is your Module 3 milestone project. Over the past ten days you have learned to write functions, create modules, handle files, work with CSV and JSON, and manage dependencies. Now you will bring it all together to build a Personal Expense Tracker — a command-line application that helps users record, categorize, search, and analyze their daily expenses.

This project tests your ability to design a real application from scratch. You will need to think about data storage, user interaction, input validation, and code organization. Treat this like a professional engineering assignment: plan before you code, keep your functions small and focused, and test your program thoroughly.

## Project Description

Build a command-line Personal Expense Tracker that allows users to:

1. **Add an expense** — Record an expense with a description, amount, category, and date.
2. **View all expenses** — Display all recorded expenses in a formatted table.
3. **View expenses by category** — Filter and display expenses for a specific category.
4. **View expenses by date range** — Filter expenses between two dates.
5. **View spending summary** — Show total spending and totals per category.
6. **Search expenses** — Search by keyword in the description.
7. **Delete an expense** — Remove an expense by its ID.
8. **Export to CSV** — Save all expenses to a CSV file.
9. **Exit** — Save data and exit the program.

## Requirements

### Data Storage

- Store expenses in a JSON file called `expenses.json`.
- Each expense should have: `id`, `description`, `amount`, `category`, `date`.
- Load data from file on startup. Save data on every modification.

### Categories

Support at least these categories (users can also type a custom category):
- Food
- Transport
- Education
- Health
- Entertainment
- Bills
- Other

### Input Validation

- Amount must be a positive number.
- Date should default to today if not provided, but allow manual entry in `YYYY-MM-DD` format.
- Description cannot be empty.

### Code Organization

Organize your code into at least two files:

```
day-030/
    expense_tracker.py     # Main program with menu and user interaction
    tracker_utils.py       # Functions for data operations (add, delete, search, summarize, file I/O)
```

## Suggested Architecture

```python
# tracker_utils.py

def load_expenses(filename="expenses.json"):
    """Load expenses from JSON file. Return empty list if file doesn't exist."""
    pass

def save_expenses(expenses, filename="expenses.json"):
    """Save expenses list to JSON file."""
    pass

def add_expense(expenses, description, amount, category, date):
    """Add a new expense and return the updated list."""
    pass

def delete_expense(expenses, expense_id):
    """Delete an expense by ID. Return True if found and deleted."""
    pass

def search_expenses(expenses, keyword):
    """Return expenses whose description contains the keyword."""
    pass

def filter_by_category(expenses, category):
    """Return expenses matching the given category."""
    pass

def filter_by_date_range(expenses, start_date, end_date):
    """Return expenses within the date range."""
    pass

def get_summary(expenses):
    """Return total spending and per-category totals."""
    pass

def export_to_csv(expenses, filename="expenses.csv"):
    """Export expenses to a CSV file."""
    pass

def generate_id(expenses):
    """Generate the next unique ID."""
    pass
```

```python
# expense_tracker.py

from tracker_utils import (
    load_expenses, save_expenses, add_expense, delete_expense,
    search_expenses, filter_by_category, filter_by_date_range,
    get_summary, export_to_csv
)

def display_menu():
    """Display the main menu."""
    pass

def display_expenses(expenses):
    """Display expenses in a formatted table."""
    pass

def main():
    """Main application loop."""
    pass

if __name__ == "__main__":
    main()
```

## Implementation Milestones

Work through these milestones in order:

1. **Milestone 1:** Create `tracker_utils.py` with `load_expenses`, `save_expenses`, `add_expense`, and `generate_id`. Test them manually.

2. **Milestone 2:** Create `expense_tracker.py` with the menu loop. Implement "Add expense" and "View all expenses".

3. **Milestone 3:** Add "View by category" and "Spending summary".

4. **Milestone 4:** Add "Search", "Delete", and "Date range filter".

5. **Milestone 5:** Add "Export to CSV". Test the complete application end to end.

## Testing Requirements

Test your program with these scenarios:

- Add 5+ expenses across different categories and dates.
- View all expenses and verify formatting.
- Filter by category and confirm only matching expenses appear.
- Search for a keyword and confirm results.
- View the spending summary and verify totals are correct.
- Delete an expense and confirm it is removed.
- Export to CSV and open the file to verify correctness.
- Exit and restart the program to verify data persists.

## Expected Deliverables

Submit the following files:

- `expense_tracker.py` — Main program.
- `tracker_utils.py` — Utility functions.
- `README.md` — A short project README explaining what the program does, how to run it, and the features it supports.

Do not include generated data files (`expenses.json`, `expenses.csv`).

## Evaluation Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Functionality | 30% | All required features work correctly. |
| Code organization | 20% | Logic split into functions and modules. Functions are focused and reusable. |
| File handling | 20% | Data persists correctly. CSV export works. Edge cases handled. |
| Input validation | 15% | Invalid input is caught and reported without crashing. |
| Code readability | 15% | Clear variable names, consistent formatting, no dead code. |

## Example Session

```
=== Personal Expense Tracker ===

1. Add expense
2. View all expenses
3. View by category
4. View by date range
5. Spending summary
6. Search expenses
7. Delete expense
8. Export to CSV
9. Exit

Choice: 1
Description: Lunch at campus
Amount: 1500
Category (Food/Transport/Education/Health/Entertainment/Bills/Other): Food
Date (YYYY-MM-DD, or press Enter for today): 
Expense added! (ID: 1)

Choice: 1
Description: Bus fare to class
Amount: 200
Category: Transport
Date: 
Expense added! (ID: 2)

Choice: 5

=== Spending Summary ===
Total expenses: 1,700.00

By category:
  Food:        1,500.00
  Transport:     200.00

Choice: 9
Data saved. Goodbye!
```

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-03/day-030/`

## Additional Resources

- [Python Docs: json module](https://docs.python.org/3/library/json.html)
- [Python Docs: csv module](https://docs.python.org/3/library/csv.html)
- [Python Docs: datetime module](https://docs.python.org/3/library/datetime.html)

## Reflection

- What was the most challenging part of building this project?
- How did splitting your code into two files affect your development process?
- If you were to add one more feature to this expense tracker, what would it be and why?
