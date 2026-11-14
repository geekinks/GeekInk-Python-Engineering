# Week 03 Monday: Defining useful functions

## Learning objectives

- Explain function and  parameter.
- Apply today's ideas in a small Python program.
- Inspect output and improve the program after a test run.

## Concepts students must understand

- function
- parameter
- return
- docstring

## Detailed lesson content

Functions name a single responsibility. Inputs belong in parameters and results should be returned rather than hidden in print statements where later code cannot reuse them.

Before coding, describe the input, processing, and output in ordinary language. Run the smallest possible version, then extend it one change at a time. Read the error message before asking for help.

## Code example

~~~python
def calculate_grade(score):
    return 'Pass' if score >= 50 else 'Retry'

print(calculate_grade(67))
~~~

## Practical coding activity

Extract grade logic from last week into a function.

## Guided exercise

Write a function that returns a formatted student name.

## Independent exercise

Create three small functions for a calculator.

## Expected output

A function call returns the expected value.

## Homework or assignment

Add docstrings to each calculator function.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Relevant retained examples in the repository, where referenced above

