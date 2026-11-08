# Day 049: Email Automation and Task Scheduling

## Learning Objectives

- Understand how email sending works using SMTP.
- Use Python's `smtplib` and `email` modules to compose and send emails.
- Apply proper security practices when handling email credentials.
- Schedule tasks to run at specific times or intervals using the `schedule` library.
- Build a daily report emailer that generates and sends reports on a schedule.

## Introduction

Automation becomes truly powerful when it runs without you. Two common needs are sending emails (notifications, reports, alerts) and scheduling tasks (run this script every morning, check this API every hour).

Python's standard library includes `smtplib` for connecting to email servers and `email` for composing messages with headers, body text, and attachments. While there are many email-sending services and APIs available, understanding SMTP gives you a solid foundation for any email-related automation.

Task scheduling lets your scripts run at specific times or intervals. The `schedule` library provides a simple, human-readable API for defining when tasks should execute. For production systems, you would use the operating system's cron (Linux/macOS) or Task Scheduler (Windows), but the `schedule` library is excellent for learning and for scripts that run continuously.

**Security note**: Never hard-code email passwords in your source code. Always use environment variables or app-specific passwords. Many email providers require you to generate an "app password" rather than using your main account password.

## Concepts

### How SMTP Works

SMTP (Simple Mail Transfer Protocol) is the protocol used to send emails. Your Python script connects to an SMTP server, authenticates, and hands off the message for delivery.

Common SMTP servers:
- Gmail: `smtp.gmail.com`, port 587 (TLS)
- Outlook: `smtp-mail.outlook.com`, port 587 (TLS)
- Yahoo: `smtp.mail.yahoo.com`, port 587 (TLS)

### Composing Emails

The `email.mime` modules help you build properly formatted email messages:
- `MIMEText` -- plain text or HTML messages.
- `MIMEMultipart` -- messages with attachments.
- `MIMEBase` -- binary attachments.

### The `schedule` Library

Install with: `pip install schedule`

```python
import schedule

schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("09:00").do(job)
schedule.every().monday.do(job)
```

### Cron (Linux/macOS)

For production scheduling, cron is the standard tool. A cron expression has five fields:

```
* * * * *
| | | | |
| | | | day of week (0-7, 0=Sunday)
| | | month (1-12)
| | day of month (1-31)
| hour (0-23)
minute (0-59)
```

Example: `0 9 * * *` runs at 9:00 AM every day.

## Practical Examples

```python
# Composing an email (without sending -- safe to run)
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create a multipart message
msg = MIMEMultipart()
msg["From"] = "sender@example.com"
msg["To"] = "recipient@example.com"
msg["Subject"] = "Daily Python Report"

body = """
Hello,

Here is your daily Python learning report:

- Completed: Day 049 - Email Automation
- Exercises solved: 3/3
- Time spent: 2 hours

Keep up the great work!

Best regards,
GeekInk Automation
"""

msg.attach(MIMEText(body, "plain"))

# Display the composed email
print("Composed email:")
print(f"  From: {msg['From']}")
print(f"  To: {msg['To']}")
print(f"  Subject: {msg['Subject']}")
print(f"  Body length: {len(body)} characters")
```

```python
# Sending an email (simulation -- shows the process without actually sending)
import smtplib
import os
from email.mime.text import MIMEText


def send_email(to_address, subject, body):
    """
    Send an email using SMTP.
    
    In a real application, set these environment variables:
      EMAIL_ADDRESS - your email address
      EMAIL_PASSWORD - your app-specific password
      SMTP_SERVER - your SMTP server address
    """
    from_address = os.environ.get("EMAIL_ADDRESS")
    password = os.environ.get("EMAIL_PASSWORD")
    smtp_server = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
    
    if not from_address or not password:
        print("[SIMULATION] Email would be sent:")
        print(f"  To: {to_address}")
        print(f"  Subject: {subject}")
        print(f"  Body: {body[:100]}...")
        print("  (Set EMAIL_ADDRESS and EMAIL_PASSWORD env vars to send for real)")
        return False
    
    msg = MIMEText(body, "plain")
    msg["From"] = from_address
    msg["To"] = to_address
    msg["Subject"] = subject
    
    try:
        with smtplib.SMTP(smtp_server, 587) as server:
            server.starttls()
            server.login(from_address, password)
            server.send_message(msg)
        print(f"Email sent to {to_address}")
        return True
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
        return False


send_email("student@example.com", "Test Email", "This is a test from Python automation.")
```

