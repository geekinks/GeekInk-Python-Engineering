# Day 024: Variable Scope

## Learning Objectives

- Understand the difference between local and global scope.
- Learn Python's LEGB rule for name resolution.
- Recognize why global state creates maintenance problems.
- Use the `global` keyword when absolutely necessary and understand its drawbacks.
- Refactor code to eliminate unintended global variable usage.

## Introduction

When you define a variable inside a function, it exists only inside that function. When you define a variable outside all functions, it exists in the global scope. Understanding scope is critical because using the wrong scope leads to bugs that are difficult to track down — a function that silently reads or modifies a variable defined somewhere else in your program.

Professional engineers treat scope seriously. They minimize the use of global variables because globals make it impossible to reason about a function in isolation. If a function depends on or modifies external state, any other part of the program could change that state unexpectedly. Today you will learn how Python resolves variable names and why keeping variables local is almost always the right choice.

## Concepts

### Local Scope

Variables defined inside a function are local to that function. They are created when the function runs and destroyed when it returns.

```python
def greet():
    message = "Hello"    # local variable
    print(message)

greet()
# print(message)  # NameError: 'message' is not defined
```

### Global Scope

Variables defined outside all functions are in the global scope. They can be read (but not reassigned) from inside a function.

```python
school = "GeekInk Academy"

def show_school():
    print(school)    # reads the global variable

show_school()
```

### The LEGB Rule

When Python encounters a variable name, it searches for it in this order:

1. **L**ocal — inside the current function.
2. **E**nclosing — inside any enclosing (outer) functions (for nested functions).
3. **G**lobal — at the module level.
4. **B**uilt-in — Python's built-in names (`print`, `len`, `range`, etc.).

### The `global` Keyword

If you need to modify a global variable inside a function, you must declare it with `global`. Without it, Python treats the assignment as creating a new local variable.

```python
counter = 0

def increment():
    global counter
    counter += 1
```

### Why Global State Is Dangerous

Global variables create hidden dependencies. A function that reads or writes globals cannot be understood, tested, or reused without knowing the entire program's state. Prefer passing values as arguments and returning results.

## Practical Examples

```python
# Local vs global
x = 10   # global

def show():
    x = 20   # local — does NOT change the global x
    print(f"Inside function: x = {x}")

show()
print(f"Outside function: x = {x}")
# Output:
# Inside function: x = 20
# Outside function: x = 10


# LEGB demonstration
name = "Global"

def outer():
    name = "Enclosing"

    def inner():
        name = "Local"
        print(f"inner: {name}")

    inner()
    print(f"outer: {name}")

outer()
print(f"module: {name}")
# Output:
# inner: Local
# outer: Enclosing
# module: Global


# The global keyword (use sparingly)
total_calls = 0

def process_request():
    global total_calls
    total_calls += 1
    print(f"Request #{total_calls} processed")

process_request()
process_request()
print(f"Total: {total_calls}")


# Better approach — avoid globals
def process_request_better(call_count):
    call_count += 1
    print(f"Request #{call_count} processed")
    return call_count

count = 0
count = process_request_better(count)
count = process_request_better(count)
print(f"Total: {count}")


# Shadowing built-ins (a common mistake)
# Don't do this:
# list = [1, 2, 3]        # shadows the built-in list()
# print = "hello"          # shadows the built-in print()
```

## Guided Practice

**Step 1:** Read this buggy program and identify the scope problem.

```python
balance = 1000

def deposit(amount):
    balance = balance + amount    # UnboundLocalError!
    print(f"New balance: {balance}")

def withdraw(amount):
    balance = balance - amount    # UnboundLocalError!
    print(f"New balance: {balance}")

deposit(500)
```

**Step 2:** Fix it the wrong way (using `global`).

```python
balance = 1000

def deposit(amount):
    global balance
    balance = balance + amount
    print(f"New balance: {balance}")

deposit(500)
print(f"Global balance: {balance}")
```

**Step 3:** Fix it the right way (using parameters and return values).

```python
def deposit(balance, amount):
    new_balance = balance + amount
    print(f"New balance: {new_balance}")
    return new_balance

def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient funds")
        return balance
    new_balance = balance - amount
    print(f"New balance: {new_balance}")
    return new_balance

account_balance = 1000
account_balance = deposit(account_balance, 500)
account_balance = withdraw(account_balance, 200)
print(f"Final balance: {account_balance}")
```

## Daily Challenge

You are given the following buggy program. It uses global variables incorrectly and has scope-related bugs. Your task is to refactor it so that:

- No function uses the `global` keyword.
- Every function receives its data through parameters and returns its results.
- The program produces the same correct output.

**Buggy program:**

```python
students = []
total_score = 0
count = 0

def add_student(name, score):
    global students, total_score, count
    students.append({"name": name, "score": score})
    total_score += score
    count += 1

def get_average():
    global total_score, count
    if count == 0:
        return 0
    return total_score / count

def get_best_student():
    global students
    best = None
    for s in students:
        if best is None or s["score"] > best["score"]:
            best = s
    return best

add_student("Amina", 85)
add_student("Musa", 92)
add_student("Fatima", 78)

print(f"Average: {get_average()}")
best = get_best_student()
print(f"Best student: {best['name']} ({best['score']})")
```

Save your refactored version as `scope_refactor.py`.

## Expected Output

```
Average: 85.0
Best student: Musa (92)
```

The output must be identical, but no function should use `global`.

## Assessment

1. What does the LEGB rule stand for, and in what order does Python search for a variable name?
2. Why does assigning to a variable inside a function create a local variable instead of modifying a global one?
3. Give two reasons why using global variables is considered poor engineering practice.

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-03/day-024/`

Include your `scope_refactor.py` file.

## Additional Resources

- [Python Docs: Scopes and Namespaces](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces)
- [Real Python: Python Scope & the LEGB Rule](https://realpython.com/python-scope-legb-rule/)

## Reflection

- Why is it easier to test a function that does not depend on global variables?
- Have you ever encountered a bug in your own code that was caused by accidentally using the wrong variable? How would proper scope management have prevented it?
