# Week 07 Tuesday: SQLite and CRUD

## Learning objectives

- Explain SQLite and  INSERT.
- Apply today's ideas in a working implementation.
- Test normal and failure behaviour before sharing the result.

## Concepts students must understand

- SQLite
- INSERT
- SELECT
- UPDATE
- DELETE

## Detailed lesson content

SQLite is a file-based relational database, ideal for local learning and prototypes. Parameterised queries keep values separate from SQL and protect against injection.

Plan input, processing, output, and failure behaviour before coding. Make a small working version first; add complexity only after observing correct output.

## Code example

~~~python
import sqlite3
con = sqlite3.connect('school.db')
con.execute('INSERT INTO students(name) VALUES (?)', ('Amina',))
con.commit()
~~~

## Practical coding activity

Create a database and insert two students.

## Guided exercise

Select and print all rows, then update one name.

## Independent exercise

Build menu actions for create, list, update, and delete.

## Expected output

CRUD actions change and display saved data.

## Homework or assignment

Write three SQL queries and their expected results.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Existing retained repository material where relevant

