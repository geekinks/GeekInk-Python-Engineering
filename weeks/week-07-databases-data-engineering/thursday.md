# Week 07 Thursday: PostgreSQL and SQLAlchemy fundamentals

## Learning objectives

- Explain PostgreSQL and  connection string.
- Apply today's ideas in a working implementation.
- Test normal and failure behaviour before sharing the result.

## Concepts students must understand

- PostgreSQL
- connection string
- ORM
- model

## Detailed lesson content

PostgreSQL is a common production database server. An ORM maps tables to Python classes, but understanding the generated data model and SQL remains essential.

Plan input, processing, output, and failure behaviour before coding. Make a small working version first; add complexity only after observing correct output.

## Code example

~~~python
from sqlalchemy.orm import DeclarativeBase
class Base(DeclarativeBase):
    pass
~~~

## Practical coding activity

Create a SQLAlchemy model outline for Student.

## Guided exercise

Compare an ORM create operation with INSERT SQL.

## Independent exercise

Connect the records design to SQLAlchemy or document a PostgreSQL migration plan.

## Expected output

A model has typed columns and a primary key.

## Homework or assignment

Install only required dependencies inside a virtual environment.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Existing retained repository material where relevant

