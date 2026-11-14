# Week 07 Wednesday: Relationships and transactions

## Learning objectives

- Explain one-to-many and  many-to-many.
- Apply today's ideas in a working implementation.
- Test normal and failure behaviour before sharing the result.

## Concepts students must understand

- one-to-many
- many-to-many
- JOIN
- transaction

## Detailed lesson content

Relationships reduce duplication. Use a join table for many-to-many enrolments. A transaction groups changes so partial work does not leave data inconsistent.

Plan input, processing, output, and failure behaviour before coding. Make a small working version first; add complexity only after observing correct output.

## Code example

~~~python
SELECT s.name, c.title FROM students s
JOIN enrolments e ON e.student_id = s.id
JOIN courses c ON c.id = e.course_id;
~~~

## Practical coding activity

Create enrolment table with foreign keys.

## Guided exercise

Run a join that shows enrolled students and courses.

## Independent exercise

Wrap two related inserts in a transaction.

## Expected output

A joined report shows related records.

## Homework or assignment

Draw the final database schema.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Existing retained repository material where relevant

