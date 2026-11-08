# Day 009: Mini Project Planning

## Learning Objectives

- Review and consolidate all concepts learned in Days 1 through 8.
- Break a problem into smaller, manageable steps using decomposition.
- Write pseudocode to plan a program before writing actual code.
- Design the structure of a multi-feature program.
- Prepare for the Module 1 capstone project.

## Introduction

Professional software engineers do not start by writing code. They start by understanding the problem, planning their approach, and breaking the work into steps. This process is called decomposition, and it is one of the most valuable skills you can develop.

Today you will review everything from the past eight days and apply it to planning tomorrow's project. You will practice writing pseudocode, which is a plain-language description of what your program will do, step by step.

## Concepts

### Problem Decomposition

Decomposition means breaking a complex problem into smaller, simpler parts. Each part can be solved independently and then combined into a complete solution.

Example: "Build a student profile and calculator" becomes:

1. Collect student information from the user.
2. Validate the input.
3. Perform calculations (age in days, BMI, etc.).
4. Format and display the results.

### Pseudocode

Pseudocode is an informal way to describe your program logic without worrying about syntax. It helps you think through the logic before committing to code.

```
START
    ASK user for their name
    ASK user for their year of birth
    CALCULATE age = current year - year of birth
    CALCULATE age in days = age * 365
    DISPLAY name and age
    DISPLAY age in days
END
```

### Planning Checklist

Before starting any project, answer these questions:

1. **What does the program do?** (One sentence)
2. **What inputs does it need?** (List all user inputs)
3. **What processing must happen?** (Calculations, decisions, transformations)
4. **What outputs should it produce?** (What the user sees)
5. **What could go wrong?** (Invalid input, edge cases)

## Practical Examples

### Review: Key Concepts from Days 1-8

```python
# Variables and types (Day 2)
name = "Suleiman"
age = 22
gpa = 3.8
is_active = True

# Type conversion (Day 3)
user_age = int(input("Enter age: "))

# String methods (Day 4)
formatted_name = name.upper()
name_length = len(name)

# Input/output formatting (Day 5)
print(f"{'Name':<15} {'Age':>5}")
print(f"{name:<15} {age:>5}")

# Conditionals (Days 6-7)
category = "Youth" if age < 30 else "Adult"

# Debugging mindset (Day 8)
# Always check types, read error messages, use print to trace
```

### Decomposition Example

Problem: Build a program that helps a shopkeeper calculate profit.

Decomposition:

```
1. Get the cost price of the item
2. Get the selling price of the item
3. Calculate profit = selling price - cost price
4. Calculate profit percentage = (profit / cost price) * 100
5. Determine if it is a profit, loss, or break-even
6. Display the results in a formatted summary
```

Pseudocode:

```
START
    ASK for item name
    ASK for cost price (convert to float)
    ASK for selling price (convert to float)

    CALCULATE profit = selling price - cost price
    CALCULATE profit_percent = (profit / cost price) * 100

    IF profit > 0:
        DISPLAY "Profit of X Naira (Y%)"
    ELSE IF profit < 0:
        DISPLAY "Loss of X Naira (Y%)"
    ELSE:
        DISPLAY "Break even — no profit, no loss"
END
```

## Guided Practice

Practice decomposing the Module 1 project. The project is: **Smart Personal Profile and Calculator**.

The program should:
- Collect user information interactively
- Perform several calculations
- Display a formatted profile card
- Handle invalid input gracefully

Work through these steps:

1. List all the inputs the program needs:

```
- Full name
- Year of birth
- Weight in kilograms
- Height in meters
- Monthly income (optional)
```

2. List all the calculations:

```
- Age = current year - year of birth
- Age in days = age * 365 (approximate)
- Age in hours = age in days * 24
- BMI = weight / (height ** 2)
- BMI category (underweight, normal, overweight, obese)
- Annual income = monthly income * 12 (if provided)
```

3. Write pseudocode for the entire program:

```
START
    DISPLAY welcome message
    ASK for full name
    ASK for year of birth (validate: must be a number, must be reasonable)
    ASK for weight in kg (validate: must be positive number)
    ASK for height in meters (validate: must be positive number)
    ASK if they want to include income calculation (yes/no)

    CALCULATE age, age_in_days, age_in_hours
    CALCULATE BMI
    DETERMINE BMI category using if/elif/else

    IF income calculation requested:
        ASK for monthly income
        CALCULATE annual income

    DISPLAY formatted profile card with all results
END
```

4. Identify potential problems:

```
- User enters text instead of a number for year of birth
- User enters negative weight or height
- User enters a future year of birth
- Division by zero if height is 0
```

## Daily Challenge

Choose one of these scenarios and write a complete project plan:

**Option A: Currency Exchange Calculator**
A program that converts between Naira, USD, GBP, and EUR with current (hardcoded) rates.

**Option B: Student Report Card Generator**
A program that takes scores in multiple subjects and produces a formatted report card.

**Option C: Fitness Tracker Summary**
A program that takes daily step counts for a week and produces statistics and recommendations.

For your chosen scenario, create a file called `project_plan.md` (or `project_plan.txt`) containing:

1. **Program description** (one paragraph)
2. **Input list** (all data the program needs)
3. **Processing steps** (what calculations and decisions)
4. **Output description** (what the user sees)
5. **Edge cases** (what could go wrong)
6. **Pseudocode** (step-by-step plan)

Then create a file called `project_prototype.py` containing:
- The basic structure of the program with comments marking where each section goes.
- At least one section fully implemented (for example, the input collection or the output formatting).

## Expected Output

Two files: a planning document with all six sections, and a Python prototype with the program structure outlined and at least one section working.

## Assessment

1. Why is it better to plan a program before writing code?
2. What is the difference between pseudocode and actual Python code?
3. Name three things that could go wrong with user input and how you would handle each one.

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-01/day-009/`

Your submission should include:
- `project_plan.md` (or `.txt`) containing your planning document.
- `project_prototype.py` containing your prototype code.

## Additional Resources

- [Problem Decomposition — Computer Science Concepts](https://docs.python.org/3/tutorial/)
- Review your own code from Days 1-8 to identify patterns you can reuse.

## Reflection

- How did writing pseudocode change the way you think about the problem?
- What part of the project are you most confident about, and what part concerns you?
