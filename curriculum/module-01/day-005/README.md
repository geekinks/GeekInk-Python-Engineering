# Day 005: User Input and Output

## Learning Objectives

- Use `input()` to receive data from the user at runtime.
- Understand that `input()` always returns a string.
- Format output using `print()`, f-strings, and format specifiers.
- Use escape characters for special output formatting.
- Build interactive programs that respond to user input.

## Introduction

So far, your programs have used hardcoded values. Real programs need to interact with users. They ask questions, receive answers, process the information, and present results. The `input()` function is your gateway to making programs interactive.

Equally important is how you present output. A well-formatted result is easier to read and more professional. Today you will learn to build programs that have a complete interaction loop: ask, receive, process, and display.

## Concepts

### The `input()` Function

`input()` pauses the program and waits for the user to type something and press Enter. It always returns a string, regardless of what the user types.

```python
name = input("What is your name? ")
# User types: Aliyu
# name is now the string "Aliyu"
```

To get a number from the user, you must convert the input:

```python
age = int(input("Enter your age: "))
price = float(input("Enter the price: "))
```

### Output Formatting

**f-strings** are the most readable way to format output:

```python
name = "Bilal"
score = 92.567
print(f"Student: {name}, Score: {score:.1f}%")
# Student: Bilal, Score: 92.6%
```

**Format specifiers** inside f-strings:

| Specifier | Meaning                          | Example                  |
| --------- | -------------------------------- | ------------------------ |
| `:.2f`    | Float with 2 decimal places     | `f"{3.14159:.2f}"` = `"3.14"` |
| `:,`      | Number with comma separators     | `f"{1000000:,}"` = `"1,000,000"` |
| `:>10`    | Right-align in 10 characters     | `f"{'hi':>10}"` = `"        hi"` |
| `:<10`    | Left-align in 10 characters      | `f"{'hi':<10}"` = `"hi        "` |
| `:^10`    | Center in 10 characters          | `f"{'hi':^10}"` = `"    hi    "` |

### Escape Characters

| Character | Meaning        |
| --------- | -------------- |
| `\n`      | New line       |
| `\t`      | Tab            |
| `\\`      | Backslash      |
| `\'`      | Single quote   |
| `\"`      | Double quote   |

## Practical Examples

```python
# Basic input and output
name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to GeekInk.")
```

```python
# Numeric input with formatting
price = float(input("Enter item price in Naira: "))
quantity = int(input("Enter quantity: "))
total = price * quantity
print(f"Total: {total:,.2f} Naira")
```

```python
# Aligned output
print(f"{'Item':<20} {'Qty':>5} {'Price':>10}")
print(f"{'-'*20} {'-'*5} {'-'*10}")
print(f"{'Rice (50kg)':<20} {3:>5} {45000:>10,}")
print(f"{'Cooking Oil':<20} {2:>5} {8500:>10,}")
print(f"{'Sugar (10kg)':<20} {1:>5} {12000:>10,}")
```

```python
# Using escape characters
print("Name:\tAisha Bello")
print("Dept:\tComputer Science")
print("---")
print("She said, \"Python is amazing!\"")
print("File path: C:\\Users\\Documents\\project")
```

## Guided Practice

Create a file called `receipt.py` that simulates a simple shop receipt:

1. Ask the user for their name.
2. Ask for three item names and their prices.
3. Calculate the subtotal, a 7.5% VAT, and the grand total.
4. Print a formatted receipt.

```python
customer = input("Customer name: ")
item1 = input("Item 1 name: ")
price1 = float(input("Item 1 price: "))
item2 = input("Item 2 name: ")
price2 = float(input("Item 2 price: "))
item3 = input("Item 3 name: ")
price3 = float(input("Item 3 price: "))

subtotal = price1 + price2 + price3
vat = subtotal * 0.075
total = subtotal + vat

print()
print("=" * 40)
print(f"{'GEEKINK STORE':^40}")
print("=" * 40)
print(f"Customer: {customer}")
print("-" * 40)
print(f"{item1:<25} {price1:>10,.2f}")
print(f"{item2:<25} {price2:>10,.2f}")
print(f"{item3:<25} {price3:>10,.2f}")
print("-" * 40)
print(f"{'Subtotal':<25} {subtotal:>10,.2f}")
print(f"{'VAT (7.5%)':<25} {vat:>10,.2f}")
print(f"{'TOTAL':<25} {total:>10,.2f}")
print("=" * 40)
print(f"{'Thank you for shopping!':^40}")
```

## Daily Challenge

Build a program called `profile_generator.py` that creates an interactive personal profile:

1. Ask the user for:
   - Full name
   - Year of birth
   - City
   - Occupation or field of study
   - Favorite programming language
   - A personal motto or goal

2. Calculate their age (use 2024 as the current year, or use `from datetime import datetime` and `datetime.now().year`).

3. Generate and display a formatted profile card:

```
+------------------------------------------+
|          PERSONAL PROFILE CARD           |
+------------------------------------------+
| Name:       Umar Farouq                  |
| Age:        23 years old                 |
| City:       Bauchi                       |
| Field:      Software Engineering         |
| Language:   Python                       |
+------------------------------------------+
| Motto: "Build solutions, not excuses."   |
+------------------------------------------+
```

The card should have consistent borders and alignment regardless of the length of the user's input.

## Expected Output

A well-formatted profile card with bordered sections, aligned labels, and calculated age. The card should look professional and consistent.

## Assessment

1. Why does `input()` always return a string, even when the user types a number?
2. What does `f"{value:>15,.2f}"` do to the value `12345.6`?
3. What will `print("Hello\nWorld")` display?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-01/day-005/`

Your submission should include:
- `profile_generator.py` containing your solution to the daily challenge.

## Additional Resources

- [Python Official Docs — input()](https://docs.python.org/3/library/functions.html#input)
- [Python Official Docs — Format Specification Mini-Language](https://docs.python.org/3/library/string.html#format-specification-mini-language)

## Reflection

- How does getting input from users change the way you think about writing a program?
- Why is output formatting important in professional software?
