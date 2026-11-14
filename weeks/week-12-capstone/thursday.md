# Week 12 Thursday: Testing, documentation, security, and deployment

## Learning objectives

- Explain acceptance test and  README.
- Apply today's ideas in a working implementation.
- Test normal and failure behaviour before sharing the result.

## Concepts students must understand

- acceptance test
- README
- threat review
- deploy

## Detailed lesson content

Verify acceptance criteria with tests and manual checks. Document setup, configuration, API use, and limitations. Review validation, permissions, secrets, dependencies, and backups before deployment.

Plan input, processing, output, and failure behaviour before coding. Make a small working version first; add complexity only after observing correct output.

## Code example

~~~python
def test_health(client):
    assert client.get('/health').status_code == 200
~~~

## Practical coding activity

Write a test for one acceptance criterion.

## Guided exercise

Write setup and run instructions for a new developer.

## Independent exercise

Complete security review and deploy or document a reproducible deployment plan.

## Expected output

Tests and documentation support a clean setup.

## Homework or assignment

Prepare a five-minute demonstration script.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Existing retained repository material where relevant

