# Day 006: Conditional Statements

## Learning Objectives

- Write `if`, `elif`, and `else` statements to control program flow.
- Use comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`) to form conditions.
- Combine conditions using logical operators (`and`, `or`, `not`).
- Nest conditional statements for multi-level decision-making.
- Apply conditionals to solve real-world decision problems.

## Introduction

Programs need to make decisions. Should the user be granted access? Is the student's score a pass or a fail? Should the system apply a discount? Conditional statements let your program choose different paths based on whether a condition is true or false.

This is one of the most fundamental concepts in programming. Every application you use — from login screens to banking apps to games — relies on conditional logic. Today you will learn to make your programs smart enough to respond differently based on the data they receive.

## Concepts

### The `if` Statement

The `if` statement executes a block of code only when its condition is `True`:

```python
if condition:
    # This code runs only when condition is True
```

### The `if/else` Statement

```python
if condition:
    # Runs when True
else:
    # Runs when False
```

### The `if/elif/else` Chain

```python
if condition_1:
    # Runs when condition_1 is True
elif condition_2:
    # Runs when condition_2 is True
else:
    # Runs when no condition above was True
```

### Comparison Operators

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

### Logical Operators

| Operator | Meaning                          |
| -------- | -------------------------------- |
| `and`    | True if both conditions are True |
| `or`     | True if at least one is True     |
| `not`    | Reverses the truth value         |

## Practical Examples

```python
# Simple if/else
age = 18
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not yet eligible to vote.")
```

```python
# if/elif/else chain
score = 75

if score >= 70:
    grade = "A"
elif score >= 60:
    grade = "B"
elif score >= 50:
    grade = "C"
elif score >= 40:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")
```

```python
# Logical operators
temperature = 32
is_raining = True

if temperature > 35 and not is_raining:
    print("It is hot and dry. Stay hydrated.")
elif temperature > 35 and is_raining:
    print("It is hot but raining. Humid weather.")
elif is_raining:
    print("Take an umbrella.")
else:
    print("Weather is fine.")
```

```python
# Nested conditionals
has_account = True
balance = 5000
withdrawal = 3000

if has_account:
    if withdrawal <= balance:
        balance -= withdrawal
        print(f"Withdrawal successful. New balance: {balance} Naira")
    else:
        print("Insufficient funds.")
else:
    print("No account found.")
```

## Guided Practice

Create a file called `admission_checker.py`:

1. Ask the user for their JAMB score (out of 400) and their O-Level credits (number of subjects with C6 or above).
2. Apply these admission rules:
   - JAMB >= 250 and credits >= 5: "Admitted"
   - JAMB >= 200 and credits >= 5: "Supplementary list"
   - JAMB >= 200 and credits < 5: "Improve your O-Level results"
   - JAMB < 200: "Score too low. Try again next year."

```python
jamb_score = int(input("Enter your JAMB score (out of 400): "))
credits = int(input("Enter number of O-Level credits (C6 and above): "))

if jamb_score >= 250 and credits >= 5:
    print("Congratulations! You are on the admission list.")
elif jamb_score >= 200 and credits >= 5:
    print("You are on the supplementary admission list.")
elif jamb_score >= 200 and credits < 5:
    print("Your JAMB score qualifies, but improve your O-Level results.")
else:
    print("Your JAMB score is below the cutoff. Try again next year.")
```

## Daily Challenge

Build a program called `grade_calculator.py` that:

1. Asks the user for their name and scores in five subjects (each out of 100):
   - Mathematics
   - English
   - Science
   - Social Studies
   - Computer Science

2. Calculates the average score.

3. Assigns a grade based on the average:
   - 90-100: A (Excellent)
   - 80-89: B (Very Good)
   - 70-79: C (Good)
   - 60-69: D (Fair)
   - 50-59: E (Pass)
   - Below 50: F (Fail)

4. Determines pass/fail status: the student passes only if the average is 50 or above AND no individual subject is below 30.

5. Displays a formatted result card:

```
======= RESULT CARD =======
Student: Hauwa Ibrahim

Mathematics:      78
English:          85
Science:          62
Social Studies:   90
Computer Science: 88

Average: 80.6
Grade:   B (Very Good)
Status:  PASSED
============================
```

## Expected Output

A complete result card showing all five scores, the calculated average, the letter grade with description, and the pass/fail status.

## Assessment

1. What is the difference between `=` and `==` in Python?
2. In an `if/elif/else` chain, can more than one block execute? Why or why not?
3. What does `not (age > 18)` evaluate to when `age` is `20`?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-01/day-006/`

Your submission should include:
- `grade_calculator.py` containing your solution to the daily challenge.

## Additional Resources

- [Python Official Docs — if Statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
- [Python Official Docs — Comparisons](https://docs.python.org/3/reference/expressions.html#comparisons)

## Reflection

- Think of a real-world situation where you make a multi-step decision. How would you model it using if/elif/else?
- Why is the order of conditions in an elif chain important?
