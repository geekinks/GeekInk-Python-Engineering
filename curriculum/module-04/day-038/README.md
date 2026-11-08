# Day 038: Abstraction

## Learning Objectives

- Understand abstraction as hiding implementation details behind a clean interface.
- Use Python's `abc` module to create abstract base classes.
- Define abstract methods with `@abstractmethod`.
- Understand why abstract classes cannot be instantiated.
- Design contracts that enforce consistency across implementations.

## Introduction

Abstraction is the final pillar of OOP. It means defining what an object should do without specifying how. An abstract class is like a contract — it declares the methods that every subclass must implement but leaves the implementation to each subclass. You cannot create an instance of an abstract class directly; it exists only to be inherited from.

This is essential for large systems. When you define an abstract `PaymentProcessor` with an `authorize()` method, every payment implementation — Stripe, PayPal, bank transfer — must implement that method. If a developer forgets, Python raises an error immediately instead of failing silently at runtime. Abstraction forces consistency and catches mistakes early.

**Reference:** [Lecture 08 — Abstraction & ABCs](../../../python-oop/lectures/08-abstraction.md)
**Exercise:** [Exercise 08 — Abstraction](../../../python-oop/exercises/08-abstraction/)

## Concepts

### Abstract Base Classes (ABC)

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
```

`Shape` cannot be instantiated. Any class inheriting from `Shape` must implement both `area()` and `perimeter()`, or it will also be abstract and non-instantiable.

### Why Abstract Classes?

1. **Contract enforcement** — Subclasses cannot skip required methods.
2. **Design clarity** — The abstract class documents the interface.
3. **Error prevention** — Forgetting a method raises `TypeError` at instantiation, not at runtime.

### Concrete Methods in Abstract Classes

Abstract classes can also contain concrete (implemented) methods that subclasses inherit directly:

```python
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def describe(self):
        return f"{type(self).__name__}: area = {self.area():.2f}"
```

## Practical Examples

```python
from abc import ABC, abstractmethod


