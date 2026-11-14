# Week 08 Friday: API demonstration and review

## Learning objectives

- Explain OpenAPI and  contract.
- Apply today's ideas in a working implementation.
- Test normal and failure behaviour before sharing the result.

## Concepts students must understand

- OpenAPI
- contract
- manual test
- reflection

## Detailed lesson content

FastAPI generates API documentation from the code. Demonstrate every endpoint, then review input validation, status codes, response consistency, and one failure case.

Plan input, processing, output, and failure behaviour before coding. Make a small working version first; add complexity only after observing correct output.

## Code example

~~~python
@app.get('/health')
def health(): return {'status': 'ok'}
~~~

## Practical coding activity

Add a health endpoint.

## Guided exercise

Peer-test a route using the generated documentation.

## Independent exercise

Submit the student management REST API.

## Expected output

Docs UI lists a working CRUD surface.

## Homework or assignment

Capture a short test checklist and reflection.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Existing retained repository material where relevant

