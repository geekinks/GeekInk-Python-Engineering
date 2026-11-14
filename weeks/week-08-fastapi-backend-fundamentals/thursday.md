# Week 08 Thursday: CRUD API implementation

## Learning objectives

- Explain POST and  PUT.
- Apply today's ideas in a working implementation.
- Test normal and failure behaviour before sharing the result.

## Concepts students must understand

- POST
- PUT
- DELETE
- HTTPException

## Detailed lesson content

Build each CRUD action around an explicit data rule. Return suitable status codes and never claim success when an item does not exist. Start with an in-memory list before adding a database.

Plan input, processing, output, and failure behaviour before coding. Make a small working version first; add complexity only after observing correct output.

## Code example

~~~python
from fastapi import HTTPException
if student_id not in students:
    raise HTTPException(status_code=404, detail='Student not found')
~~~

## Practical coding activity

Implement create and list endpoints.

## Guided exercise

Add get, update, and delete with 404 handling.

## Independent exercise

Build the week's CRUD student API.

## Expected output

Each endpoint has a testable JSON response.

## Homework or assignment

Write an API usage example in README.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Existing retained repository material where relevant

