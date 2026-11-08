# Day 003: Type Conversion and Arithmetic

## Learning Objectives

- Convert between data types using `int()`, `float()`, `str()`, and `bool()`.
- Understand when and why type conversion is necessary.
- Use all Python arithmetic operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`.
- Understand operator precedence and how to control it with parentheses.
- Combine user input with arithmetic operations.

## Introduction

When you receive input from a user, read data from a file, or combine different kinds of values, you will often need to convert one type to another. For example, `input()` always returns a string, so if you need a number, you must convert it.

Arithmetic is the backbone of computation. Whether you are calculating a student's GPA, converting currencies, or computing loan interest, you need to understand how Python handles mathematical operations. Today you will master both type conversion and arithmetic so you can start building programs that compute real results.

## Concepts

### Type Conversion (Casting)

Python provides built-in functions to convert between types:

| Function  | Converts to | Example                        |
| --------- | ----------- | ------------------------------ |
| `int()`   | Integer     | `int("42")` returns `42`      |
| `float()` | Float       | `float("3.14")` returns `3.14`|
| `str()`   | String      | `str(100)` returns `"100"`    |
| `bool()`  | Boolean     | `bool(1)` returns `True`      |

Not every conversion works. `int("hello")` will raise a `ValueError` because `"hello"` is not a valid number.

### Arithmetic Operators

| Operator | Operation         | Example       | Result  |
| -------- | ----------------- | ------------- | ------- |
| `+`      | Addition          | `10 + 3`      | `13`    |
| `-`      | Subtraction       | `10 - 3`      | `7`     |
| `*`      | Multiplication    | `10 * 3`      | `30`    |
| `/`      | Division          | `10 / 3`      | `3.333` |
| `//`     | Floor division    | `10 // 3`     | `3`     |
| `%`      | Modulo (remainder)| `10 % 3`      | `1`     |
| `**`     | Exponentiation    | `10 ** 3`     | `1000`  |

### Operator Precedence

Python follows standard mathematical order of operations (PEMDAS):
1. Parentheses `()`
2. Exponentiation `**`
3. Multiplication, Division, Floor Division, Modulo `* / // %`
4. Addition, Subtraction `+ -`

Use parentheses to make your intent clear and avoid surprises.

## Practical Examples

```python
# Type conversion examples
age_text = "25"
age_number = int(age_text)
print(age_number + 5)  # 30 — math works on the integer

price = 1500
price_label = "Total: " + str(price) + " Naira"
print(price_label)

gpa_text = "3.85"
gpa = float(gpa_text)
print(gpa * 100)  # 385.0
```

```python
# Arithmetic operations
a = 17
b = 5

print(f"{a} + {b} = {a + b}")    # 22
print(f"{a} - {b} = {a - b}")    # 12
print(f"{a} * {b} = {a * b}")    # 85
print(f"{a} / {b} = {a / b}")    # 3.4
print(f"{a} // {b} = {a // b}")  # 3
print(f"{a} % {b} = {a % b}")    # 2
print(f"{a} ** {b} = {a ** b}")  # 1419857
```

```python
# Practical: converting Celsius to Fahrenheit
celsius = 37.5
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius}C = {fahrenheit}F")  # 37.5C = 99.5F
```

```python
# Practical: calculating total cost with discount
item_price = 4500  # Naira
quantity = 3
discount_percent = 10

subtotal = item_price * quantity
discount = subtotal * discount_percent / 100
total = subtotal - discount

print(f"Subtotal: {subtotal} Naira")
print(f"Discount ({discount_percent}%): {discount} Naira")
print(f"Total: {total} Naira")
```

## Guided Practice

Create a file called `currency_converter.py`:

1. Store an amount in Nigerian Naira as an integer.
2. Define an exchange rate (for example, 1 USD = 1550 Naira).
3. Calculate the equivalent in US Dollars.
4. Print both values formatted to 2 decimal places.

```python
amount_naira = 50000
exchange_rate = 1550  # Naira per USD

amount_usd = amount_naira / exchange_rate

print(f"Amount: {amount_naira:,} Naira")
print(f"Exchange rate: 1 USD = {exchange_rate:,} Naira")
print(f"Equivalent: ${amount_usd:.2f} USD")
```

Now extend the program:

5. Add conversion to British Pounds (1 GBP = 1950 Naira).
6. Add conversion to Euro (1 EUR = 1680 Naira).
7. Print all three conversions.

## Daily Challenge

Build a program called `calculator.py` that:

1. Asks the user to enter two numbers (use `input()` and convert to `float`).
2. Performs all seven arithmetic operations on those numbers.
3. Displays the results in a clean, formatted table.

Your output should look similar to this:

```
Enter the first number: 20
Enter the second number: 7

=========== RESULTS ===========
20.0 + 7.0  = 27.0
20.0 - 7.0  = 13.0
20.0 * 7.0  = 140.0
20.0 / 7.0  = 2.86
20.0 // 7.0 = 2.0
20.0 % 7.0  = 6.0
20.0 ** 7.0 = 1280000000.0
================================
```

Handle the case where the second number is zero for division and modulo by printing an appropriate message instead of crashing.

## Expected Output

A formatted table showing all seven arithmetic operations applied to the two user-provided numbers, with division by zero handled gracefully.

## Assessment

1. What happens if you try to do `int("3.14")`? How would you convert `"3.14"` to an integer?
2. What is the difference between `/` and `//` in Python?
3. Why does `input()` always return a string, even when the user types a number?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-01/day-003/`

Your submission should include:
- `calculator.py` containing your solution to the daily challenge.

## Additional Resources

- [Python Official Docs — Numeric Types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
- [Python Official Docs — Built-in Functions](https://docs.python.org/3/library/functions.html)

## Reflection

- When would you use floor division (`//`) instead of regular division (`/`) in a real program?
- What could go wrong if you forget to convert user input from a string to a number?
