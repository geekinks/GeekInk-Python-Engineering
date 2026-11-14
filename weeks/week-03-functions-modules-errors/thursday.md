# Week 03 Thursday: Exceptions and custom errors

## Learning objectives

- Explain try and  except.
- Apply today's ideas in a small Python program.
- Inspect output and improve the program after a test run.

## Concepts students must understand

- try
- except
- else
- finally
- raise

## Detailed lesson content

Exceptions separate expected bad input from normal behaviour. Catch specific exceptions, give a helpful message, and never hide unexpected failures with a bare except.

Before coding, describe the input, processing, and output in ordinary language. Run the smallest possible version, then extend it one change at a time. Read the error message before asking for help.

## Code example

~~~python
try:
    score = int(input('Score: '))
except ValueError:
    print('Enter a whole number.')
~~~

## Practical coding activity

Wrap numeric score input safely.

## Guided exercise

Raise ValueError when score is outside 0-100.

## Independent exercise

Add safe input and clear messages to the student manager.

## Expected output

Invalid input produces a message instead of a crash.

## Homework or assignment

Add one documented custom validation rule.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Relevant retained examples in the repository, where referenced above

