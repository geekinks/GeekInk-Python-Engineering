# Day 039: Composition and SOLID Principles

## Learning Objectives

- Understand composition as an alternative to inheritance for building complex objects.
- Know the difference between "HAS-A" (composition) and "IS-A" (inheritance) relationships.
- Apply the "favor composition over inheritance" principle.
- Learn the five SOLID principles and recognize their practical value.
- Refactor inheritance-heavy designs to use composition where appropriate.

## Introduction

Inheritance models "is-a" relationships: a Manager is an Employee. Composition models "has-a" relationships: a Car has an Engine, a Student has an Address, a Course has a list of Students. Many real-world relationships are "has-a," not "is-a," and forcing them into an inheritance hierarchy leads to fragile, inflexible designs.

The SOLID principles are five guidelines for designing maintainable, extensible object-oriented systems. They were formulated by Robert C. Martin and are widely used in professional software engineering. Today you will learn both composition and SOLID as complementary tools for better system design.

**Reference:** [Lecture 09 — Composition, Association, Aggregation](../../../python-oop/lectures/09-composition-association-aggregation.md) | [Lecture 10 — Class & Static Methods](../../../python-oop/lectures/10-class-static-methods.md) | [Lecture 11 — OOP Design Principles (SOLID)](../../../python-oop/lectures/11-oop-design-principles.md)
**Exercises:** [Exercise 09 — Composition](../../../python-oop/exercises/09-composition/) | [Exercise 10 — OOP Design](../../../python-oop/exercises/10-oop-design/)

## Concepts

### Composition

Composition means a class contains instances of other classes as attributes.

```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine ({self.horsepower}hp) started")

class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine    # Car HAS-A Engine

    def start(self):
        print(f"Starting {self.make} {self.model}...")
        self.engine.start()
```

### Composition vs Inheritance

| Aspect | Inheritance (IS-A) | Composition (HAS-A) |
|--------|-------------------|---------------------|
| Relationship | Dog is an Animal | Car has an Engine |
| Coupling | Tight — child depends on parent | Loose — components are independent |
| Flexibility | Fixed at definition time | Can swap components at runtime |
| When to use | True specialization | Combining capabilities |

### The SOLID Principles

**S — Single Responsibility Principle (SRP)**
A class should have only one reason to change. Each class does one thing well.

**O — Open/Closed Principle (OCP)**
Classes should be open for extension but closed for modification. Add new behavior through new classes, not by changing existing ones.

**L — Liskov Substitution Principle (LSP)**
Objects of a child class should be usable wherever objects of the parent class are expected, without breaking the program.

**I — Interface Segregation Principle (ISP)**
No class should be forced to implement methods it does not use. Prefer small, focused interfaces.

**D — Dependency Inversion Principle (DIP)**
High-level modules should not depend on low-level modules. Both should depend on abstractions.

## Practical Examples

```python
# Composition example: School system
class Address:
    def __init__(self, street, city, state):
        self.street = street
        self.city = city
        self.state = state

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}"


class ContactInfo:
    def __init__(self, email, phone):
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"{self.email} | {self.phone}"


class Student:
    def __init__(self, name, student_id, address, contact):
        self.name = name
        self.student_id = student_id
        self.address = address        # HAS-A Address
        self.contact = contact        # HAS-A ContactInfo
        self.courses = []             # HAS many Courses

    def enroll(self, course):
        self.courses.append(course)

    def display(self):
        print(f"Student: {self.name} (ID: {self.student_id})")
        print(f"  Address: {self.address}")
        print(f"  Contact: {self.contact}")
        print(f"  Courses: {', '.join(c.name for c in self.courses)}")


class Course:
    def __init__(self, code, name, credits):
        self.code = code
        self.name = name
        self.credits = credits
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        student.enroll(self)

    def display(self):
        print(f"Course: {self.code} — {self.name} ({self.credits} credits)")
        print(f"  Enrolled: {len(self.students)} students")


# Using composition
addr = Address("15 Maitama Crescent", "Kano", "Kano State")
contact = ContactInfo("amina@example.com", "08012345678")
amina = Student("Amina Bello", "STU001", addr, contact)

python_course = Course("CS101", "Python Engineering", 4)
data_course = Course("DS201", "Data Science", 3)

python_course.add_student(amina)
data_course.add_student(amina)

amina.display()
print()
python_course.display()
```

