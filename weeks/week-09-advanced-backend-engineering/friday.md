# Week 09 Friday: Secure API review

## Learning objectives

- Explain threat model and  audit.
- Apply today's ideas in a working implementation.
- Test normal and failure behaviour before sharing the result.

## Concepts students must understand

- threat model
- audit
- error response
- review

## Detailed lesson content

Demonstrate persistent CRUD, configuration, and an authentication flow concept. Review common threats: weak validation, leaked secrets, overbroad roles, verbose errors, and untested permissions.

Plan input, processing, output, and failure behaviour before coding. Make a small working version first; add complexity only after observing correct output.

## Code example

~~~python
# Never return password hashes or secret settings
~~~

## Practical coding activity

Test an unauthorised and authorised path.

## Guided exercise

Peer-review endpoints against the security checklist.

## Independent exercise

Submit the secure learning-platform API increment.

## Expected output

Sensitive fields never appear in responses.

## Homework or assignment

Write a prioritised remediation list.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Existing retained repository material where relevant

