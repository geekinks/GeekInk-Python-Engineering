# Smart Personal Profile and Calculator

**Module:** 1 — Python Foundations
**Day:** 10
**Difficulty:** Beginner

---

## Problem Statement

Many beginner programmers struggle to connect isolated concepts (variables, input, conditionals, arithmetic) into a cohesive program. This project brings together every topic from Module 1 into a single interactive application that collects personal information, performs useful calculations, and displays a formatted profile card.

## Objectives

- Apply variables, data types, and type conversion in a real program.
- Accept and validate user input.
- Perform arithmetic calculations with meaningful output.
- Use conditional logic to handle different cases.
- Format and display output in a readable, professional way.
- Practice debugging and handling invalid input gracefully.

## Requirements

### Functional Requirements

1. **Collect user information interactively:**
   - Full name
   - Year of birth
   - Height in meters
   - Weight in kilograms
   - Favorite subject or hobby

2. **Perform calculations:**
   - Age (current year minus birth year)
   - Age in days (approximate: age * 365)
   - Age in hours (age in days * 24)
   - Body Mass Index (BMI = weight / height^2)
   - BMI category (Underweight / Normal / Overweight / Obese)

3. **Display a formatted profile card:**
   - Show all collected information and calculated results in a bordered, readable format.

4. **Handle invalid input:**
   - Non-numeric values for numeric fields should be caught and re-prompted.
   - Negative or impossible values (e.g., height of 0) should be rejected with a clear message.

### Non-Functional Requirements

- The program must run without crashing on any input.
- Output must be clearly formatted and easy to read.
- Code must use meaningful variable names and follow PEP 8 conventions.

## Features

| Feature | Description |
| :--- | :--- |
| Interactive input | Prompts the user for each piece of information |
| Input validation | Rejects invalid or impossible values |
| Age calculations | Computes age in years, days, and hours |
| BMI calculation | Computes BMI and determines the health category |
| Profile card | Displays a formatted summary of all data |

## Suggested Architecture

This is a single-file program. Organize it with clear sections:

```
main.py
├── Input collection (with validation loops)
├── Calculations
├── Profile card formatting
└── Main execution block
```

For cleaner code, consider extracting helper functions:

- `get_valid_number(prompt, min_value, max_value)` — re-prompts until a valid number is entered.
- `calculate_bmi(weight, height)` — returns the BMI value.
- `get_bmi_category(bmi)` — returns the category string.
- `display_profile(data)` — prints the formatted profile card.

## Technologies

- Python 3.10+
- Standard library only (no external packages)

## Implementation Milestones

| Milestone | Description |
| :--- | :--- |
| 1. Basic input | Collect name and year of birth, print them back |
| 2. Calculations | Add age, BMI, and category calculations |
| 3. Validation | Add input validation with re-prompting |
| 4. Profile card | Format and display the complete profile |
| 5. Polish | Handle edge cases, clean up formatting |

## Testing Requirements

Since this is a beginner project, formal automated tests are not required. However, students should manually verify:

- The program handles non-numeric input without crashing.
- The program rejects negative height or weight.
- The BMI category is correct for known values (e.g., BMI of 22 is Normal).
- The profile card displays all information correctly.

**Test cases to try:**

| Input | Expected Behavior |
| :--- | :--- |
| Name: "Amina", Birth year: 2000, Height: 1.65, Weight: 60 | Profile displayed, BMI ~22.0 (Normal) |
| Birth year: "abc" | Error message, re-prompt |
| Height: -1 | Error message, re-prompt |
| Weight: 0 | Error message, re-prompt |

## Expected Deliverables

1. `main.py` — The complete program.
2. A screenshot or text copy of a sample run showing the profile card output.

## Evaluation Criteria

| Criterion | Weight | Description |
| :--- | :--- | :--- |
| Correctness | 30% | Calculations are accurate, program runs without errors |
| Input handling | 20% | Invalid input is handled gracefully |
| Code quality | 20% | Meaningful names, PEP 8, logical structure |
| Output formatting | 20% | Profile card is clear and readable |
| Completeness | 10% | All required features are implemented |
