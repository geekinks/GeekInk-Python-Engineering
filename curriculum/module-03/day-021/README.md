# Day 021: Defining and Calling Functions

## Learning Objectives

- Understand what functions are and why they are essential in software engineering.
- Define functions using the `def` keyword.
- Call functions with and without arguments.
- Apply the DRY (Don't Repeat Yourself) principle by extracting repeated logic into functions.
- Write functions that perform a single, well-defined task.

## Introduction

As your programs grow beyond a few dozen lines, you will quickly find yourself copying and pasting the same blocks of code in multiple places. When a bug appears in that logic, you have to fix it everywhere you copied it. Functions solve this problem. A function is a named, reusable block of code that performs a specific task. You define it once and call it as many times as you need.

Functions are the first major step toward writing professional software. Every library you import, every method you call on a string or list, is a function someone wrote so that others would not have to rewrite the same logic. Learning to write your own functions is learning to think like an engineer: break big problems into small, named, testable pieces.

In this lesson you will define simple functions, call them, and begin to see how they make your code shorter, clearer, and easier to maintain.

## Concepts

### What Is a Function?

A function is a block of code that runs only when it is called. You give it a name, and optionally, inputs (called parameters). When you call the function, it executes its body and optionally returns a result.

### The `def` Keyword

In Python, you create a function with the `def` keyword, followed by the function name, parentheses, and a colon. The body of the function is indented.

```
def function_name():
    # body of the function
    pass
```

### Naming Conventions

Function names should be lowercase, with words separated by underscores (snake_case). They should describe what the function does: `calculate_total`, `print_report`, `is_valid_email`. Avoid vague names like `do_stuff` or single letters like `f`.

### Calling a Function

Defining a function does not run it. You must call it by writing its name followed by parentheses:

```
greet()
```

### The DRY Principle

DRY stands for "Don't Repeat Yourself." If you find yourself writing the same code more than once, extract it into a function. This makes your code easier to read, test, and fix.

## Practical Examples

```python
# Defining a simple function
def greet():
    print("Hello! Welcome to GeekInk Python Engineering.")


# Calling the function
greet()
# Output: Hello! Welcome to GeekInk Python Engineering.


# A function that takes a parameter
def greet_person(name):
    print(f"Hello, {name}! Welcome to the bootcamp.")


greet_person("Amina")
# Output: Hello, Amina! Welcome to the bootcamp.


# A function that returns a value
def add(a, b):
    return a + b


result = add(10, 25)
print(result)
# Output: 35


# A function with no return statement returns None
def say_goodbye():
    print("Goodbye!")


value = say_goodbye()
print(value)
# Output:
# Goodbye!
# None


# Using a function to eliminate repetition
def print_separator():
    print("-" * 40)


print_separator()
print("Student Report")
print_separator()
print("Name: Musa Ibrahim")
print("Grade: A")
print_separator()
```

## Guided Practice

Build a small program step by step.

**Step 1:** Create a function called `display_menu` that prints a numbered list of options.

```python
def display_menu():
    print("1. View grades")
    print("2. Add grade")
    print("3. Exit")
```

**Step 2:** Create a function called `calculate_average` that takes a list of numbers and returns their average.

```python
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count
```

**Step 3:** Use both functions together.

```python
def display_menu():
    print("1. View grades")
    print("2. Add grade")
    print("3. Calculate average")
    print("4. Exit")


def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count


grades = [85, 92, 78, 90, 88]

display_menu()
print()
avg = calculate_average(grades)
print(f"Average grade: {avg}")
```

**Step 4:** Run the program and verify that it prints the menu and the average.

## Daily Challenge

Write a Python file called `utilities.py` that contains the following five functions:

1. `greet(name)` — Takes a name and prints a personalized greeting.
2. `calculate_rectangle_area(length, width)` — Returns the area of a rectangle.
3. `is_even(number)` — Returns `True` if the number is even, `False` otherwise.
4. `celsius_to_fahrenheit(celsius)` — Returns the temperature converted to Fahrenheit using the formula `(celsius * 9/5) + 32`.
5. `count_vowels(text)` — Returns the number of vowels (a, e, i, o, u) in the given text (case-insensitive).

After defining all five functions, add a section at the bottom of the file that calls each function and prints its result. Example:

```
greet("Fatima")
print(calculate_rectangle_area(5, 3))
print(is_even(7))
print(celsius_to_fahrenheit(100))
print(count_vowels("Hello World"))
```

## Expected Output

Your program should produce output similar to:

```
Hello, Fatima! Welcome!
15
False
212.0
3
```

The exact greeting text is up to you, but the numeric results should be correct.

## Assessment

1. What is the difference between defining a function and calling a function?
2. What does a function return if it has no `return` statement?
3. Why is the DRY principle important in software engineering? Give an example of how a function helps you follow it.

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-03/day-021/`

Include your `utilities.py` file.

## Additional Resources

- [Python Official Tutorial: Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [PEP 8 — Naming Conventions](https://peps.python.org/pep-0008/#function-and-variable-names)

## Reflection

- Why is breaking code into functions better than writing one long script?
- Think of a task you do every day. How would you break it into smaller, reusable steps (functions)?
