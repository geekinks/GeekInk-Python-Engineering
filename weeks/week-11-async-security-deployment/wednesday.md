# Week 11 Wednesday: API testing and monitoring

## Learning objectives

- Explain TestClient and  integration test.
- Apply today's ideas in a working implementation.
- Test normal and failure behaviour before sharing the result.

## Concepts students must understand

- TestClient
- integration test
- health check
- metric

## Detailed lesson content

Integration tests exercise components together, such as a route and database fixture. Monitoring starts with structured logs, a health check, and a useful error signal; it must not expose private data.

Plan input, processing, output, and failure behaviour before coding. Make a small working version first; add complexity only after observing correct output.

## Code example

~~~python
from fastapi.testclient import TestClient
# client = TestClient(app)
# assert client.get('/health').status_code == 200
~~~

## Practical coding activity

Write a health endpoint test.

## Guided exercise

Test one successful and one invalid request.

## Independent exercise

Add request identifiers or safe structured logging.

## Expected output

Tests prove expected API behaviour.

## Homework or assignment

Define what an unhealthy service means.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Existing retained repository material where relevant

