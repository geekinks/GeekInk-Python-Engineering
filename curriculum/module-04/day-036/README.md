# Day 036: Inheritance

## Learning Objectives

- Understand inheritance as a mechanism for code reuse and specialization.
- Create derived (child) classes that inherit from base (parent) classes.
- Use `super()` to call parent class methods.
- Override methods to specialize behavior in child classes.
- Use `isinstance()` and `issubclass()` to check relationships.

## Introduction

Inheritance lets you create a new class based on an existing one. The new class (child) inherits all the attributes and methods of the existing class (parent) and can add new ones or override existing ones. This models "is-a" relationships: a Manager is an Employee, a Dog is an Animal, a SavingsAccount is a BankAccount.

Inheritance eliminates duplication. Instead of copying the same code into every related class, you write it once in a base class and let the children inherit it. Each child can then specialize — adding unique behavior or modifying inherited behavior. This is one of the most powerful features of OOP, but it must be used carefully. Tomorrow and the day after, you will learn about polymorphism and abstraction, which build on inheritance.

**Reference:** [Lecture 06 — Inheritance & super()](../../../python-oop/lectures/06-inheritance.md)
**Exercise:** [Exercise 06 — Inheritance](../../../python-oop/exercises/06-inheritance/)

## Concepts

### Basic Inheritance

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows"
```

`Dog` and `Cat` inherit `__init__` from `Animal` but override `speak`.

### `super()` — Calling the Parent

`super()` lets you call the parent class's methods, typically used in `__init__` to ensure the parent sets up its part of the object.

```python
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department
```

### Method Overriding

A child class can redefine a method from the parent. When you call the method on a child object, the child's version runs.

### Checking Relationships

```python
m = Manager("Amina", "MGR001", "Engineering")
print(isinstance(m, Manager))    # True
print(isinstance(m, Employee))   # True
print(issubclass(Manager, Employee))  # True
```

## Practical Examples

```python
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display(self):
        print(f"{self.name} (ID: {self.employee_id}) — Salary: {self.salary:,.2f}")

    def annual_salary(self):
        return self.salary * 12


class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department
        self.team = []

    def add_to_team(self, employee):
        self.team.append(employee)

    def display(self):
        super().display()
        print(f"  Department: {self.department} | Team size: {len(self.team)}")


class Intern(Employee):
    def __init__(self, name, employee_id, salary, university):
        super().__init__(name, employee_id, salary)
        self.university = university
        self.mentor = None

    def assign_mentor(self, mentor):
        self.mentor = mentor

    def display(self):
        super().display()
        mentor_name = self.mentor.name if self.mentor else "Not assigned"
        print(f"  University: {self.university} | Mentor: {mentor_name}")


# Creating objects
mgr = Manager("Amina", "MGR001", 150000, "Engineering")
emp = Employee("Musa", "EMP001", 80000)
intern1 = Intern("Fatima", "INT001", 30000, "BUK")

mgr.add_to_team(emp)
mgr.add_to_team(intern1)
intern1.assign_mentor(mgr)

# Displaying
mgr.display()
emp.display()
intern1.display()

# Type checking
print(f"\nAmina is Employee: {isinstance(mgr, Employee)}")
print(f"Amina is Manager: {isinstance(mgr, Manager)}")
print(f"Manager is subclass of Employee: {issubclass(Manager, Employee)}")
print(f"Annual salary (Amina): {mgr.annual_salary():,.2f}")
```

```python
# Inheriting and extending — BankAccount hierarchy
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    @property
    def balance(self):
        return self._balance

    def display(self):
        print(f"{self.owner} | Balance: {self._balance:,.2f}")


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        return interest

    def display(self):
        super().display()
        print(f"  Type: Savings | Interest Rate: {self.interest_rate:.1%}")


class CurrentAccount(BankAccount):
    def __init__(self, owner, balance=0, overdraft_limit=10000):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self._balance + self.overdraft_limit:
            raise ValueError("Exceeds overdraft limit")
        self._balance -= amount

    def display(self):
        super().display()
        print(f"  Type: Current | Overdraft Limit: {self.overdraft_limit:,.2f}")


savings = SavingsAccount("Amina", 100000, 0.06)
current = CurrentAccount("Musa", 50000, 20000)

savings.display()
print(f"Interest earned: {savings.apply_interest():,.2f}")
savings.display()

print()
current.display()
current.withdraw(60000)  # Uses overdraft
current.display()
```

## Guided Practice

Build an employee hierarchy step by step.

**Step 1:** Create the base `Employee` class.
**Step 2:** Create `Manager` that adds department and team management.
**Step 3:** Create `Intern` that adds university and mentor tracking.
**Step 4:** Create instances, build a team, and display everyone.
**Step 5:** Process all employees in a list using polymorphism (each one has `display()`).

```python
employees = [mgr, emp, intern1]
print("=== All Employees ===")
for e in employees:
    e.display()
    print()
```

## Daily Challenge

Create a file called `employee_hierarchy.py` with the following class hierarchy:

**Base class:** `Employee`
- Constructor: `name`, `employee_id`, `base_salary`
- Methods: `calculate_pay()` (returns base_salary), `display()`, `annual_pay()` (12 * calculate_pay())

**Child class:** `Manager(Employee)`
- Additional: `department`, `bonus_percent` (default 15)
- Override `calculate_pay()` to include bonus: `base_salary * (1 + bonus_percent/100)`
- Method: `add_report(employee)`, `display()` (includes department and number of reports)

**Child class:** `Developer(Employee)`
- Additional: `programming_languages` (list), `level` ("junior", "mid", "senior")
- Override `calculate_pay()`: add 10% for mid, 25% for senior
- Method: `add_language(lang)`, `display()` (includes level and languages)

**Child class:** `Intern(Employee)`
- Additional: `university`, `duration_months`
- Override `calculate_pay()`: return base_salary (no modifications)
- Method: `display()` (includes university and duration)

Demonstrate:
1. Create at least one of each type.
2. A Manager has a Developer and Intern reporting to them.
3. Print all employees with their calculated pay.
4. Show that isinstance checks work correctly.

## Expected Output

```
=== Employee Report ===

Amina Bello (MGR001) — Manager
  Department: Engineering | Reports: 2
  Monthly Pay: 172,500.00

Musa Ibrahim (DEV001) — Developer
  Level: senior | Languages: Python, JavaScript, Go
  Monthly Pay: 125,000.00

Fatima Yusuf (INT001) — Intern
  University: BUK | Duration: 6 months
  Monthly Pay: 30,000.00

Type checks:
  Amina is Employee: True
  Amina is Manager: True
  Musa is Manager: False
```

## Assessment

1. What does `super().__init__()` do and why is it necessary?
2. What happens if a child class does not override a parent method?
3. Explain the "is-a" relationship with an example from your challenge.

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-04/day-036/`

Include your `employee_hierarchy.py` file.

## Additional Resources

- [Lecture 06 — Inheritance & super()](../../../python-oop/lectures/06-inheritance.md)
- [Exercise 06 — Inheritance](../../../python-oop/exercises/06-inheritance/)
- [Python Docs: Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)

## Reflection

- When should you use inheritance vs just adding attributes to a single class?
- What are the risks of creating very deep inheritance chains (class A -> B -> C -> D -> E)?
