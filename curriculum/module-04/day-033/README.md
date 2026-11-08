# Day 033: Attributes, Methods, and self

## Learning Objectives

- Define instance attributes that store object state.
- Define methods that operate on an object's data.
- Understand what `self` is and how Python uses it.
- Know the difference between a function and a method.
- Build classes with meaningful behavior.

## Introduction

Yesterday you created objects and assigned attributes to them after creation. That approach works but is fragile — nothing ensures that every object has the attributes it needs. Today you will learn the proper way to give objects their data (through instance attributes) and their behavior (through methods).

The key concept is `self`. Every method in a class receives `self` as its first parameter. `self` refers to the specific object the method was called on. When you write `amina.deposit(500)`, Python translates this to `BankAccount.deposit(amina, 500)`. Understanding this translation is essential to understanding how OOP works in Python.

**Reference:** [Lecture 03 — Attributes, Methods & self](../../../python-oop/lectures/03-attributes-methods-and-self.md)
**Exercise:** [Exercise 02 — Attributes and Methods](../../../python-oop/exercises/02-attributes-and-methods/)

## Concepts

### Instance Attributes

Attributes store an object's state. They are set on `self` inside methods.

```python
class Student:
    def set_info(self, name, age):
        self.name = name
        self.age = age
```

### Methods

Methods are functions defined inside a class. They always take `self` as their first parameter.

```python
class Student:
    def set_info(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"{self.name}, age {self.age}")
```

### How `self` Works

When you call `student.display()`, Python automatically passes the object as the first argument:

```python
student = Student()
student.set_info("Amina", 20)
student.display()

# Python internally does:
# Student.display(student)
```

`self` is not a keyword — it is a convention. You could name it anything, but all Python developers use `self`.

### Function vs Method

A function is standalone. A method belongs to a class and operates on an object's data through `self`.

## Practical Examples

```python
class BankAccount:
    def set_up(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
            return
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")

    def get_balance(self):
        return self.balance

    def display(self):
        print(f"Account: {self.owner} | Balance: {self.balance:,.2f}")


# Create and use objects
acc1 = BankAccount()
acc1.set_up("Amina", 50000)
acc1.display()

acc1.deposit(10000)
acc1.withdraw(5000)
acc1.display()

acc2 = BankAccount()
acc2.set_up("Musa", 30000)
acc2.deposit(20000)
acc2.display()

# Each object has its own state
print(f"\nAmina's balance: {acc1.get_balance():,.2f}")
print(f"Musa's balance: {acc2.get_balance():,.2f}")
```

```python
# Demonstrating self explicitly
class Counter:
    def reset(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count


c1 = Counter()
c1.reset()
c1.increment()
c1.increment()
c1.increment()

c2 = Counter()
c2.reset()
c2.increment()

print(f"c1: {c1.get_count()}")   # 3
print(f"c2: {c2.get_count()}")   # 1

# c1 and c2 have independent state
```

```python
# A class with methods that return values for chaining logic
class Rectangle:
    def set_dimensions(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def display(self):
        shape = "Square" if self.is_square() else "Rectangle"
        print(f"{shape}: {self.width}x{self.height} | Area: {self.area()} | Perimeter: {self.perimeter()}")


r1 = Rectangle()
r1.set_dimensions(5, 3)
r1.display()

r2 = Rectangle()
r2.set_dimensions(4, 4)
r2.display()
```

## Guided Practice

Build a `StudentGrade` class step by step.

**Step 1:** Define the class with a method to set student data.

```python
class StudentGrade:
    def set_info(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.scores = []
```

**Step 2:** Add a method to record scores.

```python
    def add_score(self, subject, score):
        self.scores.append({"subject": subject, "score": score})
```

**Step 3:** Add methods for calculations.

```python
    def average(self):
        if not self.scores:
            return 0
        total = sum(s["score"] for s in self.scores)
        return total / len(self.scores)

    def highest_score(self):
        if not self.scores:
            return None
        return max(self.scores, key=lambda s: s["score"])

    def is_passing(self):
        return self.average() >= 50
```

**Step 4:** Add a display method.

```python
    def display_report(self):
        print(f"\nStudent: {self.name} (ID: {self.student_id})")
        print("-" * 30)
        for s in self.scores:
            print(f"  {s['subject']}: {s['score']}")
        print("-" * 30)
        print(f"  Average: {self.average():.1f}")
        status = "PASS" if self.is_passing() else "FAIL"
        print(f"  Status: {status}")
```

**Step 5:** Use the class.

```python
s1 = StudentGrade()
s1.set_info("Amina Bello", "STU001")
s1.add_score("Math", 85)
s1.add_score("English", 90)
s1.add_score("Science", 78)
s1.display_report()

best = s1.highest_score()
print(f"Highest: {best['subject']} ({best['score']})")
```

## Daily Challenge

Expand the `BankAccount` class from yesterday into a fully featured version. Create a file called `bank_system.py`:

Define a `BankAccount` class with these methods:

1. `set_up(self, owner, account_number, balance, account_type)` — Initialize the account.
2. `deposit(self, amount)` — Add money. Reject negative amounts.
3. `withdraw(self, amount)` — Remove money. Reject if insufficient funds or negative amount.
4. `get_balance(self)` — Return the current balance.
5. `transfer(self, other_account, amount)` — Transfer money to another BankAccount. Withdraw from self, deposit to other.
6. `get_statement(self)` — Return a list of all transactions (maintain a transaction history as a list of strings).
7. `display(self)` — Print account details.

Requirements:
- Every deposit, withdrawal, and transfer should add an entry to a transaction history list.
- The `transfer` method should update both accounts.
- Validate all amounts (must be positive numbers).
- Create at least 3 accounts and demonstrate all methods.

## Expected Output

```
=== Amina's Account ===
Owner: Amina | Account: ACC001 | Type: savings | Balance: 50,000.00

Deposited 10,000.00. New balance: 60,000.00
Withdrew 5,000.00. New balance: 55,000.00
Transferred 15,000.00 to Musa. New balance: 40,000.00

=== Transaction History (Amina) ===
  1. DEPOSIT: +10,000.00 | Balance: 60,000.00
  2. WITHDRAWAL: -5,000.00 | Balance: 55,000.00
  3. TRANSFER OUT: -15,000.00 to ACC002 | Balance: 40,000.00

=== Musa's Account ===
Owner: Musa | Account: ACC002 | Type: current | Balance: 45,000.00
```

## Assessment

1. What is `self` and why does every method need it as the first parameter?
2. How does Python translate `account.deposit(500)` internally?
3. What is the difference between an attribute and a method?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-04/day-033/`

Include your `bank_system.py` file.

## Additional Resources

- [Lecture 03 — Attributes, Methods & self](../../../python-oop/lectures/03-attributes-methods-and-self.md)
- [Exercise 02 — Attributes and Methods](../../../python-oop/exercises/02-attributes-and-methods/)
- [Python Docs: Instance Objects](https://docs.python.org/3/tutorial/classes.html#instance-objects)

## Reflection

- How does bundling data and behavior into an object change the way you think about program design?
- Why is it important that each object maintains its own independent state?
