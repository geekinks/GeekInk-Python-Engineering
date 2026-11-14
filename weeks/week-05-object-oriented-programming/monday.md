# Week 05 Monday: Classes and objects

## Learning objectives

- Explain class and  instance.
- Apply today's ideas in a small Python program.
- Inspect output and improve the program after a test run.

## Concepts students must understand

- class
- instance
- constructor
- state

## Detailed lesson content

A class is a blueprint; an object is one concrete thing with state and behaviour. Start with a small model and avoid putting unrelated work in one class.

Before coding, describe the input, processing, and output in ordinary language. Run the smallest possible version, then extend it one change at a time. Read the error message before asking for help.

## Code example

~~~python
class Student:
    def __init__(self, name):
        self.name = name

print(Student('Ada').name)
~~~

## Practical coding activity

Create Student objects with name and identifier.

## Guided exercise

Add a Course class and print object state.

## Independent exercise

Model one learner and one course.

## Expected output

Two objects preserve different values.

## Homework or assignment

Read python-oop/lectures/02-classes-and-objects.md.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Relevant retained examples in the repository, where referenced above

