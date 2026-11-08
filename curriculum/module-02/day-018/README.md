# Day 018: Exception Handling

## Learning Objectives

- Understand what exceptions are and why they occur.
- Use `try/except` blocks to handle errors gracefully.
- Use `else` and `finally` clauses for complete error handling.
- Raise exceptions intentionally with `raise`.
- Handle specific exception types instead of catching everything.

## Introduction

Programs crash when they encounter situations they cannot handle: dividing by zero, converting invalid text to a number, accessing a file that does not exist. Instead of letting your program crash, you can anticipate these situations and handle them gracefully using exception handling.

Exception handling is essential for building robust software. A good program does not just work when everything goes right — it handles failures cleanly and gives the user helpful feedback.

## Concepts

### The try/except Block

```python
try:
    # Code that might cause an error
    result = 10 / 0
except ZeroDivisionError:
    # Code that runs if the error occurs
    print("Cannot divide by zero!")
```

### Multiple except Clauses

```python
try:
    value = int(input("Enter a number: "))
    result = 100 / value
except ValueError:
    print("That is not a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

### else and finally

```python
try:
    value = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
else:
    # Runs only if no exception occurred
    print(f"You entered: {value}")
finally:
    # Runs no matter what
    print("Input processing complete.")
```

### Raising Exceptions

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age is unrealistically high")
    return age
```

### Common Exception Types

| Exception           | When it occurs                              |
| -------------------- | ------------------------------------------- |
| `ValueError`         | Wrong value for the type                    |
| `TypeError`          | Wrong type in an operation                  |
| `KeyError`           | Dictionary key not found                    |
| `IndexError`         | List index out of range                     |
| `FileNotFoundError`  | File does not exist                         |
| `ZeroDivisionError`  | Division by zero                            |
| `AttributeError`     | Object does not have the attribute/method   |

## Practical Examples

```python
# Safe number input
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

price = get_number("Enter price: ")
print(f"Price: {price}")
```

```python
# Safe dictionary access
student = {"name": "Fatima", "age": 20}

try:
    email = student["email"]
except KeyError:
    email = "Not provided"
    print("Email not found in student record.")

print(f"Email: {email}")
```

```python
# Safe list access
scores = [85, 92, 78]

try:
    print(scores[5])
except IndexError:
    print(f"Index out of range. List has {len(scores)} items.")
```

```python
# Raising and catching custom validation errors
def validate_score(score):
    if not isinstance(score, (int, float)):
        raise TypeError(f"Score must be a number, got {type(score).__name__}")
    if score < 0 or score > 100:
        raise ValueError(f"Score must be between 0 and 100, got {score}")
    return score

try:
    validated = validate_score(105)
except ValueError as e:
    print(f"Validation error: {e}")
except TypeError as e:
    print(f"Type error: {e}")
```

```python
# Using else and finally together
filename = "data.txt"
try:
    with open(filename) as f:
        content = f.read()
except FileNotFoundError:
    print(f"File '{filename}' not found.")
    content = None
else:
    print(f"File loaded: {len(content)} characters.")
finally:
    print("File operation complete.")
```

## Guided Practice

Create a file called `safe_calculator.py`:

Build a calculator that never crashes, no matter what the user enters.

```python
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Try again.")

def calculate(a, b, operation):
    try:
        if operation == "+":
            return a + b
        elif operation == "-":
            return a - b
        elif operation == "*":
            return a * b
        elif operation == "/":
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return a / b
        else:
            raise ValueError(f"Unknown operation: {operation}")
    except (ZeroDivisionError, ValueError) as e:
        return f"Error: {e}"

print("Safe Calculator")
print("-" * 20)

num1 = get_number("First number: ")
num2 = get_number("Second number: ")
op = input("Operation (+, -, *, /): ").strip()

result = calculate(num1, num2, op)
print(f"Result: {result}")
```

## Daily Challenge

Build a program called `input_validator.py` that provides a robust data collection system:

1. Create validation functions that raise appropriate exceptions:
   - `validate_name(name)`: Must not be empty, must contain only letters and spaces.
   - `validate_age(age_str)`: Must be a positive integer between 1 and 120.
   - `validate_email(email)`: Must contain exactly one `@` and at least one `.` after the `@`.
   - `validate_phone(phone)`: Must be exactly 11 digits.
   - `validate_score(score_str)`: Must be a number between 0 and 100.

2. Create a `get_valid_input(prompt, validator)` function that keeps asking until valid input is provided, catching exceptions and displaying the error message.

3. Use these functions to collect a complete student registration:
   - Name, age, email, phone, and three subject scores.

4. Display the collected information in a formatted card.

Example interaction:

```
===== STUDENT REGISTRATION =====

Enter name: 
Error: Name cannot be empty.
Enter name: John123
Error: Name must contain only letters and spaces.
Enter name: Musa Abdullahi

Enter age: abc
Error: Age must be a whole number.
Enter age: 200
Error: Age must be between 1 and 120.
Enter age: 22

Enter email: musa
Error: Invalid email format.
Enter email: musa@university.edu.ng

Enter phone: 0801234
Error: Phone must be exactly 11 digits.
Enter phone: 08012345678

Enter Math score: 150
Error: Score must be between 0 and 100.
Enter Math score: 85

...

===== REGISTRATION COMPLETE =====
Name:    Musa Abdullahi
Age:     22
Email:   musa@university.edu.ng
Phone:   08012345678
Math:    85
English: 72
Science: 90
Average: 82.3
=================================
```

## Expected Output

A registration system that validates every input, never crashes, gives clear error messages, and displays a final summary of all collected data.

## Assessment

1. What is the difference between using `try/except` and checking with `if` statements before an operation?
2. Why should you catch specific exceptions rather than using a bare `except:`?
3. When does the `else` block in a `try/except/else` execute?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-02/day-018/`

Your submission should include:
- `input_validator.py` containing your solution to the daily challenge.

## Additional Resources

- [Python Official Docs — Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Python Official Docs — Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)

## Reflection

- How does exception handling change the user experience of your programs?
- What is the trade-off between catching too many exceptions and too few?
