# Week 03 Tuesday: Arguments, scope, and lambda

## Learning objectives

- Explain positional and  keyword.
- Apply today's ideas in a small Python program.
- Inspect output and improve the program after a test run.

## Concepts students must understand

- positional
- keyword
- default
- local scope
- lambda

## Detailed lesson content

Use defaults for genuinely optional values and keyword arguments for clarity. A local variable only exists while its function runs. Lambdas suit a tiny one-expression transformation, not complex logic.

Before coding, describe the input, processing, and output in ordinary language. Run the smallest possible version, then extend it one change at a time. Read the error message before asking for help.

## Code example

~~~python
def welcome(name, course='Python'):
    return f'Welcome {name} to {course}'
print(welcome('Zainab'))
~~~

## Practical coding activity

Call a function with positional, keyword, and default values.

## Guided exercise

Show why a variable created inside a function cannot be used outside it.

## Independent exercise

Add configurable passing score to your grading functions.

## Expected output

Calls produce personalised messages.

## Homework or assignment

Write two tests by hand: input and expected return value.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Relevant retained examples in the repository, where referenced above

