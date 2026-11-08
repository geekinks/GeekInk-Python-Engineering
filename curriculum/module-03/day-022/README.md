# Day 022: Parameters and Return Values

## Learning Objectives

- Understand the difference between parameters and arguments.
- Pass multiple parameters to a function.
- Use the `return` statement to send results back to the caller.
- Return multiple values from a function using tuples.
- Design functions with clear inputs and outputs.

## Introduction

Yesterday you learned to define and call functions. Today you will learn how to make functions truly flexible by giving them parameters and getting results back through return values. A function without parameters can only do one fixed thing. A function with parameters can work with different data every time it is called.

Return values are equally important. Instead of printing results inside a function, you return them to the caller. This lets the caller decide what to do with the result: print it, store it, pass it to another function, or use it in a calculation. Functions that return values are composable — you can chain them together to build complex behavior from simple pieces.

Mastering parameters and return values is what turns your functions from convenient shortcuts into powerful building blocks.

## Concepts

### Parameters vs Arguments

A **parameter** is the variable name in the function definition. An **argument** is the actual value you pass when you call the function.

```python
def greet(name):      # 'name' is a parameter
    print(f"Hello, {name}!")

greet("Aisha")        # "Aisha" is an argument
```

### Multiple Parameters

Functions can accept any number of parameters, separated by commas.

### The `return` Statement

The `return` statement ends the function and sends a value back to the caller. Any code after `return` inside the function does not execute.

### Returning Multiple Values

Python lets you return multiple values as a tuple. The caller can unpack them into separate variables.

```python
def divide(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide(17, 5)
```

## Practical Examples

```python
# Function with multiple parameters
def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)


bmi = calculate_bmi(70, 1.75)
print(f"BMI: {bmi}")
# Output: BMI: 22.9


# Returning multiple values
def min_max(numbers):
    return min(numbers), max(numbers)


lowest, highest = min_max([45, 12, 89, 34, 67])
print(f"Lowest: {lowest}, Highest: {highest}")
# Output: Lowest: 12, Highest: 89


# Using a return value in further computation
def calculate_discount(price, discount_percent):
    discount_amount = price * (discount_percent / 100)
    return price - discount_amount


original = 5000
discounted = calculate_discount(original, 15)
tax = discounted * 0.075
total = discounted + tax
print(f"Original: {original}")
print(f"After discount: {discounted}")
print(f"After tax: {total}")


# A function that returns a boolean
def is_passing(score, threshold=50):
    return score >= threshold


print(is_passing(72))    # True
print(is_passing(35))    # False


# The difference between print and return
def add_and_print(a, b):
    print(a + b)        # Displays but returns None

def add_and_return(a, b):
    return a + b         # Returns the value silently

result1 = add_and_print(3, 4)    # Prints 7
result2 = add_and_return(3, 4)   # Returns 7

print(f"result1: {result1}")     # None
print(f"result2: {result2}")     # 7
```

## Guided Practice

Build a unit converter step by step.

**Step 1:** Write a function to convert kilometers to miles.

```python
def km_to_miles(km):
    return km * 0.621371
```

**Step 2:** Write a function to convert Celsius to Fahrenheit.

```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32
```

**Step 3:** Write a function to convert kilograms to pounds.

```python
def kg_to_pounds(kg):
    return kg * 2.20462
```

**Step 4:** Combine them in a program that asks the user for input.

```python
def km_to_miles(km):
    return round(km * 0.621371, 2)

def celsius_to_fahrenheit(celsius):
    return round((celsius * 9 / 5) + 32, 2)

def kg_to_pounds(kg):
    return round(kg * 2.20462, 2)


print("Unit Converter")
print("1. Kilometers to Miles")
print("2. Celsius to Fahrenheit")
print("3. Kilograms to Pounds")

choice = input("Choose conversion (1/2/3): ")

if choice == "1":
    value = float(input("Enter kilometers: "))
    print(f"{value} km = {km_to_miles(value)} miles")
elif choice == "2":
    value = float(input("Enter Celsius: "))
    print(f"{value} C = {celsius_to_fahrenheit(value)} F")
elif choice == "3":
    value = float(input("Enter kilograms: "))
    print(f"{value} kg = {kg_to_pounds(value)} lbs")
else:
    print("Invalid choice.")
```

## Daily Challenge

Build a **unit converter** program called `converter.py` with the following functions:

1. `km_to_miles(km)` — Returns the value in miles.
2. `miles_to_km(miles)` — Returns the value in kilometers.
3. `celsius_to_fahrenheit(celsius)` — Returns the value in Fahrenheit.
4. `fahrenheit_to_celsius(fahrenheit)` — Returns the value in Celsius.
5. `kg_to_pounds(kg)` — Returns the value in pounds.
6. `pounds_to_kg(pounds)` — Returns the value in kilograms.

Requirements:
- All functions must use `return`, not `print`.
- All results should be rounded to 2 decimal places.
- Add a main section that presents a menu, takes user input, calls the appropriate function, and displays the result.
- The program should handle at least one round of conversion and display the result clearly.

## Expected Output

```
=== Unit Converter ===
1. Kilometers to Miles
2. Miles to Kilometers
3. Celsius to Fahrenheit
4. Fahrenheit to Celsius
5. Kilograms to Pounds
6. Pounds to Kilograms

Choose an option: 3
Enter value: 37.5
37.5 Celsius = 99.5 Fahrenheit
```

## Assessment

1. What is the difference between a parameter and an argument?
2. What happens if you try to use the return value of a function that only uses `print` inside it?
3. How do you return multiple values from a function in Python, and how does the caller receive them?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-03/day-022/`

Include your `converter.py` file.

## Additional Resources

- [Python Tutorial: More on Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)
- [Real Python: Defining Your Own Functions](https://realpython.com/defining-your-own-python-function/)

## Reflection

- Why is it better for a function to return a value rather than print it directly?
- Think about a calculation you perform regularly. How would you design a function for it? What would the parameters and return value be?
