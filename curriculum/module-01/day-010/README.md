# Day 010: Module 1 Project — Smart Personal Profile and Calculator

## Learning Objectives

- Apply all Python fundamentals learned in Days 1 through 9.
- Build a complete, multi-feature interactive program from scratch.
- Practice input validation and error handling.
- Produce clean, formatted output for a real-world use case.
- Experience the full cycle of planning, building, and testing a project.

## Introduction

Today is your first project day. You will combine everything from Module 1 — variables, data types, type conversion, strings, input/output, conditionals, and debugging — into a single, polished program.

This project is your first portfolio piece. Treat it like real software: it should handle unexpected input, produce clean output, and be something you are proud to show.

## Project: Smart Personal Profile and Calculator

### Problem Statement

Build an interactive Python program that collects personal information from the user, performs useful calculations, and displays a comprehensive, formatted profile card.

### Requirements

Your program must:

1. **Collect user information:**
   - Full name
   - Year of birth
   - Gender (for appropriate pronouns in output)
   - Weight in kilograms
   - Height in meters
   - City of residence
   - Monthly income in Naira (optional — user can skip)

2. **Perform calculations:**
   - Age (based on current year)
   - Age in days (approximate: age * 365)
   - Age in hours (age_in_days * 24)
   - BMI (Body Mass Index): `weight / (height ** 2)`
   - BMI category:
     - Below 18.5: Underweight
     - 18.5 to 24.9: Normal weight
     - 25.0 to 29.9: Overweight
     - 30.0 and above: Obese
   - If income is provided: annual income and daily income

3. **Handle invalid input:**
   - If the user enters a non-numeric value for year, weight, or height, display a helpful message.
   - If height is zero or negative, prevent division by zero.
   - If year of birth is in the future or unreasonably old, display a message.

4. **Display a formatted profile card** with borders, aligned labels, and all calculated values.

### Suggested Architecture

```
1. Welcome message and instructions
2. Input collection section
3. Validation checks
4. Calculation section
5. Profile card display
```

### Starter Code

Use this scaffold as your starting point. Fill in the sections marked with comments.

```python
# ============================================
# GeekInk Python Engineering
# Module 1 Project: Smart Personal Profile
# ============================================

from datetime import datetime

CURRENT_YEAR = datetime.now().year


def main():
    print("=" * 50)
    print("   SMART PERSONAL PROFILE AND CALCULATOR")
    print("   GeekInk Python Engineering — Module 1")
    print("=" * 50)
    print()

    # --- Section 1: Collect Information ---
    name = input("Enter your full name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    # TODO: Collect year of birth (validate it is a number)
    # TODO: Collect weight in kg (validate it is a positive number)
    # TODO: Collect height in meters (validate it is a positive number)
    # TODO: Collect city
    # TODO: Ask if user wants to include income calculation

    # --- Section 2: Perform Calculations ---
    # TODO: Calculate age, age_in_days, age_in_hours
    # TODO: Calculate BMI and determine BMI category
    # TODO: If income provided, calculate annual and daily income

    # --- Section 3: Display Profile Card ---
    # TODO: Print a formatted profile card with all information

    print()
    print("Thank you for using the Smart Profile Generator!")


if __name__ == "__main__":
    main()
```

### Example Output

```
==================================================
   SMART PERSONAL PROFILE AND CALCULATOR
   GeekInk Python Engineering — Module 1
==================================================

Enter your full name: Amina Bello
Enter your year of birth: 1999
Enter your weight in kg: 62
Enter your height in meters: 1.65
Enter your city: Kaduna
Include income calculation? (yes/no): yes
Enter your monthly income in Naira: 85000

==================================================
              PERSONAL PROFILE CARD
==================================================
  Name:             Amina Bello
  City:             Kaduna
  Year of Birth:    1999
  Age:              25 years
  Age in Days:      9,125 days
  Age in Hours:     219,000 hours
--------------------------------------------------
  Weight:           62.0 kg
  Height:           1.65 m
  BMI:              22.77
  BMI Category:     Normal weight
--------------------------------------------------
  Monthly Income:   85,000.00 Naira
  Annual Income:    1,020,000.00 Naira
  Daily Income:     2,794.52 Naira
==================================================
```

## Features Checklist

Use this checklist to ensure your project is complete:

- [ ] Program collects all required information from the user.
- [ ] All calculations produce correct results.
- [ ] Invalid input is handled gracefully (no crashes).
- [ ] Profile card is neatly formatted with alignment.
- [ ] Income section is optional and only shown if the user chose to include it.
- [ ] BMI category is correctly determined.
- [ ] Program has a clear welcome message and closing message.

## Assessment

Your project will be evaluated on:

| Criteria                  | Weight |
| ------------------------- | ------ |
| Correct calculations      | 30%    |
| Input validation          | 20%    |
| Output formatting         | 20%    |
| Code readability          | 15%    |
| Completeness              | 15%    |

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-01/day-010/`

Your submission should include:
- `smart_profile.py` containing your complete project.

## Additional Resources

- Review your work from Days 1-9 for techniques to reuse.
- [Python Official Docs — datetime](https://docs.python.org/3/library/datetime.html)

## Reflection

- What was the hardest part of building this project?
- If you had more time, what feature would you add?
- How did planning (Day 9) help you build the project today?
