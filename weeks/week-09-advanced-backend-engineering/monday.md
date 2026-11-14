# Week 09 Monday: FastAPI database integration

## Learning objectives

- Explain session and  repository.
- Apply today's ideas in a working implementation.
- Test normal and failure behaviour before sharing the result.

## Concepts students must understand

- session
- repository
- dependency
- PostgreSQL

## Detailed lesson content

Keep database access separate from HTTP concerns. A session is a unit of database work; dependency injection makes it explicit and testable. Use PostgreSQL for shared production data.

Plan input, processing, output, and failure behaviour before coding. Make a small working version first; add complexity only after observing correct output.

## Code example

~~~python
from sqlalchemy.orm import Session
def get_db():
    # yield one session per request
    yield
~~~

## Practical coding activity

Identify the boundary between route, service, and database code.

## Guided exercise

Add a repository function that lists students.

## Independent exercise

Connect an API endpoint to a database-backed model.

## Expected output

A route returns persisted records.

## Homework or assignment

Document local database setup without sharing credentials.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Existing retained repository material where relevant

