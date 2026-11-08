# Day 007: Advanced Conditionals and Logic

## Learning Objectives

- Write complex conditions combining multiple operators.
- Use ternary (conditional) expressions for concise decisions.
- Understand truthiness and falsiness in Python.
- Use `match/case` statements for structured pattern matching (Python 3.10+).
- Apply advanced logic to realistic decision-making scenarios.

## Introduction

Yesterday you learned the fundamentals of conditional statements. Today you will go deeper. Real-world programs often require complex conditions that check multiple factors at once, compact expressions for simple decisions, and structured pattern matching for routing logic.

Understanding truthiness, ternary expressions, and match/case will make your code more expressive and professional. These are tools that experienced Python developers use daily.

## Concepts

### Complex Conditions

You can combine any number of conditions using `and`, `or`, and `not`:

```python
if age >= 18 and has_id and not is_banned:
    print("Access granted")
```

Use parentheses for clarity when mixing operators:

```python
if (score >= 70 and attendance >= 75) or is_special_case:
    print("Eligible")
```

### Ternary (Conditional) Expressions

A compact way to assign a value based on a condition:

```python
# Instead of:
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

# You can write:
status = "Adult" if age >= 18 else "Minor"
```

Use ternary expressions for simple, clear decisions. Avoid nesting them.

### Truthiness and Falsiness

In Python, every value has a truth value. These are considered **falsy** (treated as `False` in a condition):

- `False`
- `0` and `0.0`
- `""` (empty string)
- `[]` (empty list), `{}` (empty dict), `()` (empty tuple), `set()`
- `None`

Everything else is **truthy**. This lets you write concise checks:

```python
name = input("Enter your name: ")
if name:
    print(f"Hello, {name}")
else:
    print("You did not enter a name.")
```

### Match/Case (Python 3.10+)

The `match/case` statement provides structured pattern matching:

```python
command = input("Enter command: ")

match command:
    case "start":
        print("Starting the engine...")
    case "stop":
        print("Stopping the engine...")
    case "status":
        print("Engine is running.")
    case _:
        print(f"Unknown command: {command}")
```

The `_` is a wildcard that matches anything not caught above.

## Practical Examples

```python
# Complex condition: loan eligibility
age = 28
salary = 150000
has_guarantor = True
existing_loans = 0

is_eligible = (
    age >= 21
    and salary >= 100000
    and has_guarantor
    and existing_loans == 0
)

print(f"Loan eligible: {'Yes' if is_eligible else 'No'}")
```

```python
# Ternary expressions
score = 72
result = "Pass" if score >= 50 else "Fail"
print(result)

# Ternary in f-strings
temperature = 38
print(f"Weather: {'Hot' if temperature > 35 else 'Moderate' if temperature > 20 else 'Cold'}")
```

```python
# Truthiness in practice
user_input = input("Enter a value: ").strip()

if user_input:
    print(f"You entered: {user_input}")
else:
    print("Empty input received.")
```

```python
# Match/case for a menu system
print("1. View Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice = input("Select an option: ")

match choice:
    case "1":
        print("Your balance is 25,000 Naira")
    case "2":
        print("Deposit selected")
    case "3":
        print("Withdrawal selected")
    case "4":
        print("Goodbye!")
    case _:
        print("Invalid option. Please choose 1-4.")
```

## Guided Practice

Create a file called `time_greeter.py`:

1. Ask the user for the current hour (0-23).
2. Use conditional logic to greet them appropriately:
   - 5-11: "Good morning"
   - 12-16: "Good afternoon"
   - 17-20: "Good evening"
   - 21-4: "Good night"
3. Add a ternary expression to check if it is a weekday or weekend (ask the user for the day).
4. Combine both into a message.

```python
hour = int(input("Enter current hour (0-23): "))
day = input("Enter day of the week: ").strip().lower()

if 5 <= hour <= 11:
    greeting = "Good morning"
elif 12 <= hour <= 16:
    greeting = "Good afternoon"
elif 17 <= hour <= 20:
    greeting = "Good evening"
else:
    greeting = "Good night"

is_weekend = "weekend" if day in ("saturday", "sunday") else "weekday"

print(f"{greeting}! It is a {is_weekend}.")

if is_weekend == "weekend":
    print("Enjoy your rest or do some coding practice!")
else:
    print("Time to study and build something great!")
```

## Daily Challenge

Build a program called `ticket_pricing.py` for a transportation company:

The base ticket price is 5,000 Naira. Apply the following rules:

1. Ask the user for:
   - Age
   - Whether they are a student (yes/no)
   - Travel class: "economy", "business", or "first"
   - Whether they are traveling during a holiday (yes/no)

2. Apply discounts and surcharges:
   - Children (under 12): 50% discount
   - Seniors (65 and above): 30% discount
   - Students (any age): 20% discount
   - Business class: 50% surcharge on base price
   - First class: 100% surcharge on base price
   - Holiday travel: 15% surcharge on the final price

3. Discounts are not cumulative. Apply the largest applicable discount only.

4. Display a ticket summary:

```
======= TICKET SUMMARY =======
Passenger age:    25
Student:          Yes
Class:            Business
Holiday travel:   No

Base price:       5,000.00
Class surcharge:  2,500.00
Discount (20%):  -1,000.00
Holiday charge:       0.00
-------------------------------
TOTAL:            6,500.00 Naira
===============================
```

## Expected Output

A formatted ticket summary showing the base price, each adjustment applied, and the final total. The largest discount should be applied, and surcharges should stack.

## Assessment

1. What values does Python consider "falsy"?
2. Rewrite this using a ternary expression: `if x > 0: sign = "positive" else: sign = "non-positive"`.
3. What does the `_` pattern match in a `match/case` statement?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-01/day-007/`

Your submission should include:
- `ticket_pricing.py` containing your solution to the daily challenge.

## Additional Resources

- [Python Official Docs — match Statement](https://docs.python.org/3/reference/compound_stmts.html#the-match-statement)
- [Python Official Docs — Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)

## Reflection

- When would you choose a ternary expression over a full if/else block?
- How does understanding truthiness help you write cleaner code?
