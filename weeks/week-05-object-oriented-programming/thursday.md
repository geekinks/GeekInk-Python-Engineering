# Week 05 Thursday: Inheritance, composition, and polymorphism

## Learning objectives

- Explain inheritance and  base class.
- Apply today's ideas in a small Python program.
- Inspect output and improve the program after a test run.

## Concepts students must understand

- inheritance
- base class
- composition
- interface

## Detailed lesson content

Use inheritance for a genuine is-a relationship; use composition when one object owns or uses another. Polymorphism lets different objects offer the same operation.

Before coding, describe the input, processing, and output in ordinary language. Run the smallest possible version, then extend it one change at a time. Read the error message before asking for help.

## Code example

~~~python
class User:
    def describe(self): return 'user'
class Lecturer(User):
    def describe(self): return 'lecturer'
~~~

## Practical coding activity

Create Student and Lecturer subclasses.

## Guided exercise

Add a Course that contains enrolled students.

## Independent exercise

Implement a report that calls describe on different user types.

## Expected output

Different roles respond through the same method.

## Homework or assignment

Read the retained composition and polymorphism exercises.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Relevant retained examples in the repository, where referenced above

