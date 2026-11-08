# Day 015: While Loops

## Learning Objectives

- Use `while` loops for repetition based on a condition.
- Understand the difference between `for` loops and `while` loops.
- Use `break` to exit a loop early and `continue` to skip iterations.
- Avoid infinite loops and recognize when they occur.
- Apply while loops to build interactive, menu-driven programs.

## Introduction

A `for` loop runs a fixed number of times — once for each item in a sequence. A `while` loop runs as long as a condition is true. This makes while loops ideal for situations where you do not know in advance how many times the loop should run: waiting for correct user input, running a game until the player quits, or processing data until a condition is met.

## Concepts

### Basic While Loop

```python
while condition:
    # This block repeats as long as condition is True
```

The condition is checked before each iteration. If it is `False` from the start, the block never executes.

### Controlling Loop Flow

- `break`: Immediately exits the loop.
- `continue`: Skips the rest of the current iteration and moves to the next.

```python
while True:
    command = input("Enter command (q to quit): ")
    if command == "q":
        break
    if command == "":
        continue
    print(f"Processing: {command}")
```

### Sentinel Values

A sentinel is a special value that signals the loop to stop:

```python
total = 0
while True:
    value = input("Enter a number (or 'done' to finish): ")
    if value == "done":
        break
    total += float(value)
print(f"Total: {total}")
```

### Avoiding Infinite Loops

If the condition never becomes `False`, the loop runs forever. Always ensure something inside the loop moves toward ending the condition:

```python
# Dangerous — infinite loop
# count = 0
# while count < 5:
#     print(count)
#     # Forgot to increment count!

# Safe
count = 0
while count < 5:
    print(count)
    count += 1
```

## Practical Examples

```python
# Countdown
count = 10
while count > 0:
    print(count)
    count -= 1
print("Liftoff!")
```

```python
# Input validation loop
while True:
    age_input = input("Enter your age: ")
    if age_input.isdigit() and 0 < int(age_input) < 150:
        age = int(age_input)
        break
    print("Please enter a valid age (1-149).")
print(f"Your age is {age}")
```

```python
# Password attempt limiter
correct_password = "geekink2024"
attempts = 3

while attempts > 0:
    password = input(f"Enter password ({attempts} attempts left): ")
    if password == correct_password:
        print("Access granted!")
        break
    attempts -= 1
    if attempts > 0:
        print("Wrong password. Try again.")
else:
    print("Account locked. Too many failed attempts.")
```

```python
# Accumulator pattern
print("Enter numbers to calculate running total. Type 'stop' to finish.")
total = 0
count = 0

while True:
    entry = input("> ")
    if entry.lower() == "stop":
        break
    try:
        number = float(entry)
        total += number
        count += 1
        print(f"  Running total: {total:.2f}")
    except ValueError:
        print("  Not a valid number. Try again.")

if count > 0:
    print(f"\nFinal total: {total:.2f}")
    print(f"Numbers entered: {count}")
    print(f"Average: {total / count:.2f}")
else:
    print("No numbers entered.")
```

## Guided Practice

Create a file called `pin_validator.py`:

1. Set a correct PIN (e.g., "1234").
2. Give the user 3 attempts to enter the correct PIN.
3. After each wrong attempt, tell them how many tries remain.
4. If they get it right, display "Access granted."
5. If they exhaust all attempts, display "Card blocked."

```python
correct_pin = "1234"
max_attempts = 3
attempts = 0

print("ATM Login")
print("-" * 20)

while attempts < max_attempts:
    pin = input("Enter your PIN: ")
    attempts += 1

    if pin == correct_pin:
        print("Access granted. Welcome!")
        break

    remaining = max_attempts - attempts
    if remaining > 0:
        print(f"Incorrect PIN. {remaining} attempt(s) remaining.")
    else:
        print("Too many incorrect attempts. Card blocked.")
```

## Daily Challenge

Build a program called `guessing_game.py`:

1. The computer picks a random number between 1 and 100 (use `from random import randint`).
2. The player guesses repeatedly until they get it right.
3. After each guess, tell the player if the answer is higher or lower.
4. Track the number of guesses.
5. After winning, display the number of guesses and a rating:
   - 1-5 guesses: "Excellent!"
   - 6-10 guesses: "Good job!"
   - 11+ guesses: "Keep practicing!"
6. Ask if the player wants to play again.

Example interaction:

```
===== NUMBER GUESSING GAME =====
I picked a number between 1 and 100.

Guess: 50
Too high! Try lower.

Guess: 25
Too low! Try higher.

Guess: 37
Too low! Try higher.

Guess: 42
Correct! You got it in 4 guesses.
Rating: Excellent!

Play again? (yes/no): no
Thanks for playing!
```

## Expected Output

A fully playable number guessing game with hints after each guess, a guess counter, performance rating, and replay option.

## Assessment

1. What is the key difference between a `for` loop and a `while` loop?
2. What does the `break` statement do inside a while loop?
3. How would you prevent an infinite loop when using `while True`?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-02/day-015/`

Your submission should include:
- `guessing_game.py` containing your solution to the daily challenge.

## Additional Resources

- [Python Official Docs — while Statement](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement)
- [Python Official Docs — random Module](https://docs.python.org/3/library/random.html)

## Reflection

- When is a `while` loop more appropriate than a `for` loop?
- What strategies did you use to handle invalid input inside a while loop?
