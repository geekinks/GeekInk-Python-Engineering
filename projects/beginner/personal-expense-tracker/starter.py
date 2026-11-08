"""
Personal Expense Tracker
Module 3 Project — GeekInk Python Engineering

A CLI application that records, persists, and summarizes personal expenses.
"""

import csv
import json
import os
from datetime import datetime

DATA_FILE = "expenses.csv"
CONFIG_FILE = "config.json"
CATEGORIES = ["Food", "Transport", "Education", "Utilities", "Entertainment", "Health", "Other"]
CSV_FIELDS = ["id", "date", "amount", "category", "description"]


def load_expenses(filepath):
    """Load expenses from a CSV file. Return an empty list if the file does not exist."""
    # TODO: Use csv.DictReader to read the file.
    # Convert amount to float and id to int.
    # Return a list of dictionaries.
    pass


def save_expenses(filepath, expenses):
    """Save the list of expenses to a CSV file."""
    # TODO: Use csv.DictWriter with CSV_FIELDS as fieldnames.
    # Write the header and all rows.
    pass


def generate_id(expenses):
    """Generate the next expense ID."""
    # TODO: Return max existing ID + 1, or 1 if the list is empty.
    pass


def add_expense(expenses, amount, category, description, date=None):
    """Create a new expense record and append it to the list."""
    # TODO: Build the expense dictionary with a generated ID.
    # Default date to today if not provided.
    # Append to the expenses list.
    pass


def delete_expense(expenses, expense_id):
    """Remove an expense by its ID. Return True if found, False otherwise."""
    # TODO: Find and remove the expense with the matching ID.
    pass


def filter_by_category(expenses, category):
    """Return expenses matching the given category."""
    # TODO: Use a list comprehension to filter.
    pass


def filter_by_date_range(expenses, start_date, end_date):
    """Return expenses within the given date range (inclusive)."""
    # TODO: Parse dates and filter. Dates are strings in "YYYY-MM-DD" format.
    pass


def search_expenses(expenses, keyword):
    """Return expenses where the description contains the keyword (case-insensitive)."""
    # TODO: Filter by keyword in description.
    pass


def calculate_summary(expenses):
    """Calculate total spending and per-category breakdown with percentages."""
    # TODO: Return a dictionary with:
    # "total": total amount
    # "categories": {category: {"total": amount, "percentage": pct}, ...}
    pass


def display_table(expenses):
    """Display expenses in a formatted table."""
    # TODO: Print aligned columns:
    # ID | Date       | Amount    | Category      | Description
    # ---|------------|-----------|---------------|------------------
    #  1 | 2025-01-15 |   1500.00 | Food          | Lunch at cafeteria
    pass


def display_summary(expenses):
    """Display the spending summary with category breakdown."""
    # TODO: Call calculate_summary and print the results.
    pass


def main():
    """Main menu loop."""
    expenses = load_expenses(DATA_FILE)
    print("Personal Expense Tracker")
    print("=" * 30)

    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View by Category")
        print("4. Search Expenses")
        print("5. Delete Expense")
        print("6. Spending Summary")
        print("7. Exit")

        choice = input("\nSelect an option (1-7): ").strip()

        if choice == "7":
            save_expenses(DATA_FILE, expenses)
            print("Data saved. Goodbye!")
            break
        else:
            # TODO: Implement each menu option.
            # Remember to save after modifications.
            print("Option not yet implemented.")


if __name__ == "__main__":
    main()
