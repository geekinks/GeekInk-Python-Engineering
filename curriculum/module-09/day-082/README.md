# Day 082: Advanced Debugging

## Learning Objectives

- Use Python's built-in `pdb` debugger to step through code interactively.
- Set breakpoints, inspect variables, and evaluate expressions during execution.
- Apply conditional breakpoints to pause only when specific conditions are met.
- Develop a systematic debugging strategy: reproduce, isolate, diagnose, fix, verify.
- Use `breakpoint()` (Python 3.7+) as the modern way to enter the debugger.

## Introduction

Every programmer writes bugs. What separates a junior developer from a senior one is not the absence of bugs but the speed and method with which they find and fix them. Scattering `print()` statements throughout your code is a common first instinct, but it scales poorly. You end up with dozens of print statements, forget to remove them, and still lack the ability to pause execution and inspect the full program state at a specific moment.

Python ships with `pdb`, a powerful interactive debugger that lets you pause your program at any line, inspect every variable in scope, step through execution one line at a time, and even evaluate arbitrary Python expressions in the current context. Learning `pdb` is one of the highest-leverage skills you can develop as a Python engineer.

Beyond tools, debugging is a discipline. A systematic approach --- reproduce the bug reliably, isolate the smallest failing case, form a hypothesis, test it, and verify the fix --- will save you hours compared to randomly changing code and hoping the problem goes away.

## Concepts

### The pdb Debugger

You can enter the debugger by inserting `breakpoint()` anywhere in your code. When Python hits that line, it pauses and gives you an interactive prompt.

### Essential pdb Commands

| Command | Shortcut | Description |
|---------|----------|-------------|
| `help` | `h` | Show available commands |
| `next` | `n` | Execute the next line (step over) |
| `step` | `s` | Step into a function call |
| `continue` | `c` | Continue running until next breakpoint |
| `print expr` | `p expr` | Print the value of an expression |
| `pp expr` | | Pretty-print the value |
| `list` | `l` | Show source code around current line |
| `where` | `w` | Show the call stack |
| `up` / `down` | `u` / `d` | Move up or down the call stack |
| `quit` | `q` | Quit the debugger |
| `break lineno` | `b lineno` | Set a breakpoint at a line number |
| `break func` | `b func` | Set a breakpoint at a function |
| `condition N expr` | | Break at breakpoint N only when expr is true |

### Debugging Strategy

1. **Reproduce**: Can you make the bug happen every time with the same inputs?
2. **Isolate**: What is the smallest input or code path that triggers it?
3. **Hypothesize**: Based on the symptoms, where might the bug be?
4. **Diagnose**: Use the debugger to verify your hypothesis.
5. **Fix**: Make the minimal change that corrects the behavior.
6. **Verify**: Confirm the fix works and does not break other things.

## Practical Examples

### Example 1: Basic breakpoint usage

```python
def calculate_grade(scores):
    """Calculate a weighted grade from a list of (score, weight) tuples."""
    total_score = 0
    total_weight = 0
    for score, weight in scores:
        total_score += score * weight
        total_weight += weight

    breakpoint()  # Pause here to inspect values

    return total_score / total_weight


student_scores = [(85, 0.3), (90, 0.3), (78, 0.4)]
result = calculate_grade(student_scores)
print(f"Final grade: {result:.1f}")
```

When you run this, Python pauses at the `breakpoint()` line. At the `(Pdb)` prompt you can type:

```
(Pdb) p total_score
84.7
(Pdb) p total_weight
1.0
(Pdb) p total_score / total_weight
84.7
(Pdb) c
```

### Example 2: Debugging a bug

```python
def find_longest_streak(values):
    """Find the longest consecutive streak of increasing values."""
    if not values:
        return 0

    longest = 1
    current = 1

    for i in range(1, len(values)):
        if values[i] > values[i - 1]:
            current += 1
        else:
            current = 1  # Bug was here: originally reset to 0

        if current > longest:
            longest = current

    return longest


# This should return 4 (the streak 2, 5, 7, 9)
data = [3, 2, 5, 7, 9, 1, 4, 6]
print(f"Longest streak: {find_longest_streak(data)}")
```

To debug, add `breakpoint()` inside the loop and use conditional inspection:

```python
for i in range(1, len(values)):
    if values[i] > values[i - 1]:
        current += 1
    else:
        breakpoint()  # Pause when streak breaks
        current = 1
```

### Example 3: Conditional breakpoints from the command line

