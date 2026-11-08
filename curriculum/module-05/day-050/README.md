# Day 050: Module 5 Project -- Automated Web Research Assistant

## Learning Objectives

- Combine API integration, web scraping, and file handling into a complete application.
- Design a multi-source data collection pipeline.
- Organize and persist research results in structured formats.
- Generate summary reports from collected data.
- Practice responsible data collection and attribution.

## Introduction

Over the past ten days, you have learned to automate file operations, parse text with regular expressions, make HTTP requests, work with APIs, scrape web pages, automate browsers, send emails, and schedule tasks. Today you bring it all together in a single, cohesive project.

Your Automated Web Research Assistant is a tool that accepts a research topic from the user, collects relevant information from multiple sources (using APIs and structured data), organizes the findings, and generates a comprehensive report. This is the kind of tool that professionals build to speed up research, competitive analysis, and market intelligence.

This project tests your ability to integrate multiple skills, handle errors gracefully, and produce clean, maintainable code. Take your time to plan the architecture before writing code.

## Project Requirements

### Core Features

1. **Topic Input**: Accept a research topic from the user via command-line input.
2. **Multi-Source Collection**: Gather information from at least two different sources:
   - A public API (e.g., Wikipedia API, GitHub API, or any free API).
   - A web page (parse a practice site or a locally provided HTML file).
3. **Data Organization**: Store collected data in a structured format (JSON and/or CSV).
4. **Report Generation**: Produce a readable summary report as a text or Markdown file.
5. **Error Handling**: Handle network failures, missing data, and invalid inputs gracefully.
6. **Logging**: Log each step of the research process to a log file.

### Technical Requirements

- Use `requests` for API calls.
- Use `BeautifulSoup` for HTML parsing.
- Use `pathlib` for file operations.
- Use `json` and/or `csv` for data storage.
- Use `logging` for application logging.
- Use `re` for any text pattern extraction.
- Organize code into functions with clear responsibilities.
- Add delays between requests to be respectful.
- Follow PEP 8 coding style.

## Project Architecture

```
web_research_assistant/
    research_assistant.py    # Main entry point
    sources/
        api_source.py        # API data collection
        web_source.py         # Web scraping data collection
    utils/
        file_handler.py      # File reading/writing utilities
        report_generator.py  # Report formatting and generation
    output/
        (generated reports and data files go here)
    README.md
```

## Starter Scaffold

```python
# research_assistant.py

import logging
from pathlib import Path
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("research.log"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


def collect_from_api(topic):
    """
    Collect data about the topic from a public API.
    
    Suggested APIs (no key required):
    - Wikipedia: https://en.wikipedia.org/api/rest_v1/page/summary/{topic}
    - GitHub search: https://api.github.com/search/repositories?q={topic}
    
    Returns a dictionary with the collected data.
    """
    # YOUR CODE HERE
    pass


def collect_from_web(topic):
    """
    Collect data about the topic from a web source.
    
    You can use books.toscrape.com, or parse a local HTML file
    containing relevant information.
    
    Returns a dictionary with the collected data.
    """
    # YOUR CODE HERE
    pass


def save_results(data, output_dir):
    """
    Save collected data to JSON and/or CSV files.
    
    Args:
        data: Dictionary containing all collected data.
        output_dir: Path to the output directory.
    
    Returns the paths of saved files.
    """
    # YOUR CODE HERE
    pass


def generate_report(data, output_dir):
    """
    Generate a human-readable research report.
    
    Args:
        data: Dictionary containing all collected data.
        output_dir: Path to the output directory.
    
    Returns the path to the generated report.
    """
    # YOUR CODE HERE
    pass


def run_research(topic):
    """Main research pipeline."""
    logger.info(f"Starting research on: {topic}")
    
    # Create output directory
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = Path("output") / f"{topic.replace(' ', '_')}_{timestamp}"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Collect data from all sources
    all_data = {
        "topic": topic,
        "timestamp": timestamp,
        "sources": {},
    }
    
    logger.info("Collecting from API sources...")
    api_data = collect_from_api(topic)
    if api_data:
        all_data["sources"]["api"] = api_data
    
    logger.info("Collecting from web sources...")
    web_data = collect_from_web(topic)
    if web_data:
        all_data["sources"]["web"] = web_data
    
    # Save and report
    logger.info("Saving results...")
    save_results(all_data, output_dir)
    
    logger.info("Generating report...")
    report_path = generate_report(all_data, output_dir)
    
    logger.info(f"Research complete. Report saved to: {report_path}")
    return report_path


if __name__ == "__main__":
    print("=== Automated Web Research Assistant ===\n")
    topic = input("Enter a research topic: ").strip()
    if topic:
        report = run_research(topic)
        print(f"\nResearch complete! Report: {report}")
    else:
        print("No topic provided. Exiting.")
```

## Expected Output

```
=== Automated Web Research Assistant ===

Enter a research topic: Python programming

2025-03-15 10:30:00 [INFO] Starting research on: Python programming
2025-03-15 10:30:00 [INFO] Collecting from API sources...
2025-03-15 10:30:01 [INFO]   Wikipedia: Found summary (1,245 characters)
2025-03-15 10:30:02 [INFO]   GitHub: Found 30 related repositories
2025-03-15 10:30:02 [INFO] Collecting from web sources...
2025-03-15 10:30:03 [INFO]   Books: Found 5 related books
2025-03-15 10:30:03 [INFO] Saving results...
2025-03-15 10:30:03 [INFO]   Data saved to output/Python_programming_20250315_103000/data.json
2025-03-15 10:30:03 [INFO] Generating report...
2025-03-15 10:30:03 [INFO]   Report saved to output/Python_programming_20250315_103000/report.md
2025-03-15 10:30:03 [INFO] Research complete.

Research complete! Report: output/Python_programming_20250315_103000/report.md
```

## Evaluation Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Functionality | 30% | All core features work correctly |
| Code quality | 20% | Clean, readable, well-organized code following PEP 8 |
| Error handling | 15% | Graceful handling of network failures, missing data, invalid input |
| Data collection | 15% | Successfully collects from at least two sources |
| Report quality | 10% | Clear, well-formatted, informative output |
| Documentation | 10% | README with setup instructions, usage, and design decisions |

## Assessment

1. How would you design this system to add new data sources without modifying existing code?
2. What strategies can you use to make your research assistant resilient to network failures?
3. Why is logging important in automation scripts, and how does it differ from print statements?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-05/day-050/`

Include your complete project directory with all source files, a sample output, and a `README.md`.

## Additional Resources

- [Wikipedia API documentation](https://www.mediawiki.org/wiki/API:Main_page)
- [logging module documentation](https://docs.python.org/3/library/logging.html)
- [Python project structure best practices](https://docs.python-guide.org/writing/structure/)

## Reflection

- What was the most challenging part of integrating multiple data sources?
- How would you extend this tool to support additional sources or output formats?
- What did you learn about error handling when working with external services?
