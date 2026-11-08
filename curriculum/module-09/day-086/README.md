# Day 086: Logging

## Learning Objectives

- Understand why logging is superior to print statements for production code.
- Use Python's `logging` module with different log levels.
- Configure handlers to direct log output to the console, files, or both.
- Format log messages with timestamps, levels, and module names.
- Add logging to an existing application without changing its behavior.

## Introduction

During development, sprinkling `print()` statements through your code to see what is happening feels natural. But print statements have serious limitations in production: they cannot be turned off without removing them, they all look the same, they cannot be routed to files, and they mix diagnostic output with actual program output.

Python's `logging` module solves every one of these problems. You assign each message a severity level --- DEBUG, INFO, WARNING, ERROR, or CRITICAL --- and configure which levels are shown. You can direct logs to the console, to a file, to a remote server, or to all three simultaneously. Each message is automatically timestamped and tagged with the module that produced it.

Professional applications always use logging. When a production system fails at 3 AM, the log file is the first thing the on-call engineer reads. Good logs tell the story of what happened, step by step, with enough detail to diagnose the problem without needing to reproduce it.

## Concepts

### Log Levels

| Level | Numeric | When to use |
|-------|---------|-------------|
| `DEBUG` | 10 | Detailed diagnostic information for developers |
| `INFO` | 20 | Confirmation that things are working as expected |
| `WARNING` | 30 | Something unexpected, but the program still works |
| `ERROR` | 40 | A serious problem; the program could not do something |
| `CRITICAL` | 50 | A fatal error; the program may not continue |

### Basic Usage

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug("Starting data processing")
logger.info("Processed 150 records successfully")
logger.warning("File 'config.yaml' not found, using defaults")
logger.error("Database connection failed after 3 retries")
logger.critical("System out of memory, shutting down")
```

### Handlers

Handlers determine where log messages go:

- `StreamHandler` --- sends to console (stderr by default)
- `FileHandler` --- writes to a file
- `RotatingFileHandler` --- writes to a file, rotating when it reaches a size limit

### Formatters

Formatters control what each log line looks like:

```python
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
```

Common format fields: `%(asctime)s`, `%(name)s`, `%(levelname)s`, `%(message)s`, `%(filename)s`, `%(lineno)d`, `%(funcName)s`.

## Practical Examples

### Basic configuration

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger("my_app")

logger.info("Application started")
logger.debug("This will NOT appear because level is INFO")
logger.warning("Disk space below 10%%")
```

### Logging to both console and file

```python
import logging

logger = logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(name)s (%(filename)s:%(lineno)d): %(message)s"
)
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug("Detailed debug info --- only in file")
logger.info("General info --- console and file")
logger.error("Error occurred --- console and file")
```

### Logging in a real application

```python
# inventory_manager.py

import logging

logger = logging.getLogger(__name__)


class InventoryManager:
    def __init__(self):
        self.items = {}
        logger.info("InventoryManager initialized")

    def add_item(self, name, quantity, price):
        if name in self.items:
            old_qty = self.items[name]["quantity"]
            self.items[name]["quantity"] += quantity
            logger.info(
                "Updated '%s': quantity %d -> %d",
                name, old_qty, self.items[name]["quantity"],
            )
        else:
            self.items[name] = {"quantity": quantity, "price": price}
            logger.info("Added new item '%s': qty=%d, price=%.2f", name, quantity, price)

    def remove_item(self, name):
        if name not in self.items:
            logger.warning("Attempted to remove nonexistent item '%s'", name)
            return False
        del self.items[name]
        logger.info("Removed item '%s'", name)
        return True

    def get_total_value(self):
        total = sum(
            item["quantity"] * item["price"]
            for item in self.items.values()
        )
        logger.debug("Calculated total inventory value: %.2f", total)
        return total


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    mgr = InventoryManager()
    mgr.add_item("Laptop", 10, 45000)
    mgr.add_item("Mouse", 50, 1500)
    mgr.add_item("Laptop", 5, 45000)
    mgr.remove_item("Keyboard")
    print(f"Total value: {mgr.get_total_value()}")
```

