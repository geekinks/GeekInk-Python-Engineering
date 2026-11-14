# Week 05 Friday: OOP design review

## Learning objectives

- Explain responsibility and  composition.
- Apply today's ideas in a small Python program.
- Inspect output and improve the program after a test run.

## Concepts students must understand

- responsibility
- composition
- classmethod
- staticmethod

## Detailed lesson content

Demonstrate the school model and explain responsibility boundaries. Use class or static methods only when they fit the model; do not use OOP merely to make code longer.

Before coding, describe the input, processing, and output in ordinary language. Run the smallest possible version, then extend it one change at a time. Read the error message before asking for help.

## Code example

~~~python
class Student:
    total = 0
    def __init__(self, name):
        self.name = name
        Student.total += 1
~~~

## Practical coding activity

Create multiple students and report the class total.

## Guided exercise

Review whether each class has one main reason to change.

## Independent exercise

Submit the OOP school management system.

## Expected output

A documented model validates data and shows relationships.

## Homework or assignment

Run or study retained student-management tests.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Relevant retained examples in the repository, where referenced above

