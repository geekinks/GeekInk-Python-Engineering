# Week 07 Friday: Database project review

## Learning objectives

- Explain normalisation and  constraints.
- Apply today's ideas in a working implementation.
- Test normal and failure behaviour before sharing the result.

## Concepts students must understand

- normalisation
- constraints
- migration plan
- review

## Detailed lesson content

Demonstrate CRUD and a relationship report. Review constraints, transaction boundaries, meaningful errors, and backups. Do not store passwords in plain text.

Plan input, processing, output, and failure behaviour before coding. Make a small working version first; add complexity only after observing correct output.

## Code example

~~~python
con.execute('SELECT COUNT(*) FROM students')
print(con.fetchone()[0])
~~~

## Practical coding activity

Add a count or filtered query.

## Guided exercise

Review whether each fact is stored once.

## Independent exercise

Submit the database-backed records app.

## Expected output

Records persist after restarting the program.

## Homework or assignment

Write backup and restore steps.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Existing retained repository material where relevant

