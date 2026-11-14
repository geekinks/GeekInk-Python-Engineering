# Week 11 Tuesday: Performance and application security

## Learning objectives

- Explain profiling and  input validation.
- Apply today's ideas in a working implementation.
- Test normal and failure behaviour before sharing the result.

## Concepts students must understand

- profiling
- input validation
- secret
- dependency

## Detailed lesson content

Measure before optimising. Typical gains come from correct algorithms, database queries, pagination, and caching—not premature complexity. Security starts with validation, updates, secure configuration, and least privilege.

Plan input, processing, output, and failure behaviour before coding. Make a small working version first; add complexity only after observing correct output.

## Code example

~~~python
import time
start = time.perf_counter()
# measured work
print(time.perf_counter() - start)
~~~

## Practical coding activity

Time a small function before changing it.

## Guided exercise

Review validation and secret handling in an API.

## Independent exercise

Create a performance and security observation list.

## Expected output

Measurements and findings are recorded.

## Homework or assignment

Update dependencies only after checking tests.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Existing retained repository material where relevant

