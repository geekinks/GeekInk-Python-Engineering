# Day 004: Strings and String Methods

## Learning Objectives

- Create strings using single quotes, double quotes, and triple quotes.
- Access individual characters using indexing and extract substrings using slicing.
- Use common string methods to transform and analyze text.
- Format strings using f-strings for clean, readable output.
- Understand that strings are immutable in Python.

## Introduction

Text is everywhere in software. Names, messages, emails, file contents, web pages, and database records all involve strings. As a software engineer, you will spend a significant amount of time working with text data: parsing it, formatting it, searching through it, and transforming it.

Python provides a rich set of tools for working with strings. Mastering these tools early will make you more productive in every project you build, from simple scripts to full web applications.

## Concepts

### Creating Strings

```python
single = 'Hello'
double = "Hello"
multiline = """This string
spans multiple
lines."""
```

Single and double quotes work the same way. Use one when the string contains the other: `"It's Python"` or `'She said "Hello"'`.

### Indexing and Slicing

Strings are sequences of characters. Each character has a position (index) starting from `0`:

```
 H   e   l   l   o
 0   1   2   3   4
-5  -4  -3  -2  -1
```

- `text[0]` gives the first character.
- `text[-1]` gives the last character.
- `text[1:4]` gives characters from index 1 up to (not including) 4.
- `text[:3]` gives the first three characters.
- `text[2:]` gives everything from index 2 onward.

### String Immutability

Strings cannot be changed in place. You cannot do `text[0] = "h"`. Instead, you create a new string with the change you want.

### Common String Methods

| Method          | Purpose                              |
| --------------- | ------------------------------------ |
| `.upper()`      | Convert to uppercase                 |
| `.lower()`      | Convert to lowercase                 |
| `.title()`      | Capitalize each word                 |
| `.strip()`      | Remove leading/trailing whitespace   |
| `.replace(a,b)` | Replace occurrences of `a` with `b`  |
| `.split(sep)`   | Split into a list by separator       |
| `.join(list)`   | Join a list into a string            |
| `.find(sub)`    | Find index of substring, -1 if absent|
| `.count(sub)`   | Count occurrences of substring       |
| `.startswith()` | Check if string starts with a value  |
| `.endswith()`   | Check if string ends with a value    |

## Practical Examples

```python
# Indexing and slicing
name = "Abdullahi"
print(name[0])      # A
print(name[-1])     # i
print(name[0:5])    # Abdul
print(name[:5])     # Abdul
print(name[5:])     # lahi
```

```python
# String methods
greeting = "  hello, world  "
print(greeting.strip())          # "hello, world"
print(greeting.strip().upper())  # "HELLO, WORLD"
print(greeting.strip().title())  # "Hello, World"
```

```python
# Replace and split
sentence = "Python is fun and Python is powerful"
print(sentence.replace("Python", "Programming"))
# "Programming is fun and Programming is powerful"

words = sentence.split(" ")
print(words)   # ['Python', 'is', 'fun', 'and', 'Python', 'is', 'powerful']
print(len(words))  # 7
```

```python
# Join
fruits = ["mango", "banana", "orange"]
result = ", ".join(fruits)
print(result)  # "mango, banana, orange"
```

```python
# f-strings for formatting
student = "Zainab"
score = 87.5
print(f"Student: {student}")
print(f"Score: {score:.1f}%")
print(f"Grade: {'A' if score >= 70 else 'B'}")
```

```python
# Counting and finding
text = "engineering is about solving engineering problems"
print(text.count("engineering"))  # 2
print(text.find("solving"))       # 21
print(text.find("cooking"))       # -1
```

## Guided Practice

Create a file called `name_formatter.py`:

1. Ask the user to enter their full name (first and last name).
2. Print the name in uppercase, lowercase, and title case.
3. Print the number of characters in the name (excluding spaces).
4. Print the initials (first letter of each word).

```python
full_name = input("Enter your full name: ")

print(f"Uppercase:  {full_name.upper()}")
print(f"Lowercase:  {full_name.lower()}")
print(f"Title case: {full_name.title()}")

char_count = len(full_name.replace(" ", ""))
print(f"Characters (no spaces): {char_count}")

parts = full_name.split()
initials = "".join(part[0].upper() for part in parts)
print(f"Initials: {initials}")
```

## Daily Challenge

Build a program called `text_analyzer.py` that:

1. Asks the user to enter a sentence or paragraph of text.
2. Analyzes the text and reports:
   - Total number of characters (including spaces).
   - Total number of characters (excluding spaces).
   - Number of words.
   - Number of sentences (count periods, exclamation marks, and question marks).
   - The longest word in the text.
   - The text reversed.

Example interaction:

```
Enter your text: Python is great. I love coding!

=== Text Analysis ===
Characters (with spaces):    31
Characters (without spaces): 27
Words:                        6
Sentences:                    2
Longest word:                 coding
Reversed:                     !gnidoc evol I .taerg si nohtyP
```

## Expected Output

A formatted analysis report showing all six metrics calculated from the user's input text. The program should handle text with multiple sentences correctly.

## Assessment

1. What is the difference between `text.find("x")` and `text.index("x")` when the substring is not found?
2. Why can you not do `name[0] = "a"` to change the first character of a string?
3. What does `"_".join(["a", "b", "c"])` produce?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-01/day-004/`

Your submission should include:
- `text_analyzer.py` containing your solution to the daily challenge.

## Additional Resources

- [Python Official Docs — String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Python Official Docs — Format String Syntax](https://docs.python.org/3/library/string.html#formatstrings)

## Reflection

- Which string method do you think you will use most often, and why?
- Why is it important that strings are immutable? What problems could arise if they were not?
