# Week 06 Thursday: Fixtures, mocks, formatting, and quality

## Learning objectives

- Explain fixture and  mock.
- Apply today's ideas in a small Python program.
- Inspect output and improve the program after a test run.

## Concepts students must understand

- fixture
- mock
- formatter
- linter
- dependency

## Detailed lesson content

Fixtures prepare repeatable data. Mock external boundaries such as files or HTTP only when a real dependency would make a test slow or unreliable. Format consistently before review.

Before coding, describe the input, processing, and output in ordinary language. Run the smallest possible version, then extend it one change at a time. Read the error message before asking for help.

## Code example

~~~python
import pytest
@pytest.fixture
def scores():
    return [50, 70]
~~~

## Practical coding activity

Use a fixture for shared score data.

## Guided exercise

Sketch a mock boundary for a file loader.

## Independent exercise

Format and review the refactored project.

## Expected output

Tests run from a clean command.

## Homework or assignment

Add development dependencies and commands to README.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Relevant retained examples in the repository, where referenced above