### Logging exceptions

```python
import logging

logger = logging.getLogger(__name__)

def divide(a, b):
    try:
        result = a / b
        logger.debug("divide(%s, %s) = %s", a, b, result)
        return result
    except ZeroDivisionError:
        logger.exception("Division by zero: divide(%s, %s)", a, b)
        raise
```

`logger.exception()` automatically includes the full traceback.

## Guided Practice

1. Create a `user_service.py` module:

```python
import logging

logger = logging.getLogger(__name__)

users = {}


def register_user(username, email):
    if username in users:
        logger.warning("Registration failed: username '%s' already exists", username)
        return False
    users[username] = {"email": email, "active": True}
    logger.info("User '%s' registered with email '%s'", username, email)
    return True


def deactivate_user(username):
    if username not in users:
        logger.error("Cannot deactivate: user '%s' not found", username)
        return False
    users[username]["active"] = False
    logger.info("User '%s' deactivated", username)
    return True


def get_active_users():
    active = [u for u, data in users.items() if data["active"]]
    logger.debug("Found %d active users out of %d total", len(active), len(users))
    return active
```

2. Create a `main.py` that configures logging and uses the service:

```python
import logging
from user_service import register_user, deactivate_user, get_active_users

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("user_service.log"),
    ],
)

register_user("amina", "amina@example.com")
register_user("ibrahim", "ibrahim@example.com")
register_user("amina", "amina2@example.com")  # Duplicate
deactivate_user("ibrahim")
deactivate_user("yusuf")  # Does not exist
print("Active users:", get_active_users())
```

3. Run the program and examine both the console output and the `user_service.log` file.

4. Change the console handler level to `WARNING` and run again. Observe which messages disappear from the console but remain in the file.

## Daily Challenge

Take the `InventoryManager` example from above and extend it into a complete application with comprehensive logging.

Requirements:

1. Add these methods to `InventoryManager`:
   - `sell_item(name, quantity)` --- Reduce quantity. Log a warning if requested quantity exceeds available stock. Log an error if item does not exist.
   - `restock_item(name, quantity)` --- Increase quantity. Log info.
   - `get_low_stock_items(threshold=5)` --- Return items with quantity below threshold. Log a warning for each low-stock item found.
   - `export_to_csv(filename)` --- Write inventory to CSV. Log info on success, error on failure.

2. Configure logging with:
   - Console handler at INFO level.
   - File handler (`inventory.log`) at DEBUG level.
   - A formatter that includes timestamp, level, module name, and line number.

3. Write a `main()` function that demonstrates all operations and produces meaningful log output.

4. The log file should tell the complete story of what happened during execution.

## Expected Output

Console (INFO and above):
```
2024-01-15 10:30:00 [INFO] inventory_manager: InventoryManager initialized
2024-01-15 10:30:00 [INFO] inventory_manager: Added new item 'Laptop': qty=10, price=45000.00
2024-01-15 10:30:00 [WARNING] inventory_manager: Low stock: 'USB Cable' has only 3 units
```

File (DEBUG and above):
```
2024-01-15 10:30:00 [DEBUG] inventory_manager: Calculated total inventory value: 525000.00
```

## Assessment

1. What are the five log levels in Python, and when should you use each one?
2. Why is `logger.exception()` preferred over `logger.error()` when logging inside an `except` block?
3. How do handlers and formatters work together to control where and how log messages appear?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-09/day-086/`

Include:
- `inventory_manager.py` (extended version)
- `main.py`
- `inventory.log` (sample output)

## Additional Resources

- [Python logging documentation](https://docs.python.org/3/library/logging.html)
- [Logging HOWTO](https://docs.python.org/3/howto/logging.html)

## Reflection

- Think about a project you built earlier in this course. Where would logging have helped you understand what was happening?
- Why is it important to use different log levels rather than logging everything at the same level?
