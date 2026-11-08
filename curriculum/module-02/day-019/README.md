# Day 019: Problem Decomposition and Algorithmic Thinking

## Learning Objectives

- Break complex problems into smaller, independent sub-problems.
- Write helper functions that each solve one part of a problem.
- Think step by step about the sequence of operations needed to solve a problem.
- Apply decomposition to multi-step data processing tasks.
- Prepare for building larger programs from composed smaller parts.

## Introduction

As programs grow more complex, you cannot solve everything in one block of code. Professional software engineers decompose problems: they break a big problem into smaller pieces, solve each piece independently, and combine the results. This approach makes code easier to write, test, understand, and maintain.

Today you will practice this essential skill by tackling multi-step problems and writing small, focused helper functions that work together to produce a complete solution.

## Concepts

### The Decomposition Process

1. **Understand** the full problem.
2. **Identify** the distinct sub-tasks.
3. **Solve** each sub-task independently (as a function).
4. **Combine** the solutions into a complete program.

### Writing Helper Functions

A helper function does one thing well:

```python
def calculate_average(scores):
    return sum(scores) / len(scores)

def determine_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"

def format_result(name, average, grade):
    return f"{name}: {average:.1f} ({grade})"
```

### Composing Functions

```python
def process_student(name, scores):
    avg = calculate_average(scores)
    grade = determine_grade(avg)
    return format_result(name, avg, grade)

print(process_student("Amina", [85, 92, 78]))
# Amina: 85.0 (A)
```

## Practical Examples

```python
# Problem: Analyze a paragraph of text
# Decompose into: count_words, count_sentences, find_longest_word, calculate_reading_level

def count_words(text):
    return len(text.split())

def count_sentences(text):
    count = 0
    for char in text:
        if char in ".!?":
            count += 1
    return max(count, 1)

def find_longest_word(text):
    words = text.split()
    longest = ""
    for word in words:
        clean = word.strip(".,!?;:")
        if len(clean) > len(longest):
            longest = clean
    return longest

def analyze_text(text):
    words = count_words(text)
    sentences = count_sentences(text)
    longest = find_longest_word(text)
    avg_words_per_sentence = words / sentences

    print(f"Words: {words}")
    print(f"Sentences: {sentences}")
    print(f"Avg words/sentence: {avg_words_per_sentence:.1f}")
    print(f"Longest word: {longest}")

sample = "Python is a powerful language. It is used in many industries. Engineers love it!"
analyze_text(sample)
```

```python
# Problem: Process a shopping receipt
# Decompose into: calculate_subtotal, apply_tax, apply_discount, format_receipt

def calculate_subtotal(items):
    return sum(price * qty for _, price, qty in items)

def apply_tax(subtotal, tax_rate):
    return subtotal * tax_rate / 100

def apply_discount(subtotal, discount_rate):
    return subtotal * discount_rate / 100

def format_receipt(items, tax_rate=7.5, discount_rate=0):
    subtotal = calculate_subtotal(items)
    tax = apply_tax(subtotal, tax_rate)
    discount = apply_discount(subtotal, discount_rate)
    total = subtotal + tax - discount

    print("=" * 40)
    print(f"{'Item':<20} {'Qty':>3} {'Amount':>10}")
    print("-" * 40)
    for name, price, qty in items:
        print(f"{name:<20} {qty:>3} {price * qty:>10,.2f}")
    print("-" * 40)
    print(f"{'Subtotal':<24} {subtotal:>10,.2f}")
    if discount_rate > 0:
        print(f"{'Discount (' + str(discount_rate) + '%)':<24} {-discount:>10,.2f}")
    print(f"{'VAT (' + str(tax_rate) + '%)':<24} {tax:>10,.2f}")
    print(f"{'TOTAL':<24} {total:>10,.2f}")
    print("=" * 40)

cart = [
    ("Rice (50kg)", 45000, 1),
    ("Cooking Oil", 8500, 2),
    ("Sugar (10kg)", 12000, 1),
]

format_receipt(cart, discount_rate=5)
```

## Guided Practice

Decompose this problem: **Password Strength Checker**

A strong password must:
- Be at least 8 characters long
- Contain at least one uppercase letter
- Contain at least one lowercase letter
- Contain at least one digit
- Contain at least one special character (!@#$%^&*)

Create separate functions for each check, then combine them:

```python
def check_length(password, min_length=8):
    return len(password) >= min_length

def has_uppercase(password):
    return any(c.isupper() for c in password)

def has_lowercase(password):
    return any(c.islower() for c in password)

def has_digit(password):
    return any(c.isdigit() for c in password)

def has_special(password):
    special_chars = "!@#$%^&*()-_=+[]{}|;:',.<>?/"
    return any(c in special_chars for c in password)

def check_password_strength(password):
    checks = [
        (check_length(password), "At least 8 characters"),
        (has_uppercase(password), "Contains uppercase letter"),
        (has_lowercase(password), "Contains lowercase letter"),
        (has_digit(password), "Contains a digit"),
        (has_special(password), "Contains special character"),
    ]

    passed = sum(1 for result, _ in checks if result)
    total = len(checks)

    print(f"\nPassword: {'*' * len(password)}")
    print(f"Strength: {passed}/{total}")
    for result, description in checks:
        status = "PASS" if result else "FAIL"
        print(f"  [{status}] {description}")

    if passed == total:
        print("Overall: Strong password!")
    elif passed >= 3:
        print("Overall: Moderate — improve the failed checks.")
    else:
        print("Overall: Weak — needs significant improvement.")

password = input("Enter a password to check: ")
check_password_strength(password)
```

## Daily Challenge

Solve three multi-step problems using decomposition. Create a file called `decomposition.py`.

**Problem 1: Election Results**

Given a list of votes (candidate names), determine:
- Total votes cast
- Votes per candidate
- Percentage per candidate
- The winner (most votes)

```python
votes = ["Amina", "Bashir", "Amina", "Chioma", "Bashir", "Amina",
         "Chioma", "Amina", "Bashir", "Chioma", "Chioma", "Amina"]
```

Write functions: `count_votes(votes)`, `calculate_percentages(vote_counts, total)`, `find_winner(vote_counts)`, and `display_results(votes)`.

**Problem 2: Temperature Analysis**

Given daily temperatures for a week, calculate:
- Average temperature
- Hottest and coldest days
- Days above average
- Temperature trend (increasing, decreasing, or mixed)

```python
temps = [32, 35, 33, 38, 36, 34, 31]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
```

Write functions for each calculation and a `display_analysis()` function.

**Problem 3: Student Class Ranking**

Given a list of students with scores, produce a ranked report card showing position, name, average, grade, and whether they passed.

```python
students = [
    {"name": "Hauwa", "scores": [80, 65, 72]},
    {"name": "Ibrahim", "scores": [55, 88, 60]},
    {"name": "Jummai", "scores": [92, 78, 85]},
    {"name": "Kabir", "scores": [40, 45, 38]},
    {"name": "Laraba", "scores": [70, 72, 68]},
]
```

## Expected Output

Three separate analysis reports, each built from composed helper functions, with clear formatting and correct calculations.

## Assessment

1. Why is it better to break a program into small functions rather than writing one large block?
2. How do you decide where to split a problem into sub-problems?
3. What does it mean for a function to "do one thing well"?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-02/day-019/`

Your submission should include:
- `decomposition.py` containing your solutions to all three problems.

## Additional Resources

- [Python Official Docs — Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- Review the guided practice from Day 9 on pseudocode and planning.

## Reflection

- How did breaking each problem into functions change your approach to solving it?
- Which of the three problems was hardest to decompose, and why?
