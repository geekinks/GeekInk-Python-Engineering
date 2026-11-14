# Week 04 Wednesday: Dates, regular expressions, and standard library

## Learning objectives

- Explain datetime and  regex.
- Apply today's ideas in a small Python program.
- Inspect output and improve the program after a test run.

## Concepts students must understand

- datetime
- regex
- match
- standard library

## Detailed lesson content

datetime represents dates and times without manual string arithmetic. Regular expressions are precise pattern tools; start with small patterns and verify every match.

Before coding, describe the input, processing, and output in ordinary language. Run the smallest possible version, then extend it one change at a time. Read the error message before asking for help.

## Code example

~~~python
from datetime import date
print(date.today().isoformat())
~~~

## Practical coding activity

Add an ISO date to a record.

## Guided exercise

Use a simple pattern to validate a school email shape.

## Independent exercise

Create a search that finds records by name prefix.

## Expected output

A valid date and matching records display.

## Homework or assignment

Read pathlib and datetime documentation examples.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Relevant retained examples in the repository, where referenced above

