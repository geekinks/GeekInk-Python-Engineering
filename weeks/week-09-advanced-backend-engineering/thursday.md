# Week 09 Thursday: Middleware, security, pagination, and tasks

## Learning objectives

- Explain middleware and  CORS.
- Apply today's ideas in a working implementation.
- Test normal and failure behaviour before sharing the result.

## Concepts students must understand

- middleware
- CORS
- pagination
- background task
- rate limit

## Detailed lesson content

Middleware surrounds requests for cross-cutting concerns such as logging or headers. Limit list results, validate every input, use least privilege, and avoid long work in a request handler.

Plan input, processing, output, and failure behaviour before coding. Make a small working version first; add complexity only after observing correct output.

## Code example

~~~python
from fastapi import Query
@app.get('/students')
def list_students(limit: int = Query(20, le=100)):
    return {'limit': limit}
~~~

## Practical coding activity

Add bounded pagination parameters.

## Guided exercise

Add request logging without sensitive values.

## Independent exercise

Build filtering, configuration, and one role-protected feature.

## Expected output

Lists return bounded, predictable pages.

## Homework or assignment

Create a security checklist for the API.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Existing retained repository material where relevant