```python
# SRP violation and fix
# BAD: One class does everything
class StudentManager:
    def add_student(self, name): pass
    def remove_student(self, id): pass
    def calculate_gpa(self, id): pass
    def generate_report(self, id): pass
    def send_email(self, id, msg): pass
    def save_to_database(self, student): pass

# GOOD: Separate responsibilities
class StudentRepository:
    def add(self, student): pass
    def remove(self, student_id): pass
    def find(self, student_id): pass

class GradeCalculator:
    def calculate_gpa(self, grades): pass

class ReportGenerator:
    def generate(self, student): pass

class NotificationService:
    def send_email(self, recipient, message): pass
```

## Guided Practice

Refactor an inheritance-heavy design to use composition.

**Before (overusing inheritance):**

```python
class FlyingSwimmingAnimal(FlyingAnimal, SwimmingAnimal):
    pass  # Diamond problem, tightly coupled
```

**After (composition):**

```python
class FlyAbility:
    def fly(self):
        print("Flying through the air!")

class SwimAbility:
    def swim(self):
        print("Swimming in water!")

class RunAbility:
    def run(self):
        print("Running on land!")


class Duck:
    def __init__(self, name):
        self.name = name
        self.fly_ability = FlyAbility()
        self.swim_ability = SwimAbility()
        self.run_ability = RunAbility()

    def fly(self):
        print(f"{self.name}: ", end="")
        self.fly_ability.fly()

    def swim(self):
        print(f"{self.name}: ", end="")
        self.swim_ability.swim()


class Penguin:
    def __init__(self, name):
        self.name = name
        self.swim_ability = SwimAbility()
        self.run_ability = RunAbility()
        # No fly_ability — penguins don't fly!

    def swim(self):
        print(f"{self.name}: ", end="")
        self.swim_ability.swim()


donald = Duck("Donald")
donald.fly()
donald.swim()

tux = Penguin("Tux")
tux.swim()
```

## Daily Challenge

Create a file called `composition_refactor.py`.

You are given this inheritance-heavy design:

```python
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity
        self.charge_level = 100

    def charge(self, percent):
        self.charge_level = min(100, self.charge_level + percent)

class GPSVehicle(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.location = (0, 0)

    def navigate(self, destination):
        self.location = destination

class ElectricGPSVehicle(ElectricVehicle, GPSVehicle):
    # Diamond inheritance problem!
    pass
```

Refactor this using composition:

1. Create separate component classes: `Engine` (with `engine_type`: "petrol", "diesel", or "electric"), `Battery` (with `capacity` and `charge_level`), `GPS` (with `location` and `navigate` method).

2. Create a single `Vehicle` class that composes these components:
   - All vehicles have an `Engine`.
   - Electric vehicles additionally have a `Battery`.
   - GPS-equipped vehicles additionally have a `GPS`.
   - Components are passed into the constructor.

3. Add a `display()` method that shows the vehicle's details and the status of each component.

4. Demonstrate by creating:
   - A petrol vehicle with GPS.
   - An electric vehicle with battery and GPS.
   - A diesel vehicle with no GPS.

5. Apply at least one SOLID principle visibly in your design and explain which one in a comment.

## Expected Output

```
=== Vehicle Fleet ===

Toyota Corolla (2023)
  Engine: petrol
  GPS: Enabled (Location: 0, 0)

Tesla Model 3 (2024)
  Engine: electric
  Battery: 85 kWh | Charge: 100%
  GPS: Enabled (Location: 0, 0)

Navigating Tesla to (9.05, 7.49)...
  GPS Location: (9.05, 7.49)

Charging Tesla...
  Battery: 100%

Ford Ranger (2022)
  Engine: diesel
  GPS: Not equipped
```

## Assessment

1. What is the difference between composition and inheritance? Give an example of each.
2. Explain the Single Responsibility Principle in your own words. Why does it matter?
3. When should you prefer composition over inheritance?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-04/day-039/`

Include your `composition_refactor.py` file.

## Additional Resources

- [Lecture 09 — Composition, Association, Aggregation](../../../python-oop/lectures/09-composition-association-aggregation.md)
- [Lecture 11 — OOP Design Principles (SOLID)](../../../python-oop/lectures/11-oop-design-principles.md)
- [Exercise 09 — Composition](../../../python-oop/exercises/09-composition/)
- [Exercise 10 — OOP Design](../../../python-oop/exercises/10-oop-design/)

## Reflection

- Look at a class you built earlier in this module. Does it have multiple responsibilities that could be separated?
- How does the "favor composition over inheritance" principle change your approach to designing classes?
