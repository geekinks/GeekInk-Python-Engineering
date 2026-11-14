# Week 03 Wednesday: Comprehensions, modules, and imports

## Learning objectives

- Explain list comprehension and  dictionary comprehension.
- Apply today's ideas in a small Python program.
- Inspect output and improve the program after a test run.

## Concepts students must understand

- list comprehension
- dictionary comprehension
- module
- import

## Detailed lesson content

A comprehension expresses a simple transform or filter in one readable line. Put related functions in a module and import only what a caller needs.

Before coding, describe the input, processing, and output in ordinary language. Run the smallest possible version, then extend it one change at a time. Read the error message before asking for help.

## Code example

~~~python
scores = [40, 55, 90]
passed = [score for score in scores if score >= 50]
print(passed)
~~~

## Practical coding activity

Turn a loop that doubles values into a comprehension.

## Guided exercise

Create grades.py and import calculate_grade from it.

## Independent exercise

Create a package-style student_manager folder with __init__.py.

## Expected output

The imported function is called from a separate script.

## Homework or assignment

Read the retained module lesson in curriculum/module-03/day-026.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Relevant retained examples in the repository, where referenced above

