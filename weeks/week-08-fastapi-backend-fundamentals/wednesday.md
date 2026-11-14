# Week 08 Wednesday: Pydantic validation and errors

## Learning objectives

- Explain Pydantic and  request model.
- Apply today's ideas in a working implementation.
- Test normal and failure behaviour before sharing the result.

## Concepts students must understand

- Pydantic
- request model
- response model
- validation

## Detailed lesson content

Validation makes an API boundary trustworthy. Declare the expected fields and types, then return clear HTTP errors for missing resources or invalid state.

Plan input, processing, output, and failure behaviour before coding. Make a small working version first; add complexity only after observing correct output.

## Code example

~~~python
from pydantic import BaseModel
class StudentIn(BaseModel):
    name: str
    age: int
~~~

## Practical coding activity

Create a request model with a constrained field.

## Guided exercise

Send valid and invalid bodies through the docs UI.

## Independent exercise

Add validation to the student create endpoint.

## Expected output

Invalid data returns a useful validation response.

## Homework or assignment

List three inputs the API must reject.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Existing retained repository material where relevant

