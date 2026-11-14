# Week 12 Tuesday: Architecture, schema, and API design

## Learning objectives

- Explain component and  boundary.
- Apply today's ideas in a working implementation.
- Test normal and failure behaviour before sharing the result.

## Concepts students must understand

- component
- boundary
- schema
- endpoint
- contract

## Detailed lesson content

Design before implementing: identify components, data ownership, failure paths, and deployment boundary. Draw only enough architecture to make decisions. Define an API contract before routes proliferate.

Plan input, processing, output, and failure behaviour before coding. Make a small working version first; add complexity only after observing correct output.

## Code example

~~~python
GET /courses
POST /enrolments
GET /students/{id}
~~~

## Practical coding activity

Draw a context diagram for the chosen problem.

## Guided exercise

Create a relational schema or data model.

## Independent exercise

Write an endpoint table with request, response, and error cases.

## Expected output

Architecture and API design are reviewable.

## Homework or assignment

Choose a minimum viable feature set.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Existing retained repository material where relevant

