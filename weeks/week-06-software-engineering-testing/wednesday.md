# Week 06 Wednesday: Unit testing with pytest

## Learning objectives

- Explain assert and  unit test.
- Apply today's ideas in a small Python program.
- Inspect output and improve the program after a test run.

## Concepts students must understand

- assert
- unit test
- arrange-act-assert
- pytest

## Detailed lesson content

A unit test checks one behaviour at a time. Tests should be deterministic and describe what matters, not implementation details.

Before coding, describe the input, processing, and output in ordinary language. Run the smallest possible version, then extend it one change at a time. Read the error message before asking for help.

## Code example

~~~python
def test_passing_score():
    assert is_passing(50) is True
~~~

## Practical coding activity

Write tests for pass, fail, and boundary scores.

## Guided exercise

Run pytest and fix a deliberately failing test.

## Independent exercise

Add tests to the student manager.

## Expected output

Tests pass and show clear test names.

## Homework or assignment

Add one test for invalid input.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Relevant retained examples in the repository, where referenced above

