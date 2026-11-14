# Week 08 Tuesday: FastAPI routes and parameters

## Learning objectives

- Explain FastAPI and  route.
- Apply today's ideas in a working implementation.
- Test normal and failure behaviour before sharing the result.

## Concepts students must understand

- FastAPI
- route
- path parameter
- query parameter
- uvicorn

## Detailed lesson content

FastAPI maps a URL and method to a Python function. Keep handlers small and return structured data. Use path parameters to identify a resource and query parameters to modify a listing.

Plan input, processing, output, and failure behaviour before coding. Make a small working version first; add complexity only after observing correct output.

## Code example

~~~python
from fastapi import FastAPI
app = FastAPI()
@app.get('/students/{student_id}')
def get_student(student_id: int):
    return {'id': student_id}
~~~

## Practical coding activity

Run a hello FastAPI app locally.

## Guided exercise

Add a list endpoint with a limit query parameter.

## Independent exercise

Create GET endpoints for a student resource.

## Expected output

Interactive docs show the route.

## Homework or assignment

Run uvicorn and test one endpoint in the docs UI.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Existing retained repository material where relevant

