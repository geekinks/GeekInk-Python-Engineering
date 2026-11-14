# Week 12 Wednesday: Implementation sprint

## Learning objectives

- Explain MVP and  task breakdown.
- Apply today's ideas in a working implementation.
- Test normal and failure behaviour before sharing the result.

## Concepts students must understand

- MVP
- task breakdown
- incremental delivery
- Git

## Detailed lesson content

Build a vertical slice: one user action working end-to-end. Keep tasks small, commit working checkpoints, and choose reliability over extra features. Ask for feedback while changes are cheap.

Plan input, processing, output, and failure behaviour before coding. Make a small working version first; add complexity only after observing correct output.

## Code example

~~~python
def health():
    return {'status': 'ok'}
~~~

## Practical coding activity

Create tasks for model, rule, route, test, and documentation.

## Guided exercise

Implement the highest-risk path first.

## Independent exercise

Build the core capstone feature.

## Expected output

A demonstrable slice runs locally.

## Homework or assignment

Commit a working baseline and update the task board.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Existing retained repository material where relevant

