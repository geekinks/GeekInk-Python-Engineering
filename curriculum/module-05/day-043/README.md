# Day 043: Regular Expressions

## Learning Objectives

- Understand what regular expressions are and when to use them.
- Use the `re` module to search, match, and extract patterns from text.
- Write patterns using character classes, quantifiers, and groups.
- Apply `re.sub()` to find and replace text based on patterns.
- Build a log file parser that extracts structured data from unstructured text.

## Introduction

Regular expressions (often shortened to "regex") are a powerful language for describing text patterns. When you need to find all email addresses in a document, validate that a phone number has the right format, or extract dates from log files, regex is the right tool.

Python provides the `re` module for working with regular expressions. While regex syntax can look intimidating at first, the core concepts are simple: you describe what a piece of text looks like using special characters, and the regex engine finds all text that matches your description.

Learning regex is an investment that pays off across your entire career. Every programming language supports them, and they appear everywhere: text editors, command-line tools, databases, and web frameworks all use regular expressions for pattern matching.

## Concepts

### Core `re` Functions

- `re.match(pattern, string)` -- matches only at the beginning of the string.
- `re.search(pattern, string)` -- finds the first match anywhere in the string.
- `re.findall(pattern, string)` -- returns all non-overlapping matches as a list.
- `re.sub(pattern, replacement, string)` -- replaces all matches with the replacement.
- `re.split(pattern, string)` -- splits the string at each match.

### Pattern Syntax

| Pattern   | Meaning                                   |
|-----------|-------------------------------------------|
| `.`       | Any character except newline              |
| `\d`      | Any digit (0-9)                           |
| `\w`      | Any word character (letter, digit, `_`)   |
| `\s`      | Any whitespace (space, tab, newline)      |
| `^`       | Start of string                           |
| `$`       | End of string                             |
| `*`       | Zero or more of the preceding             |
| `+`       | One or more of the preceding              |
| `?`       | Zero or one of the preceding              |
| `{n}`     | Exactly n of the preceding                |
| `{n,m}`   | Between n and m of the preceding          |
| `[abc]`   | Any one of a, b, or c                     |
| `[^abc]`  | Any character except a, b, or c           |
| `(...)` | A capturing group                          |
| `\|`      | OR operator                               |

### Raw Strings

Always use raw strings (`r"..."`) for regex patterns to avoid conflicts between Python's backslash escaping and regex backslash escaping.

## Practical Examples

```python
import re

# Basic matching
text = "My phone number is 080-1234-5678"

# Search for a phone pattern
match = re.search(r"\d{3}-\d{4}-\d{4}", text)
if match:
    print(f"Found phone number: {match.group()}")
# Output: Found phone number: 080-1234-5678
```

```python
import re

# findall -- extract all email addresses from text
text = """
Contact us at support@geekink.com or info@geekink.com.
Students can reach admin@school.edu.ng for enrollment.
"""

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
for email in emails:
    print(f"  Found: {email}")
```

```python
import re

# Groups -- extract parts of a match
date_text = "The event is on 2025-03-15 and ends on 2025-03-17."

for match in re.finditer(r"(\d{4})-(\d{2})-(\d{2})", date_text):
    year, month, day = match.groups()
    print(f"  Date: {day}/{month}/{year}")
# Output:
#   Date: 15/03/2025
#   Date: 17/03/2025
```

```python
import re

# sub -- find and replace
text = "Call 080-1111-2222 or 090-3333-4444 for info."

# Redact phone numbers
redacted = re.sub(r"\d{3}-\d{4}-\d{4}", "[REDACTED]", text)
print(redacted)
# Output: Call [REDACTED] or [REDACTED] for info.
```

## Guided Practice

Write a script that validates common data formats:

```python
import re


def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def validate_phone_ng(phone):
    """Validate Nigerian phone number format: 0XX-XXXX-XXXX or 0XXXXXXXXXX"""
    pattern = r"^0\d{2}-?\d{4}-?\d{4}$"
    return bool(re.match(pattern, phone))


def validate_date(date_str):
    """Validate date in YYYY-MM-DD format (basic structure check)"""
    pattern = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"
    return bool(re.match(pattern, date_str))


# Test the validators
test_data = {
    "emails": ["user@example.com", "bad@", "test@site.ng", "@missing.com"],
    "phones": ["080-1234-5678", "09012345678", "123-456", "0801234567890"],
    "dates": ["2025-03-15", "2025-13-01", "2025-00-10", "2025-12-31"],
}

print("Email Validation:")
for email in test_data["emails"]:
    status = "valid" if validate_email(email) else "invalid"
    print(f"  {email:<25} -> {status}")

print("\nPhone Validation:")
for phone in test_data["phones"]:
    status = "valid" if validate_phone_ng(phone) else "invalid"
    print(f"  {phone:<25} -> {status}")

print("\nDate Validation:")
for date in test_data["dates"]:
    status = "valid" if validate_date(date) else "invalid"
    print(f"  {date:<25} -> {status}")
```

## Daily Challenge

**Build a Log File Parser**

Write a script called `log_parser.py` that processes a server log file and extracts structured information.

First, create a sample log file (`sample.log`) with content like:

```
2025-03-15 08:23:41 INFO 192.168.1.10 User login successful
2025-03-15 08:24:02 ERROR 192.168.1.15 Database connection failed: timeout after 30s
2025-03-15 08:25:11 WARNING 10.0.0.5 Disk usage at 85%
2025-03-15 08:26:33 INFO 192.168.1.10 File uploaded: report_q1.pdf
2025-03-15 08:27:45 ERROR 172.16.0.20 Authentication failed for user admin
2025-03-15 08:28:59 INFO 192.168.1.22 User logout
2025-03-15 08:30:10 ERROR 192.168.1.15 Database connection failed: max retries exceeded
```

Your script should:

1. Read the log file.
2. Use regex to extract: timestamp, log level (INFO/WARNING/ERROR), IP address, and message.
3. Count occurrences of each log level.
4. List all unique IP addresses.
5. Display all ERROR messages with their timestamps.
6. Print a summary report.

Requirements:
- Use named groups in your regex: `(?P<name>...)`.
- Handle lines that do not match the expected format gracefully.

## Expected Output

```
Log File Analysis: sample.log
================================

Log Level Summary:
  INFO:    3
  WARNING: 1
  ERROR:   3

Unique IP Addresses:
  192.168.1.10
  192.168.1.15
  10.0.0.5
  172.16.0.20
  192.168.1.22

Error Messages:
  [2025-03-15 08:24:02] 192.168.1.15 - Database connection failed: timeout after 30s
  [2025-03-15 08:27:45] 172.16.0.20 - Authentication failed for user admin
  [2025-03-15 08:30:10] 192.168.1.15 - Database connection failed: max retries exceeded
```

## Assessment

1. What is the difference between `re.match()` and `re.search()`?
2. Why should you use raw strings (`r"..."`) when writing regex patterns in Python?
3. What does the regex pattern `(\d{1,3}\.){3}\d{1,3}` match? Is it a complete IP address validator? Why or why not?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-05/day-043/`

Include `log_parser.py`, `sample.log`, and a `README.md`.

## Additional Resources

- [re module documentation](https://docs.python.org/3/library/re.html)
- [Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)

## Reflection

- When is regex the right tool, and when should you use simpler string methods like `split()` or `startswith()` instead?
- What challenges did you face writing the log-parsing pattern? How did you debug it?