class DataExporter(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def export(self, filename):
        """Export data to the specified file."""
        pass

    @abstractmethod
    def validate(self):
        """Validate data before exporting."""
        pass

    def run(self, filename):
        if self.validate():
            self.export(filename)
            print(f"Export complete: {filename}")
        else:
            print("Validation failed. Export aborted.")


class CSVExporter(DataExporter):
    def export(self, filename):
        print(f"Writing {len(self.data)} rows to {filename} as CSV")

    def validate(self):
        return len(self.data) > 0


class JSONExporter(DataExporter):
    def export(self, filename):
        print(f"Serializing {len(self.data)} records to {filename} as JSON")

    def validate(self):
        return all(isinstance(item, dict) for item in self.data)


# Cannot instantiate abstract class:
try:
    exporter = DataExporter([])
except TypeError as e:
    print(f"Error: {e}")

# Concrete classes work:
data = [{"name": "Amina"}, {"name": "Musa"}]
csv_exp = CSVExporter(data)
csv_exp.run("output.csv")

json_exp = JSONExporter(data)
json_exp.run("output.json")
```

```python
from abc import ABC, abstractmethod


class Notification(ABC):
    def __init__(self, recipient, message):
        self.recipient = recipient
        self.message = message

    @abstractmethod
    def send(self):
        pass

    def preview(self):
        print(f"To: {self.recipient}")
        print(f"Message: {self.message}")


class EmailNotification(Notification):
    def __init__(self, recipient, message, subject):
        super().__init__(recipient, message)
        self.subject = subject

    def send(self):
        print(f"Sending email to {self.recipient}: [{self.subject}] {self.message}")


class SMSNotification(Notification):
    def send(self):
        truncated = self.message[:160]
        print(f"Sending SMS to {self.recipient}: {truncated}")


class PushNotification(Notification):
    def __init__(self, recipient, message, app_name):
        super().__init__(recipient, message)
        self.app_name = app_name

    def send(self):
        print(f"Push from {self.app_name} to {self.recipient}: {self.message}")


# Polymorphic processing with guaranteed interface
notifications = [
    EmailNotification("amina@example.com", "Your order shipped!", "Order Update"),
    SMSNotification("08012345678", "Your OTP is 482910"),
    PushNotification("user_123", "New message from Musa", "GeekChat"),
]

for notif in notifications:
    notif.send()
```

## Guided Practice

Design an abstract `PaymentProcessor`.

**Step 1:** Define the abstract class.

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def authorize(self, amount):
        pass

    @abstractmethod
    def capture(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

    def process_payment(self, amount):
        print(f"Processing payment of {amount:,.2f}...")
        if self.authorize(amount):
            self.capture(amount)
            print("Payment successful!")
            return True
        print("Payment failed.")
        return False
```

**Step 2:** Implement concrete processors.

```python
class CashProcessor(PaymentProcessor):
    def __init__(self, cash_on_hand):
        self.cash_on_hand = cash_on_hand

    def authorize(self, amount):
        return amount <= self.cash_on_hand

    def capture(self, amount):
        self.cash_on_hand -= amount
        print(f"  Cash collected: {amount:,.2f}")

    def refund(self, amount):
        self.cash_on_hand += amount
        print(f"  Cash refunded: {amount:,.2f}")


class CardProcessor(PaymentProcessor):
    def __init__(self, card_number, limit):
        self.card_number = card_number
        self.limit = limit
        self.charged = 0

    def authorize(self, amount):
        return (self.charged + amount) <= self.limit

    def capture(self, amount):
        self.charged += amount
        print(f"  Card {self.card_number[-4:]} charged: {amount:,.2f}")

    def refund(self, amount):
        self.charged -= amount
        print(f"  Card {self.card_number[-4:]} refunded: {amount:,.2f}")
```

**Step 3:** Use them through the common interface.

```python
processors = [
    CashProcessor(50000),
    CardProcessor("4111111111111111", 100000),
]

for p in processors:
    p.process_payment(25000)
    print()
```

## Daily Challenge

Create a file called `payment_system.py` with an abstract payment processing system:

1. Define an abstract class `PaymentProcessor(ABC)` with:
   - Abstract methods: `authorize(amount)`, `capture(amount)`, `refund(amount, reason)`
   - Concrete method: `process_payment(amount)` that calls authorize then capture
   - Concrete method: `display_info()` that shows the processor name

2. Implement three concrete processors:
   - `CreditCardProcessor(card_number, expiry, credit_limit)` — Authorizes if within credit limit.
   - `BankTransferProcessor(account_number, bank_name, balance)` — Authorizes if sufficient balance.
   - `MobileMoneyProcessor(phone_number, provider, balance)` — Authorizes if sufficient balance.

3. Each processor must:
   - Track total charged and total refunded amounts.
   - Implement all abstract methods.
   - Override `display_info()` with relevant details.

4. Demonstrate:
   - Attempting to instantiate `PaymentProcessor` directly (show the error).
   - Processing payments through each processor.
   - Attempting a payment that exceeds the limit/balance.
   - Processing a refund.
   - Displaying info for all processors.

## Expected Output

```
Attempting to create abstract PaymentProcessor...
Error: Can't instantiate abstract class PaymentProcessor with abstract methods authorize, capture, refund

=== Processing Payments ===

Credit Card (****1111):
  Authorized: 25,000.00
  Captured: 25,000.00
  Payment successful!

Bank Transfer (First Bank - ****5678):
  Authorized: 50,000.00
  Captured: 50,000.00
  Payment successful!

Mobile Money (MTN - 08012345678):
  Authorized: 10,000.00
  Captured: 10,000.00
  Payment successful!

=== Attempting Over-Limit Payment ===
Credit Card: Authorization failed for 200,000.00 (exceeds limit)

=== Refund ===
Refunded 5,000.00 to card ****1111. Reason: Customer request

=== Processor Summary ===
Credit Card ****1111 | Charged: 25,000.00 | Refunded: 5,000.00
Bank Transfer ****5678 | Charged: 50,000.00 | Refunded: 0.00
Mobile Money 08012345678 | Charged: 10,000.00 | Refunded: 0.00
```

## Assessment

1. What is the difference between an abstract class and a regular class?
2. What happens if a subclass of an abstract class does not implement all abstract methods?
3. Why is abstraction useful when multiple developers work on different parts of a system?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-04/day-038/`

Include your `payment_system.py` file.

## Additional Resources

- [Lecture 08 — Abstraction & ABCs](../../../python-oop/lectures/08-abstraction.md)
- [Exercise 08 — Abstraction](../../../python-oop/exercises/08-abstraction/)
- [Python Docs: abc module](https://docs.python.org/3/library/abc.html)

## Reflection

- How does defining an abstract interface upfront help a team of developers build a system in parallel?
- Think of a system with multiple implementations of the same concept (payment methods, notification channels, export formats). How would abstraction help ensure consistency?