```python
def process_transactions(transactions):
    """Sum transactions, flagging any negative amounts."""
    total = 0
    for i, amount in enumerate(transactions):
        total += amount
    return total


data = [100, 250, -50, 300, -75, 400]
# Run: python -m pdb script.py
# At (Pdb) prompt:
#   b 5, amount < 0       # Break only when amount is negative
#   c                      # Continue; stops at first negative amount
```

## Guided Practice

1. Create a file `debug_exercise.py` with the following buggy code:

```python
def merge_sorted_lists(list_a, list_b):
    """Merge two sorted lists into one sorted list."""
    result = []
    i = 0
    j = 0

    while i < len(list_a) and j < len(list_b):
        if list_a[i] <= list_b[j]:
            result.append(list_a[i])
            i += 1
        else:
            result.append(list_b[j])
            j += 1

    # Bug: only one of these should run, but the slicing is correct.
    # The real bug is elsewhere --- find it using pdb.
    result.extend(list_a[i:])
    result.extend(list_b[j:])

    return result


def find_median(numbers):
    """Find the median of a list of numbers."""
    sorted_nums = merge_sorted_lists(
        sorted(numbers[:len(numbers)//2]),
        sorted(numbers[len(numbers)//2:])
    )
    n = len(sorted_nums)
    if n % 2 == 1:
        return sorted_nums[n // 2]
    else:
        return (sorted_nums[n // 2] + sorted_nums[n // 2 - 1]) / 2


test_data = [7, 3, 1, 9, 5, 2, 8, 4, 6]
print(f"Median: {find_median(test_data)}")
# Expected: 5
```

2. Run the file. Check if the output is correct.

3. If not, insert `breakpoint()` calls and use `pdb` to step through the logic. Check the values of `sorted_nums` after the merge.

4. Fix the bug and verify.

## Daily Challenge

Debug the following three programs. For each one, describe the bug, explain how you found it using `pdb`, and provide the corrected code.

### Program 1: Grade Calculator

```python
def letter_grade(percentage):
    if percentage >= 90:
        return "A"
    if percentage >= 80:
        return "B"
    if percentage >= 70:
        return "C"
    if percentage >= 60:
        return "D"
    return "F"


def class_summary(students):
    grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for name, scores in students.items():
        avg = sum(scores) / len(scores)
        grade = letter_grade(avg)
        grade_counts[grade] += 1
    return grade_counts


data = {
    "Amina": [88, 92, 79],
    "Ibrahim": [55, 60, 48],
    "Fatima": [95, 98, 100],
    "Yusuf": [],  # This student has no scores --- will crash
}

print(class_summary(data))
```

### Program 2: Fibonacci with Memoization

```python
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    memo[n] = result
    return result


# Should print first 10 Fibonacci numbers
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")

# Bug: the mutable default argument persists across calls.
# What happens if you call fibonacci(5) in a second script run?
# Use pdb to inspect the memo dict.
```

### Program 3: Word Frequency Counter

```python
def count_words(text):
    words = text.lower().split()
    frequency = {}
    for word in words:
        cleaned = ""
        for char in word:
            if char.isalpha():
                cleaned += char
        frequency[cleaned] = frequency.get(cleaned, 0) + 1
    return frequency


def top_words(text, n=5):
    freq = count_words(text)
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:n]


sample = "The quick brown fox jumps over the lazy dog. The dog barked at the fox."
result = top_words(sample, 3)
for word, count in result:
    print(f"{word}: {count}")

# Check: does the empty string end up as a key in the frequency dict?
# Use pdb to inspect freq after count_words returns.
```

## Expected Output

For each program, submit:
- A text file describing the bug and how you found it with `pdb`.
- The corrected Python file.
- The correct output of each program after fixing.

## Assessment

1. What is the difference between `next` (n) and `step` (s) in pdb?
2. How do you set a conditional breakpoint that only triggers when a variable exceeds a specific value?
3. Why is a systematic debugging strategy more effective than adding random print statements?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-09/day-082/`

Include:
- `program1_fix.py`, `program2_fix.py`, `program3_fix.py`
- `debug_report.txt` (describing each bug and how you found it)

## Additional Resources

- [Python pdb documentation](https://docs.python.org/3/library/pdb.html)
- [Python Debugging with breakpoint()](https://docs.python.org/3/library/functions.html#breakpoint)

## Reflection

- How has your debugging process changed after learning about pdb? Will you still rely on print statements?
- Think of a bug you struggled with in the past. How would pdb have helped you find it faster?
