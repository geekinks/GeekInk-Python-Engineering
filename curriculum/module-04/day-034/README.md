# Day 034: Constructors and Properties

## Learning Objectives

- Use `__init__` to initialize objects with required data at creation time.
- Set default values for optional parameters in constructors.
- Use `@property` to create computed or controlled attribute access.
- Use `@setter` to validate data before it is stored.
- Understand why constructors are better than manual attribute assignment.

## Introduction

In the previous lessons, you created objects and then called a separate `set_up` method to give them their data. This is error-prone — you could forget to call `set_up` and try to use an object that has no attributes. The constructor (`__init__`) solves this by running automatically when you create an object. It guarantees that every object starts with all the data it needs.

Properties take control a step further. Instead of letting code directly set `student.age = -5`, you define a property with a setter that validates the data. From the outside, it looks like a regular attribute assignment, but behind the scenes, your validation code runs. This pattern protects your objects from invalid state.

**Reference:** [Lecture 04 — Constructors & Properties](../../../python-oop/lectures/04-constructors-and-properties.md)
**Exercises:** [Exercise 03 — Constructors and self](../../../python-oop/exercises/03-constructors-and-self/) | [Exercise 04 — Properties](../../../python-oop/exercises/04-properties/)

## Concepts

### The `__init__` Constructor

`__init__` is a special method that Python calls automatically when a new object is created.

```python
class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
```

Now you must provide the data when creating the object:

```python
s = Student("Amina", 20, "STU001")
```

### Default Parameter Values

```python
class Student:
    def __init__(self, name, age, student_id, department="General"):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.department = department

s1 = Student("Amina", 20, "STU001")               # department = "General"
s2 = Student("Musa", 22, "STU002", "Engineering")  # department = "Engineering"
```

### Properties with `@property`

A property looks like an attribute from the outside but runs a method inside.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14159 * self.radius ** 2

c = Circle(5)
print(c.area)    # 78.53975 — accessed like an attribute, but computed
```

### Setters with `@attribute.setter`

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age     # This calls the setter below

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0 or value > 150:
            raise ValueError(f"Invalid age: {value}")
        self._age = value
```

## Practical Examples

```python
class Product:
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price       # calls the setter
        self.quantity = quantity  # calls the setter

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Quantity cannot be negative")
        self._quantity = value

    @property
    def total_value(self):
        return self.price * self.quantity

    def display(self):
        print(f"{self.name} | Price: {self.price:,.2f} | Qty: {self.quantity} | Value: {self.total_value:,.2f}")


# Creating products with constructor
laptop = Product("Laptop", 450000, 5)
laptop.display()

phone = Product("Phone", 180000, 12)
phone.display()

# Computed property
print(f"Total inventory value: {laptop.total_value + phone.total_value:,.2f}")

# Validation in action
try:
    bad = Product("Bad Item", -100)
except ValueError as e:
    print(f"Caught: {e}")

# Updating through setter
laptop.quantity = 8
laptop.display()
```

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return (self.celsius * 9 / 5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9

    def display(self):
        print(f"{self.celsius:.1f}C = {self.fahrenheit:.1f}F")


t = Temperature(100)
t.display()           # 100.0C = 212.0F

t.fahrenheit = 72
t.display()           # 22.2C = 72.0F
```

## Guided Practice

Build a validated `Product` class step by step.

**Step 1:** Start with a basic constructor.

```python
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self._price = price
        self._quantity = quantity
```

**Step 2:** Add a `@property` for price with validation.

```python
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number")
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = round(value, 2)
```

**Step 3:** Update `__init__` to use the setter.

```python
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price        # uses the setter for validation
        self.quantity = quantity
```

**Step 4:** Add a computed property and test it.

```python
    @property
    def total_value(self):
        return self.price * self.quantity

p = Product("Notebook", 500, 10)
print(f"Total: {p.total_value}")   # 5000
```

## Daily Challenge

Create a file called `product_catalog.py` with a `Product` class:

**Constructor parameters:**
- `name` (required, string)
- `price` (required, must be positive)
- `quantity` (required, must be non-negative integer)
- `category` (optional, default `"General"`)

**Properties with validation:**
- `price` — Must be a positive number. Round to 2 decimal places.
- `quantity` — Must be a non-negative integer.

**Computed properties:**
- `total_value` — Returns `price * quantity`.
- `in_stock` — Returns `True` if quantity > 0.

**Methods:**
- `apply_discount(percent)` — Reduces the price by the given percentage. Percent must be between 0 and 100.
- `restock(amount)` — Adds to the quantity.
- `sell(amount)` — Reduces quantity. Raises `ValueError` if not enough stock.
- `display()` — Prints formatted product information.

Demonstrate the class by:
1. Creating at least 3 products.
2. Applying discounts to one.
3. Selling some quantity of another.
4. Restocking a third.
5. Printing all products.
6. Attempting invalid operations (negative price, selling more than in stock) and catching the errors.

## Expected Output

```
=== Product Catalog ===
Laptop | Price: 450,000.00 | Qty: 5 | Value: 2,250,000.00 | In Stock: Yes
Phone  | Price: 180,000.00 | Qty: 0 | Value: 0.00 | In Stock: No
Book   | Price: 2,500.00   | Qty: 50 | Value: 125,000.00 | In Stock: Yes

Applying 10% discount to Laptop...
Laptop | Price: 405,000.00 | Qty: 5 | Value: 2,025,000.00

Selling 3 Laptops...
Laptop | Price: 405,000.00 | Qty: 2 | Value: 810,000.00

Attempting to sell 10 Books...
Error: Not enough stock. Available: 50, Requested: 60
```

## Assessment

1. Why is `__init__` better than manually setting attributes after creating an object?
2. What is the difference between a regular attribute and a `@property`?
3. How does a `@setter` help protect an object from invalid data?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-04/day-034/`

Include your `product_catalog.py` file.

## Additional Resources

- [Lecture 04 — Constructors & Properties](../../../python-oop/lectures/04-constructors-and-properties.md)
- [Exercise 03 — Constructors and self](../../../python-oop/exercises/03-constructors-and-self/)
- [Exercise 04 — Properties](../../../python-oop/exercises/04-properties/)
- [Python Docs: property()](https://docs.python.org/3/library/functions.html#property)

## Reflection

- How does using properties change the way external code interacts with your objects?
- In what situations would validation in a setter prevent real bugs in a larger application?
