# Week 11 Monday: Async and concurrency fundamentals

## Learning objectives

- Explain sync and  async.
- Apply today's ideas in a working implementation.
- Test normal and failure behaviour before sharing the result.

## Concepts students must understand

- sync
- async
- await
- event loop
- I/O bound

## Detailed lesson content

Synchronous code completes one task before the next. Async is most useful when waiting for I/O; it is not automatically faster for CPU-heavy work. Keep async code readable and avoid blocking calls inside it.

Plan input, processing, output, and failure behaviour before coding. Make a small working version first; add complexity only after observing correct output.

## Code example

~~~python
import asyncio
async def greet():
    await asyncio.sleep(0.1)
    return 'ready'
print(asyncio.run(greet()))
~~~

## Practical coding activity

Run an async greeting.

## Guided exercise

Compare a sequential and concurrent waiting example conceptually.

## Independent exercise

Identify I/O-bound work in an API.

## Expected output

The coroutine returns ready.

## Homework or assignment

Explain when ordinary functions remain the best choice.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Existing retained repository material where relevant

