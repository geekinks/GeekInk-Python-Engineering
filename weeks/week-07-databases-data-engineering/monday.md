# Week 07 Monday: Relational data modelling and SQL

## Learning objectives

- Explain table and  row.
- Apply today's ideas in a working implementation.
- Test normal and failure behaviour before sharing the result.

## Concepts students must understand

- table
- row
- primary key
- foreign key
- schema

## Detailed lesson content

A database stores facts reliably beyond one program run. Model entities first, then relationships. A primary key identifies a row; a foreign key connects it to another table.

Plan input, processing, output, and failure behaviour before coding. Make a small working version first; add complexity only after observing correct output.

## Code example

~~~python
CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT NOT NULL);
~~~

## Practical coding activity

Draw student, course, and enrolment entities.

## Guided exercise

Write CREATE TABLE statements for student and course.

## Independent exercise

Design a schema for a small library.

## Expected output

A schema identifies tables, keys, and relationships.

## Homework or assignment

Read an existing project and list its persistent data.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Existing retained repository material where relevant

