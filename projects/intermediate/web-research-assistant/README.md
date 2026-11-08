# Automated Web Research Assistant

**Module:** 5 — Automation and Web Scraping
**Day:** 50
**Difficulty:** Intermediate

---

## Problem Statement

Researchers and professionals spend significant time gathering information from multiple online sources. This project builds an automated research assistant that collects, organizes, and summarizes information from APIs and web sources on a given topic — applying automation, HTTP requests, and web scraping skills responsibly.

## Objectives

- Make HTTP requests and process JSON responses from APIs.
- Parse HTML content with Beautiful Soup.
- Organize collected data into structured files (CSV, JSON).
- Generate formatted research summaries.
- Follow responsible scraping practices (respect robots.txt, rate limits, terms of service).

## Requirements

### Functional Requirements

1. **Topic input:** Accept a research topic from the user.

2. **Data collection from APIs:**
   - Search a free knowledge API (e.g., Wikipedia API, Open Library API, or a news API).
   - Collect at least 5 relevant results per source.
   - Handle API errors, rate limits, and empty responses.

3. **Web content extraction (optional, if a scrapable site is available):**
   - Parse relevant content from HTML pages.
   - Respect `robots.txt` and implement request delays.
   - Extract titles, summaries, dates, and URLs.

4. **Data organization:**
   - Save raw results to a JSON file.
   - Save a structured summary to a CSV file.
   - Organize output in a results directory per topic.

5. **Report generation:**
   - Generate a Markdown report summarizing findings.
   - Include source attribution (title, URL, date).
   - Include a brief summary for each source.

### Non-Functional Requirements

- The tool must handle network errors without crashing.
- Request delays must be implemented between API calls (at least 1 second).
- No scraping of sites that prohibit it in their terms of service.

## Responsible Scraping Policy

This project teaches responsible data collection. Students must:

- Check `robots.txt` before scraping any website.
- Implement rate limiting (minimum 1-second delay between requests).
- Include a descriptive `User-Agent` header.
- Never bypass authentication or access controls.
- Never scrape personal data without consent.
- Prefer public APIs over scraping when available.
- Document which sources are used and their terms.

## Technologies

- Python 3.10+
- `requests` — HTTP requests
- `beautifulsoup4` — HTML parsing
- Standard library (`json`, `csv`, `os`, `time`, `re`)

## Implementation Milestones

| Milestone | Description |
| :--- | :--- |
| 1. API integration | Fetch data from one free API |
| 2. Data storage | Save results to JSON and CSV |
| 3. Multiple sources | Add a second API source |
| 4. HTML parsing | Extract content from a web page (if applicable) |
| 5. Report generation | Generate a Markdown summary report |
| 6. Error handling | Handle network errors, empty results, rate limits |

## Testing Requirements

- Test with multiple topics to verify results vary.
- Test with a nonsense topic to verify graceful handling of no results.
- Test with network disconnected to verify error handling.
- Verify output files are correctly formatted.

## Expected Deliverables

1. `main.py` — Entry point.
2. `researcher.py` — Core research logic.
3. `report_generator.py` — Report formatting.
4. `results/` directory with sample output (JSON, CSV, Markdown report).
5. Documentation of APIs and sources used.

## Evaluation Criteria

| Criterion | Weight | Description |
| :--- | :--- | :--- |
| API integration | 25% | Successfully fetches and processes API data |
| Data organization | 20% | Results saved in structured, correct formats |
| Report quality | 15% | Generated report is readable and well-attributed |
| Responsible practices | 15% | Rate limiting, error handling, terms compliance |
| Code quality | 15% | Modular, readable, PEP 8 compliant |
| Completeness | 10% | All required features implemented |
