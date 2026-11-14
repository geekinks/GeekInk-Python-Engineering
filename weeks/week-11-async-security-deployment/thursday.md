# Week 11 Thursday: Docker and deployment concepts

## Learning objectives

- Explain container and  image.
- Apply today's ideas in a working implementation.
- Test normal and failure behaviour before sharing the result.

## Concepts students must understand

- container
- image
- Dockerfile
- port
- environment

## Detailed lesson content

A container packages an application and its runtime, not production secrets. Build small images, expose the required port, pass configuration at runtime, and test the image locally before choosing a hosting platform.

Plan input, processing, output, and failure behaviour before coding. Make a small working version first; add complexity only after observing correct output.

## Code example

~~~python
FROM python:3.12-slim
WORKDIR /app
COPY . .
CMD ['python', 'main.py']
~~~

## Practical coding activity

Write a Dockerfile outline for a simple app.

## Guided exercise

List files that should be excluded with .dockerignore.

## Independent exercise

Containerise the API or create a detailed local build plan.

## Expected output

The container starts and serves a health response.

## Homework or assignment

Document build, run, and stop commands.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Existing retained repository material where relevant

