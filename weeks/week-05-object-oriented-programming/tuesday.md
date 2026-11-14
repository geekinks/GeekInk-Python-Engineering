# Week 05 Tuesday: Methods, attributes, and dataclasses

## Learning objectives

- Explain instance method and  class attribute.
- Apply today's ideas in a small Python program.
- Inspect output and improve the program after a test run.

## Concepts students must understand

- instance method
- class attribute
- dataclass
- type hint

## Detailed lesson content

Methods act on an object's own state. Type hints communicate intended values, while dataclasses reduce boilerplate for simple data containers.

Before coding, describe the input, processing, and output in ordinary language. Run the smallest possible version, then extend it one change at a time. Read the error message before asking for help.

## Code example

~~~python
from dataclasses import dataclass
@dataclass
class Course:
    code: str
    title: str
~~~

## Practical coding activity

Add an enrol method to Student.

## Guided exercise

Add type hints to a result calculation method.

## Independent exercise

Create dataclasses for course and attendance.

## Expected output

Object methods produce a useful message.

## Homework or assignment

Complete a retained OOP starter exercise.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Relevant retained examples in the repository, where referenced above

