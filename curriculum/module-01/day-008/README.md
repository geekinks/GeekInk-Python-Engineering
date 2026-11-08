# Day 008: Debugging Fundamentals

## Learning Objectives

- Recognize and understand common Python error types.
- Read and interpret Python tracebacks to locate errors.
- Use `print()` statements strategically to trace program behavior.
- Apply a systematic approach to finding and fixing bugs.
- Gain confidence in debugging as a normal part of programming.

## Introduction

Every programmer makes mistakes. The difference between a beginner and an experienced engineer is not that one makes fewer errors, but that the experienced one knows how to find and fix them efficiently. Debugging is a skill, and like any skill, it improves with practice.

Python provides helpful error messages when something goes wrong. Learning to read these messages is one of the most important skills you will develop. Today, you will learn to identify common errors, read tracebacks, and use simple techniques to find bugs in your code.

## Concepts

### Common Error Types

| Error Type       | Cause                                          | Example                          |
| ---------------- | ---------------------------------------------- | -------------------------------- |
| `SyntaxError`    | Invalid Python syntax                          | Missing colon, unmatched quotes  |
| `NameError`      | Using a variable that has not been defined      | Typo in variable name            |
| `TypeError`      | Wrong type in an operation                     | Adding a string to an integer    |
| `ValueError`     | Right type but wrong value                     | `int("hello")`                   |
| `IndexError`     | Accessing a list index that does not exist      | `items[10]` when list has 3 items|
| `KeyError`       | Accessing a dictionary key that does not exist  | `data["age"]` when key is missing|
| `ZeroDivisionError` | Dividing by zero                            | `10 / 0`                         |
| `IndentationError` | Incorrect indentation                        | Missing or extra spaces          |

### Reading a Traceback

When Python encounters an error, it prints a traceback. Read it from bottom to top:

```
Traceback (most recent call last):
  File "program.py", line 5, in <module>
    result = 10 / x
ZeroDivisionError: division by zero
```

1. **Last line**: The error type and description. This tells you what went wrong.
2. **Above that**: The file name, line number, and the code that caused it. This tells you where it went wrong.

### Print Debugging

The simplest debugging technique is adding `print()` statements to check the values of variables at different points:

```python
def calculate_discount(price, discount):
    print(f"DEBUG: price={price}, discount={discount}")  # Temporary
    result = price - (price * discount / 100)
    print(f"DEBUG: result={result}")  # Temporary
    return result
```

Remove or comment out debug prints once the bug is fixed.

### Systematic Debugging Process

1. **Read the error message** carefully.
2. **Find the line** where the error occurred.
3. **Check the values** of variables at that point.
4. **Form a hypothesis** about what is wrong.
5. **Test your hypothesis** by making a small change.
6. **Verify** the fix does not break anything else.

## Practical Examples

```python
# SyntaxError — missing colon
# BROKEN:
# if age > 18
#     print("Adult")

# FIXED:
age = 20
if age > 18:
    print("Adult")
```

```python
# NameError — typo in variable name
# BROKEN:
# student_name = "Amina"
# print(studnet_name)

# FIXED:
student_name = "Amina"
print(student_name)
```

```python
# TypeError — mixing types
# BROKEN:
# age = 25
# message = "I am " + age + " years old"

# FIXED:
age = 25
message = "I am " + str(age) + " years old"
print(message)
# Or better: use an f-string
print(f"I am {age} years old")
```

```python
# ValueError — invalid conversion
# BROKEN:
# number = int("twenty")

# FIXED: validate before converting
user_input = "twenty"
if user_input.isdigit():
    number = int(user_input)
else:
    print(f"'{user_input}' is not a valid number")
```

## Guided Practice

Practice reading tracebacks. For each error below, identify:
- The error type
- The line causing the problem
- How to fix it

Create a file called `debug_practice.py` and fix each section:

```python
# Bug 1: Fix the syntax error
# print("Welcome to GeekInk"

# Fixed:
print("Welcome to GeekInk")


# Bug 2: Fix the name error
# first_name = "Yusuf"
# print(f"Hello, {firstname}")

# Fixed:
first_name = "Yusuf"
print(f"Hello, {first_name}")


# Bug 3: Fix the type error
# price = 1500
# quantity = "3"
# total = price * quantity

# Fixed:
price = 1500
quantity = int("3")
total = price * quantity
print(f"Total: {total}")


# Bug 4: Fix the logic error (no crash, wrong result)
# Calculate average of three scores
score1 = 80
score2 = 90
score3 = 70
# BROKEN: average = score1 + score2 + score3 / 3  # Only divides score3
# FIXED:
average = (score1 + score2 + score3) / 3
print(f"Average: {average}")
```

## Daily Challenge

Below are five buggy programs. Create a file called `bug_fixer.py`. For each program, find and fix all the bugs so it runs correctly. Add a comment above each fix explaining what was wrong.

**Program 1: Temperature Converter**
```python
# Convert Celsius to Fahrenheit
celsius = input("Enter temperature in Celsius: )
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius}C = {fahrenheit}F")
```

**Program 2: Age Category**
```python
age = int(input("Enter your age: "))
if age < 13
    category = "Child"
elif age < 20:
    category = "Teenager"
elif age < 60:
    category = "Adult"
else
    category = "Senior"
print(f"You are a {category}")
```

**Program 3: Rectangle Area**
```python
lenght = float(input("Enter length: "))
width = float(input("Enter width: "))
area = lenght * widht
perimeter = 2 * (lenght + width)
print(f"Area: {area}, Perimeter: {perimeter})
```

**Program 4: Name Formatter**
```python
full_name = input("Enter your full name: ")
first = full_name.split()[0]
last = full_name.split()[1]
initials = first[0] + "." + last[0] + "."
print(f"Name: {last, first}")
print(f"Initials: " + intials)
```

**Program 5: Simple Calculator**
```python
num1 = float(input("First number: "))
num2 = float(input("Second number: "))
operation = input("Operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result == num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2

print(f"Result: {reslt}")
```

Fix all bugs in each program. Your final file should run all five programs without errors.

## Expected Output

A single Python file containing all five programs, each corrected and running without errors. Include comments explaining each bug that was found.

## Assessment

1. What is the difference between a `SyntaxError` and a `TypeError`?
2. When reading a traceback, which line should you look at first and why?
3. A program runs without errors but gives the wrong answer. What kind of bug is this, and how do you find it?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-01/day-008/`

Your submission should include:
- `bug_fixer.py` containing all five fixed programs with explanatory comments.

## Additional Resources

- [Python Official Docs — Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Python Official Docs — Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)

## Reflection

- What is the most common type of error you have encountered so far, and what causes it?
- Describe your process for finding a bug. How has it changed since Day 1?
