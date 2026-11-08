# Day 032: Classes and Objects

## Learning Objectives

- Define classes using the `class` keyword.
- Create objects (instances) from a class.
- Understand the relationship between a class (blueprint) and an object (instance).
- Use `type()`, `id()`, and `isinstance()` to inspect objects.
- Recognize that everything in Python is an object.

## Introduction

Yesterday you learned why OOP exists. Today you start building with it. A class is a blueprint — a template that defines what data and behavior a type of object will have. An object is a specific instance built from that blueprint. You define one `Student` class, then create as many individual students as you need, each with their own name, age, and scores.

This is the same relationship as an architectural blueprint and the buildings constructed from it. The blueprint specifies the structure; each building is a real, independent entity. Understanding this distinction between class and object is the foundation of everything that follows in OOP.

**Reference:** [Lecture 02 — Classes and Objects](../../../python-oop/lectures/02-classes-and-objects.md)
**Exercise:** [Exercise 01 — Classes and Objects](../../../python-oop/exercises/01-classes-and-objects/)

## Concepts

### Defining a Class

```python
class Student:
    pass
```

By convention, class names use PascalCase (capitalize each word, no underscores).

### Creating Objects

```python
student1 = Student()
student2 = Student()
```

Each call to `Student()` creates a new, independent object.

### Adding Attributes

You can add attributes to an object at any time:

```python
student1.name = "Amina"
student1.age = 20
```

However, the standard practice is to set attributes in the `__init__` method (covered tomorrow).

### Inspecting Objects

```python
print(type(student1))           # <class '__main__.Student'>
print(id(student1))             # Unique memory address
print(isinstance(student1, Student))  # True
print(student1 is student2)     # False — different objects
```

### Everything Is an Object

In Python, every value is an object — integers, strings, lists, functions, and even classes themselves.

```python
print(type(42))        # <class 'int'>
print(type("hello"))   # <class 'str'>
print(type([1, 2]))    # <class 'list'>
```

## Practical Examples

```python
# Defining a simple class
class Car:
    pass


# Creating instances
car1 = Car()
car2 = Car()

# Adding attributes
car1.make = "Toyota"
car1.model = "Corolla"
car1.year = 2020

car2.make = "Honda"
car2.model = "Civic"
car2.year = 2022

print(f"{car1.make} {car1.model} ({car1.year})")
print(f"{car2.make} {car2.model} ({car2.year})")


# Each object is independent
print(f"car1 type: {type(car1)}")
print(f"car1 id: {id(car1)}")
print(f"car2 id: {id(car2)}")
print(f"Same object? {car1 is car2}")


# isinstance checks
print(isinstance(car1, Car))   # True
print(isinstance(car1, str))   # False


# A class with a method
class Greeter:
    def say_hello(self):
        print("Hello from GeekInk!")

g = Greeter()
g.say_hello()


# Multiple objects from the same class
class Student:
    pass

students = []
names = ["Amina", "Musa", "Fatima"]
for name in names:
    s = Student()
    s.name = name
    students.append(s)

for s in students:
    print(f"Student: {s.name}, type: {type(s).__name__}, id: {id(s)}")
```

## Guided Practice

**Step 1:** Define a `Book` class.

```python
class Book:
    pass
```

**Step 2:** Create three book objects and assign attributes.

```python
book1 = Book()
book1.title = "Things Fall Apart"
book1.author = "Chinua Achebe"
book1.pages = 209

book2 = Book()
book2.title = "Half of a Yellow Sun"
book2.author = "Chimamanda Ngozi Adichie"
book2.pages = 433

book3 = Book()
book3.title = "Purple Hibiscus"
book3.author = "Chimamanda Ngozi Adichie"
book3.pages = 307
```

**Step 3:** Store them in a list and display them.

```python
library = [book1, book2, book3]

for book in library:
    print(f"'{book.title}' by {book.author} — {book.pages} pages")
```

**Step 4:** Verify they are all Book instances.

```python
for book in library:
    print(f"{book.title}: isinstance(Book)? {isinstance(book, Book)}")
```

## Daily Challenge

Create a file called `bank_account.py`:

1. Define a `BankAccount` class.
2. Create at least 3 bank account objects.
3. Assign these attributes to each: `owner` (string), `account_number` (string), `balance` (float), `account_type` (string: "savings" or "current").
4. Store all accounts in a list.
5. Write a function `display_accounts(accounts)` that prints a formatted list of all accounts.
6. Write a function `find_account(accounts, account_number)` that searches for an account by number and returns it (or `None` if not found).
7. Write a function `total_deposits(accounts)` that returns the sum of all balances.
8. Use `type()`, `id()`, and `isinstance()` to demonstrate that your objects are instances of `BankAccount`.

## Expected Output

```
=== Bank Accounts ===
Owner: Amina Bello | Account: 1001 | Type: savings | Balance: 50,000.00
Owner: Musa Ibrahim | Account: 1002 | Type: current | Balance: 125,000.00
Owner: Fatima Yusuf | Account: 1003 | Type: savings | Balance: 75,000.00

Searching for account 1002...
Found: Musa Ibrahim (current) — Balance: 125,000.00

Total deposits across all accounts: 250,000.00

Object inspection:
  Amina's account — type: BankAccount, id: 140234567890, is BankAccount: True
```

## Assessment

1. What is the relationship between a class and an object?
2. What do `type()`, `id()`, and `isinstance()` tell you about an object?
3. Why does `student1 is student2` return `False` even if both have the same name and age?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-04/day-032/`

Include your `bank_account.py` file.

## Additional Resources

- [Lecture 02 — Classes and Objects](../../../python-oop/lectures/02-classes-and-objects.md)
- [Exercise 01 — Classes and Objects](../../../python-oop/exercises/01-classes-and-objects/)
- [Python Docs: Classes — A First Look](https://docs.python.org/3/tutorial/classes.html#a-first-look-at-classes)

## Reflection

- How is creating an object from a class similar to using a template or form in real life?
- What advantages does storing data in objects have over storing it in dictionaries?
