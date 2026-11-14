# Week 06 Monday: Clean code, structure, and Git

## Learning objectives

- Explain single responsibility and  naming.
- Apply today's ideas in a small Python program.
- Inspect output and improve the program after a test run.

## Concepts students must understand

- single responsibility
- naming
- Git status
- commit

## Detailed lesson content

Readable code makes change safer. Split input/output from business rules, use names that reveal intent, and commit a coherent small change with a message explaining it.

Before coding, describe the input, processing, and output in ordinary language. Run the smallest possible version, then extend it one change at a time. Read the error message before asking for help.

## Code example

~~~python
def is_passing(score: int) -> bool:
    return score >= 50
~~~

## Practical coding activity

Rename unclear variables in an earlier project.

## Guided exercise

Create a src and tests layout and initialise Git if needed.

## Independent exercise

Refactor one long script into focused functions.

## Expected output

A Git status and clean function layout are shown.

## Homework or assignment

Make two descriptive commits.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Relevant retained examples in the repository, where referenced above

