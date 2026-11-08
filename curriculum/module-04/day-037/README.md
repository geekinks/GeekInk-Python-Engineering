# Day 037: Polymorphism

## Learning Objectives

- Understand polymorphism as the ability to treat different types through a common interface.
- Implement method overriding to give different classes the same method with different behavior.
- Use polymorphic collections to process objects of different types uniformly.
- Understand duck typing: "If it walks like a duck and quacks like a duck, it is a duck."
- Apply polymorphism to write flexible, extensible code.

## Introduction

Polymorphism means "many forms." In OOP, it means that objects of different classes can be used through the same interface. If every shape has an `area()` method, you can calculate the total area of a list containing circles, rectangles, and triangles without knowing or caring which specific shape each one is.

This is powerful because it lets you write code that works with any object that follows a common protocol, without checking types. When you add a new shape, the existing code that loops through shapes and calls `area()` does not need to change at all. Polymorphism is what makes OOP systems extensible — you can add new behavior without modifying existing code.

**Reference:** [Lecture 07 — Polymorphism & Duck Typing](../../../python-oop/lectures/07-polymorphism.md)
**Exercise:** [Exercise 07 — Polymorphism](../../../python-oop/exercises/07-polymorphism/)

## Concepts

### Method Overriding

When a child class defines a method with the same name as one in its parent, the child's version is used.

### Polymorphic Collections

You can store objects of different classes in the same list and call the same method on each one:

```python
shapes = [circle, rectangle, triangle]
for shape in shapes:
    print(shape.area())
```

### Duck Typing

Python does not require objects to share a parent class to be used polymorphically. If an object has the right method, it works:

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Robot:
    def speak(self):
        return "Beep boop!"

for thing in [Dog(), Cat(), Robot()]:
    print(thing.speak())
```

`Robot` is not an `Animal`, but it has a `speak()` method, so it works in the same loop.

## Practical Examples

```python
import math

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter()")

    def display(self):
        print(f"{self.name}: area = {self.area():.2f}, perimeter = {self.perimeter():.2f}")


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, base, height, side_a, side_b, side_c):
        super().__init__("Triangle")
        self.base = base
        self.height = height
        self.sides = (side_a, side_b, side_c)

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return sum(self.sides)


# Polymorphic processing
shapes = [
    Circle(5),
    Rectangle(10, 4),
    Triangle(6, 8, 6, 8, 10),
    Circle(3),
    Rectangle(7, 7),
]

print("=== Shape Report ===")
for shape in shapes:
    shape.display()

total_area = sum(shape.area() for shape in shapes)
print(f"\nTotal area: {total_area:.2f}")
```

```python
# Duck typing example — no inheritance required
class PDFExporter:
    def export(self, data):
        print(f"Exporting {len(data)} records to PDF...")

class CSVExporter:
    def export(self, data):
        print(f"Exporting {len(data)} records to CSV...")

class JSONExporter:
    def export(self, data):
        print(f"Exporting {len(data)} records to JSON...")


def run_export(exporter, data):
    exporter.export(data)


records = [{"name": "Amina"}, {"name": "Musa"}]

for exp in [PDFExporter(), CSVExporter(), JSONExporter()]:
    run_export(exp, records)
```

## Guided Practice

Build a polymorphic payment system.

```python
class Payment:
    def __init__(self, amount):
        self.amount = amount

    def process(self):
        raise NotImplementedError

    def receipt(self):
        raise NotImplementedError


class CashPayment(Payment):
    def process(self):
        print(f"Processing cash payment of {self.amount:,.2f}")
        return True

    def receipt(self):
        return f"CASH RECEIPT: {self.amount:,.2f}"


class CardPayment(Payment):
    def __init__(self, amount, card_last_four):
        super().__init__(amount)
        self.card_last_four = card_last_four

    def process(self):
        print(f"Charging card ending {self.card_last_four}: {self.amount:,.2f}")
        return True

    def receipt(self):
        return f"CARD RECEIPT: {self.amount:,.2f} (Card: ****{self.card_last_four})"


class MobilePayment(Payment):
    def __init__(self, amount, phone_number):
        super().__init__(amount)
        self.phone_number = phone_number

    def process(self):
        print(f"Mobile payment from {self.phone_number}: {self.amount:,.2f}")
        return True

    def receipt(self):
        return f"MOBILE RECEIPT: {self.amount:,.2f} (Phone: {self.phone_number})"


# Polymorphic processing
payments = [
    CashPayment(5000),
    CardPayment(15000, "4321"),
    MobilePayment(3000, "08012345678"),
]

total = 0
for payment in payments:
    if payment.process():
        total += payment.amount
        print(f"  {payment.receipt()}")

print(f"\nTotal collected: {total:,.2f}")
```

## Daily Challenge

Create a file called `shape_calculator.py` with a polymorphic shape calculation system:

1. Define a base `Shape` class with:
   - `area()` method (raises NotImplementedError)
   - `perimeter()` method (raises NotImplementedError)
   - `describe()` method that returns a string like `"Circle with radius 5"`

2. Implement these shapes:
   - `Circle(radius)` — area = pi * r^2, perimeter = 2 * pi * r
   - `Rectangle(width, height)` — area = w * h, perimeter = 2(w + h)
   - `Square(side)` — inherits from Rectangle. Constructor calls `super().__init__(side, side)`.
   - `Triangle(side_a, side_b, side_c)` — area using Heron's formula, perimeter = sum of sides.

3. Create a function `shape_report(shapes)` that accepts a list of shapes and prints:
   - Each shape's description, area, and perimeter.
   - The shape with the largest area.
   - The shape with the largest perimeter.
   - Total combined area.

4. Create at least 6 shapes of different types and pass them to `shape_report()`.

Heron's formula: `area = sqrt(s * (s-a) * (s-b) * (s-c))` where `s = (a+b+c)/2`.

## Expected Output

```
=== Shape Report ===
Circle with radius 5.0: area = 78.54, perimeter = 31.42
Rectangle 10x4: area = 40.00, perimeter = 28.00
Square 6x6: area = 36.00, perimeter = 24.00
Triangle (3, 4, 5): area = 6.00, perimeter = 12.00
Circle with radius 3.0: area = 28.27, perimeter = 18.85
Rectangle 8x6: area = 48.00, perimeter = 28.00

Largest area: Circle with radius 5.0 (78.54)
Largest perimeter: Circle with radius 5.0 (31.42)
Total area: 236.81
```

## Assessment

1. What is polymorphism and how does it make code more extensible?
2. Explain duck typing with your own example.
3. Why is it useful that a `Square` inherits from `Rectangle` but does not need its own `area()` method?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-04/day-037/`

Include your `shape_calculator.py` file.

## Additional Resources

- [Lecture 07 — Polymorphism & Duck Typing](../../../python-oop/lectures/07-polymorphism.md)
- [Exercise 07 — Polymorphism](../../../python-oop/exercises/07-polymorphism/)
- [Python Docs: Classes](https://docs.python.org/3/tutorial/classes.html)

## Reflection

- How does polymorphism reduce the amount of conditional logic (if/elif/else) in your code?
- Think of a real-world system where different types of items are processed the same way (payments, deliveries, notifications). How would polymorphism apply?
