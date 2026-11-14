# Week 09 Wednesday: Authentication and authorisation concepts

## Learning objectives

- Explain hash and  token.
- Apply today's ideas in a working implementation.
- Test normal and failure behaviour before sharing the result.

## Concepts students must understand

- hash
- token
- JWT
- role
- least privilege

## Detailed lesson content

Authentication proves identity; authorisation decides what an identity may do. Store password hashes, never passwords. JWTs are signed credentials with expiry, not encrypted user databases.

Plan input, processing, output, and failure behaviour before coding. Make a small working version first; add complexity only after observing correct output.

## Code example

~~~python
from hashlib import sha256
print(sha256(b'demo-only').hexdigest())
~~~

## Practical coding activity

Explain why the example hash is not a production password solution.

## Guided exercise

Map learner, instructor, and admin permissions.

## Independent exercise

Protect one conceptual endpoint using a role check.

## Expected output

Unauthorised requests receive a clear response.

## Homework or assignment

Research a production password-hashing library before using one.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Existing retained repository material where relevant

