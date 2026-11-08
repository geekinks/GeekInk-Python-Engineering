# Day 035: Encapsulation

## Learning Objectives

- Understand encapsulation as the practice of hiding internal state and requiring controlled access.
- Use protected attributes (single underscore `_`) and private attributes (double underscore `__`).
- Understand Python's name mangling mechanism for private attributes.
- Recognize why encapsulation protects object invariants.
- Refactor classes to properly encapsulate their data.

## Introduction

Encapsulation is one of the four pillars of OOP. It means bundling data with the methods that operate on it and restricting direct access to the internal details. When you make an attribute private, you force all access to go through methods or properties that you control. This lets you enforce rules — a bank balance can never be negative, a student's grade must be between 0 and 100, a temperature must be above absolute zero.

Without encapsulation, any code anywhere in your program can reach into an object and change its data to something invalid. With encapsulation, the object protects itself. Professional codebases rely heavily on this principle because it makes software predictable and maintainable.

**Reference:** [Lecture 05 — Encapsulation](../../../python-oop/lectures/05-encapsulation.md)
**Exercise:** [Exercise 05 — Encapsulation](../../../python-oop/exercises/05-encapsulation/)

## Concepts

### Access Levels in Python

Python does not have strict access control like Java or C++. It uses naming conventions:

| Convention | Meaning | Enforcement |
|-----------|---------|-------------|
| `name` | Public — accessible from anywhere | None |
| `_name` | Protected — intended for internal use only | Convention only (no enforcement) |
| `__name` | Private — name mangling makes direct access harder | Name mangling (`_ClassName__name`) |

### Protected Attributes (`_`)

A single underscore signals "this attribute is for internal use." Other code can still access it, but the underscore warns developers not to.

```python
class Account:
    def __init__(self, balance):
        self._balance = balance   # protected by convention
```

### Private Attributes (`__`)

Double underscore triggers name mangling. Python renames `__balance` to `_Account__balance` internally, making accidental access from outside the class much harder.

```python
class Account:
    def __init__(self, balance):
        self.__balance = balance  # name-mangled

acc = Account(1000)
# acc.__balance          # AttributeError
# acc._Account__balance  # works, but defeats the purpose
```

### Protecting Invariants

An invariant is a condition that must always be true. "Balance is never negative" is an invariant. Encapsulation lets you enforce it:

```python
class Account:
    def __init__(self, balance):
        self.__balance = balance

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
```

## Practical Examples

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance
        self.__transactions = []

    @property
    def owner(self):
        return self.__owner

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        self.__transactions.append(f"DEPOSIT: +{amount:,.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        self.__transactions.append(f"WITHDRAWAL: -{amount:,.2f}")

    def get_statement(self):
        return list(self.__transactions)

    def display(self):
        print(f"Account: {self.__owner} | Balance: {self.__balance:,.2f}")


acc = BankAccount("Amina", 50000)
acc.deposit(10000)
acc.withdraw(5000)
acc.display()

# The balance is protected:
# acc.__balance = -99999  # This does NOT modify the real balance
# It creates a new attribute called __balance on the instance

# The real balance is safe:
acc.display()  # Still shows the correct balance

# Attempting invalid operations:
try:
    acc.withdraw(100000)
except ValueError as e:
    print(f"Error: {e}")

try:
    acc.deposit(-500)
except ValueError as e:
    print(f"Error: {e}")
```

```python
class Student:
    def __init__(self, name, student_id):
        self._name = name
        self._student_id = student_id
        self.__grades = {}

    @property
    def name(self):
        return self._name

    def add_grade(self, subject, score):
        if not 0 <= score <= 100:
            raise ValueError(f"Score must be 0-100, got {score}")
        self.__grades[subject] = score

    def get_grade(self, subject):
        return self.__grades.get(subject, None)

    def average(self):
        if not self.__grades:
            return 0
        return sum(self.__grades.values()) / len(self.__grades)

    def display(self):
        print(f"\nStudent: {self._name} (ID: {self._student_id})")
        for subject, score in self.__grades.items():
            print(f"  {subject}: {score}")
        print(f"  Average: {self.average():.1f}")


s = Student("Musa", "STU001")
s.add_grade("Math", 85)
s.add_grade("English", 90)
s.display()

try:
    s.add_grade("Science", 150)
except ValueError as e:
    print(f"Error: {e}")
```

## Guided Practice

Refactor a class that has no encapsulation.

**Before (no encapsulation):**

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e = Employee("Amina", 50000)
e.salary = -1000   # No protection!
print(e.salary)     # -1000
```

**After (encapsulated):**

```python
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.salary = salary   # uses the setter

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self.__salary = value

    def give_raise(self, percent):
        if percent < 0:
            raise ValueError("Raise percent cannot be negative")
        self.__salary += self.__salary * (percent / 100)

    def display(self):
        print(f"{self.__name} | Salary: {self.__salary:,.2f}")


e = Employee("Amina", 50000)
e.display()

e.give_raise(10)
e.display()

try:
    e.salary = -1000
except ValueError as e_msg:
    print(f"Blocked: {e_msg}")
```

## Daily Challenge

You are given this class with NO encapsulation:

```python
class StudentRecord:
    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores
        self.passed = False

    def calculate_average(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0

    def check_pass(self, threshold=50):
        self.passed = self.calculate_average() >= threshold
        return self.passed
```

Problems:
- Anyone can set `age` to -5 or `scores` to contain 999.
- Anyone can directly set `passed = True` without actually passing.
- The `scores` list can be modified directly, bypassing validation.

**Your task:** Create a file called `encapsulated_student.py` that refactors this class with proper encapsulation:

1. Make `name` a read-only property (set once in constructor, cannot be changed).
2. Make `age` a property with a setter that validates it is between 5 and 100.
3. Make `scores` private. Provide an `add_score(subject, score)` method that validates scores are 0-100. Store as a dict mapping subject to score.
4. Make `passed` a read-only computed property based on whether the average is >= 50.
5. Add a `remove_score(subject)` method.
6. Add a `display_report()` method.

Demonstrate that:
- Setting age to -5 raises an error.
- Adding a score of 150 raises an error.
- `passed` cannot be set directly.
- Valid operations work correctly.

## Expected Output

```
Student: Amina Bello | Age: 20
  Math: 85
  English: 92
  Science: 78
  Average: 85.0
  Status: PASSED

Attempting invalid operations:
  Setting age to -5: Error — Age must be between 5 and 100
  Adding score 150: Error — Score must be between 0 and 100
  Setting passed directly: Error — can't set attribute
```

## Assessment

1. What is the difference between protected (`_`) and private (`__`) attributes in Python?
2. What is name mangling and why does Python use it?
3. Give an example of an invariant in a real-world system and how encapsulation would protect it.

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-04/day-035/`

Include your `encapsulated_student.py` file.

## Additional Resources

- [Lecture 05 — Encapsulation](../../../python-oop/lectures/05-encapsulation.md)
- [Exercise 05 — Encapsulation](../../../python-oop/exercises/05-encapsulation/)
- [Python Docs: Private Variables](https://docs.python.org/3/tutorial/classes.html#private-variables)

## Reflection

- Why is it better to provide controlled methods like `add_score()` rather than allowing direct access to the scores list?
- Can you think of a real-world analogy for encapsulation? (Hint: think about how ATMs work versus having direct access to a bank vault.)
