# Week 05 Wednesday: Encapsulation and properties

## Learning objectives

- Explain private convention and  property.
- Apply today's ideas in a small Python program.
- Inspect output and improve the program after a test run.

## Concepts students must understand

- private convention
- property
- validation
- invariant

## Detailed lesson content

Encapsulation protects valid state. Python uses a naming convention for internal fields and properties for controlled access; validate important rules at the boundary.

Before coding, describe the input, processing, and output in ordinary language. Run the smallest possible version, then extend it one change at a time. Read the error message before asking for help.

## Code example

~~~python
class Result:
    def __init__(self, score):
        self.score = score
    @property
    def score(self): return self._score
    @score.setter
    def score(self, value):
        if not 0 <= value <= 100: raise ValueError('0-100')
        self._score = value
~~~

## Practical coding activity

Validate a score with a property.

## Guided exercise

Explain the difference between a field and a behaviour.

## Independent exercise

Add safe score updates to the school model.

## Expected output

Invalid scores are rejected with a clear message.

## Homework or assignment

Use python-oop/exercises/05-encapsulation.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Relevant retained examples in the repository, where referenced above

