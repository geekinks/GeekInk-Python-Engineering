# Week 08 Monday: HTTP, REST, and JSON

## Learning objectives

- Explain HTTP and  request.
- Apply today's ideas in a working implementation.
- Test normal and failure behaviour before sharing the result.

## Concepts students must understand

- HTTP
- request
- response
- method
- status code
- JSON

## Detailed lesson content

HTTP carries requests and responses. REST-style APIs use resource URLs and methods deliberately: GET reads, POST creates, PUT/PATCH changes, DELETE removes. JSON is a data format, not a database.

Plan input, processing, output, and failure behaviour before coding. Make a small working version first; add complexity only after observing correct output.

## Code example

~~~python
import json
print(json.dumps({'status': 'ok'}))
~~~

## Practical coding activity

Identify method and status code for four scenarios.

## Guided exercise

Use requests only after explaining the endpoint and response shape.

## Independent exercise

Describe endpoints for students and courses.

## Expected output

A resource map names URLs, methods, and responses.

## Homework or assignment

Read HTTP status-code documentation.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Existing retained repository material where relevant