```python
import schedule
import time
from datetime import datetime


def morning_greeting():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Good morning! Time to code.")


def hourly_check():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Hourly system check complete.")


# Schedule tasks
schedule.every(5).seconds.do(morning_greeting)  # Using seconds for demo

print("Scheduler running (press Ctrl+C to stop)...")
print("(Running for 20 seconds as a demonstration)\n")

end_time = time.time() + 20
while time.time() < end_time:
    schedule.run_pending()
    time.sleep(1)

print("\nScheduler stopped.")
```

## Guided Practice

Build a report generator that creates a summary and simulates emailing it.

```python
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json


def generate_daily_report():
    """Generate a daily learning progress report."""
    report_data = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "student": "Amina Ibrahim",
        "module": 5,
        "day": 49,
        "topic": "Email Automation and Task Scheduling",
        "exercises_completed": 3,
        "exercises_total": 3,
        "time_spent_minutes": 120,
        "notes": "Learned about SMTP and the schedule library.",
    }
    
    # Format as a readable report
    report_text = f"""
GeekInk Python Engineering - Daily Progress Report
{'=' * 50}
Date: {report_data['date']}
Student: {report_data['student']}

Progress:
  Module {report_data['module']}, Day {report_data['day']}
  Topic: {report_data['topic']}
  Exercises: {report_data['exercises_completed']}/{report_data['exercises_total']}
  Time spent: {report_data['time_spent_minutes']} minutes

Notes:
  {report_data['notes']}

{'=' * 50}
Keep learning, keep building!
"""
    return report_text, report_data


def compose_report_email(report_text, recipient):
    """Compose an email with the report."""
    msg = MIMEMultipart()
    msg["From"] = "reports@geekink.example.com"
    msg["To"] = recipient
    msg["Subject"] = f"Daily Report - {datetime.now().strftime('%Y-%m-%d')}"
    msg.attach(MIMEText(report_text, "plain"))
    return msg


def save_report(report_data, filename="reports.json"):
    """Save report data to a JSON file for record keeping."""
    try:
        with open(filename, "r") as f:
            reports = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        reports = []
    
    reports.append(report_data)
    
    with open(filename, "w") as f:
        json.dump(reports, f, indent=2)
    
    return len(reports)


# Generate and display the report
report_text, report_data = generate_daily_report()
print(report_text)

# Compose the email (simulation)
email = compose_report_email(report_text, "instructor@geekink.example.com")
print(f"Email composed: '{email['Subject']}' to {email['To']}")

# Save to file
count = save_report(report_data)
print(f"Report saved. Total reports on file: {count}")
```

## Daily Challenge

**Build a Daily Report Emailer**

Write a script called `daily_reporter.py` that:

1. Generates a progress report (you can use simulated data or read from a JSON file).
2. Formats the report as a readable email body.
3. Composes the email using `email.mime`.
4. Simulates sending it (print the full email details) unless real credentials are configured.
5. Saves the report to a local JSON file for record-keeping.
6. Uses the `schedule` library to run the report generation every N seconds (for testing) or at a specified time.
7. Runs for a configurable duration, then exits.

Requirements:
- Use environment variables for any email credentials (never hard-code).
- Include a `--once` mode that generates and "sends" a single report without scheduling.
- Include a `--schedule` mode that runs on a timer.
- Save reports to `report_history.json`.
- Format all output cleanly.

## Expected Output

```
=== Daily Report Emailer ===
Mode: single report

Generating report...
  Date: 2025-03-15
  Student: Amina Ibrahim
  Module: 5, Day: 49
  Exercises: 3/3

Composing email...
  From: reports@geekink.example.com
  To: instructor@geekink.example.com
  Subject: Daily Report - 2025-03-15

[SIMULATION] Email details:
  This is a simulated send. Set EMAIL_ADDRESS and EMAIL_PASSWORD
  environment variables to send for real.

Report saved to report_history.json (total: 5 reports)
```

## Assessment

1. Why should you never store email passwords directly in your Python source code?
2. What is the difference between `smtplib.SMTP()` and `smtplib.SMTP_SSL()`? When do you use `starttls()`?
3. What are the advantages and disadvantages of using the `schedule` library versus the operating system's cron for task scheduling?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-05/day-049/`

Include `daily_reporter.py`, a sample `report_history.json`, and a `README.md`.

## Additional Resources

- [smtplib documentation](https://docs.python.org/3/library/smtplib.html)
- [email.mime documentation](https://docs.python.org/3/library/email.mime.html)
- [schedule library](https://schedule.readthedocs.io/)

## Reflection

- What are the security risks of automated email sending, and how can you mitigate them?
- How would you modify your scheduler to handle failures (e.g., the email server is down)?
