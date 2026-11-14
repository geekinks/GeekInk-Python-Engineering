# Week 09 Tuesday: Migrations and configuration

## Learning objectives

- Explain migration and  environment variable.
- Apply today's ideas in a working implementation.
- Test normal and failure behaviour before sharing the result.

## Concepts students must understand

- migration
- environment variable
- settings
- secret

## Detailed lesson content

Schema changes must be repeatable. Store configuration in environment variables, validate it at start-up, and keep secrets out of source control. Use migration tooling deliberately after understanding the SQL change.

Plan input, processing, output, and failure behaviour before coding. Make a small working version first; add complexity only after observing correct output.

## Code example

~~~python
import os
DATABASE_URL = os.environ.get('DATABASE_URL', '')
~~~

## Practical coding activity

Create a local example environment file without a secret.

## Guided exercise

Describe an additive migration for a new email column.

## Independent exercise

Add settings validation or a configuration checklist.

## Expected output

Missing configuration fails clearly in development.

## Homework or assignment

Add .env to gitignore and .env.example to project.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Existing retained repository material where relevant

