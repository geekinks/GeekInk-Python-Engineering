# Day 097: AI APIs and Integration

## Learning Objectives

- Understand how to use AI services through APIs without building models from scratch.
- Make HTTP requests to AI API endpoints and process responses.
- Handle API keys securely using environment variables.
- Build practical applications that use AI capabilities.
- Understand rate limits, costs, and responsible API usage.

## Introduction

Not every AI application requires you to build and train your own machine learning model. Many powerful AI capabilities --- text generation, image recognition, language translation, sentiment analysis --- are available as cloud services through APIs. You send data to the API, it processes it using pre-trained models, and returns the results.

This approach has several advantages. You do not need specialized hardware (GPUs) for training. You do not need large datasets. You can start building AI-powered features in minutes rather than months. Companies like OpenAI, Google, Anthropic, and Hugging Face provide APIs that give you access to state-of-the-art models.

The trade-off is cost and dependency. API calls cost money (usually per request or per token), your data leaves your system, and you depend on an external service being available. For many applications, this trade-off is well worth it.

## Concepts

### How AI APIs Work

```
Your Application
     |
     | HTTP Request (with data + API key)
     v
AI Service (cloud)
     |
     | HTTP Response (with results)
     v
Your Application (processes results)
```

### API Key Security

Never hardcode API keys in your source code. Use environment variables:

```python
import os

api_key = os.environ.get("AI_API_KEY")
if not api_key:
    raise ValueError("Set the AI_API_KEY environment variable")
```

Set the variable in your terminal:
```bash
export AI_API_KEY="your-key-here"
```

Or use a `.env` file (never commit this file to Git):
```
AI_API_KEY=your-key-here
```

### Common AI API Capabilities

| Capability | Example APIs | Use Case |
|-----------|-------------|----------|
| Text generation | OpenAI, Anthropic | Chatbots, content creation, summarization |
| Text classification | Hugging Face | Sentiment analysis, spam detection |
| Translation | Google Translate API | Multi-language applications |
| Image recognition | Google Vision, AWS Rekognition | Object detection, OCR |
| Speech-to-text | Google Speech, Whisper | Transcription, voice commands |

### Rate Limits and Responsible Usage

APIs have rate limits (requests per minute/hour). Always:
- Handle rate limit errors gracefully.
- Cache results to avoid repeated identical requests.
- Do not send sensitive personal data without considering privacy.

## Practical Examples

### Example 1: Text classification with Hugging Face Inference API

```python
import requests
import os

API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"


def classify_sentiment(text, api_key):
    """Classify the sentiment of a text as positive or negative.

    Args:
        text: The text to analyze.
        api_key: Hugging Face API key.

    Returns:
        A list of label-score pairs.
    """
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {"inputs": text}

    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()


# Usage (requires a Hugging Face API key)
# api_key = os.environ.get("HF_API_KEY")
# result = classify_sentiment("I love learning Python!", api_key)
# print(result)

# Simulated output for demonstration:
print("Simulated sentiment analysis:")
sample_results = [
    {"text": "I love learning Python!", "label": "POSITIVE", "score": 0.9998},
    {"text": "This homework is too difficult.", "label": "NEGATIVE", "score": 0.9876},
    {"text": "The project deadline is tomorrow.", "label": "NEGATIVE", "score": 0.6543},
]
for r in sample_results:
    print(f"  '{r['text']}' -> {r['label']} ({r['score']:.2%})")
```

### Example 2: Building a text analysis tool without external APIs

When you do not have an API key, you can still build useful text analysis tools using local techniques:

```python
from collections import Counter
import re


def analyze_text(text):
    """Perform basic text analysis on a given string.

    Args:
        text: The text to analyze.

    Returns:
        A dictionary containing analysis results.
    """
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]

    word_freq = Counter(words)

    return {
        "word_count": len(words),
        "unique_words": len(set(words)),
        "sentence_count": len(sentences),
        "avg_word_length": sum(len(w) for w in words) / len(words) if words else 0,
        "avg_sentence_length": len(words) / len(sentences) if sentences else 0,
        "top_words": word_freq.most_common(10),
        "vocabulary_richness": len(set(words)) / len(words) if words else 0,
    }


sample_text = """
Python is a versatile programming language. Python is used in web development,
data science, artificial intelligence, and automation. Many developers love Python
because of its clean syntax and large community. Learning Python opens doors to
many career opportunities in technology.
"""

result = analyze_text(sample_text)
print("Text Analysis Results:")
print(f"  Words: {result['word_count']}")
print(f"  Unique words: {result['unique_words']}")
print(f"  Sentences: {result['sentence_count']}")
print(f"  Avg word length: {result['avg_word_length']:.1f} characters")
print(f"  Vocabulary richness: {result['vocabulary_richness']:.2%}")
print(f"  Top words: {result['top_words'][:5]}")
```

### Example 3: Simple keyword-based sentiment classifier

```python
def simple_sentiment(text):
    """Classify sentiment using keyword matching.

    This is a basic approach that works for simple cases.
    Production applications should use proper NLP models.
    """
    positive_words = {
        "good", "great", "excellent", "love", "happy", "wonderful",
        "amazing", "fantastic", "best", "enjoy", "helpful", "perfect",
        "beautiful", "brilliant", "outstanding", "pleasant",
    }
    negative_words = {
        "bad", "terrible", "awful", "hate", "sad", "horrible",
        "worst", "boring", "difficult", "ugly", "poor", "annoying",
        "frustrating", "disappointing", "useless", "broken",
    }

    words = set(text.lower().split())
    pos_count = len(words & positive_words)
    neg_count = len(words & negative_words)

    if pos_count > neg_count:
        return "positive", pos_count / (pos_count + neg_count)
    elif neg_count > pos_count:
        return "negative", neg_count / (pos_count + neg_count)
    else:
        return "neutral", 0.5


texts = [
    "This course is great and the instructor is excellent!",
    "The homework is terrible and boring.",
    "The class starts at 9am on Monday.",
    "I love the amazing projects but the tests are difficult.",
]

for text in texts:
    sentiment, confidence = simple_sentiment(text)
    print(f"  [{sentiment:8s} {confidence:.0%}] {text}")
```

## Guided Practice

1. Build a text analysis tool that combines multiple analysis functions:

```python
def full_analysis(text):
    """Perform comprehensive text analysis."""
    stats = analyze_text(text)
    sentiment, confidence = simple_sentiment(text)

    return {
        **stats,
        "sentiment": sentiment,
        "sentiment_confidence": confidence,
    }
```

2. Test it on 5 different text samples (product reviews, news headlines, social media posts).

3. If you have a Hugging Face API key (free to create at huggingface.co):
   - Set it as an environment variable.
   - Use the sentiment classification API on the same texts.
   - Compare results from the simple keyword approach with the API results.

4. If you do not have an API key, extend the simple_sentiment function:
   - Add 20 more positive and negative words.
   - Handle negation: "not good" should be negative.
   - Test on 10 diverse sentences and evaluate accuracy.

## Daily Challenge

Build a Text Analysis Application that analyzes a collection of text documents.

### Requirements

Create `text_analyzer.py` with a `TextAnalyzer` class that:

1. **Loads text** from a file or string.

2. **Analyzes text** providing:
   - Word count, sentence count, paragraph count.
   - Average word length and sentence length.
   - Top 10 most frequent words (excluding common stop words).
   - Vocabulary richness (unique words / total words).
   - Reading level estimate (based on avg sentence and word length).
   - Simple sentiment score.

3. **Compares texts**: Given two texts, compare their statistics side by side.

4. **Generates a report**: Output a formatted summary of the analysis.

### Implementation

```python
class TextAnalyzer:
    STOP_WORDS = {
        "the", "a", "an", "is", "are", "was", "were", "be", "been",
        "being", "have", "has", "had", "do", "does", "did", "will",
        "would", "could", "should", "may", "might", "can", "shall",
        "to", "of", "in", "for", "on", "with", "at", "by", "from",
        "it", "its", "this", "that", "and", "or", "but", "not",
        "i", "you", "he", "she", "we", "they", "my", "your",
    }

    def __init__(self, text):
        # Your implementation here
        pass

    def word_count(self):
        pass

    def sentence_count(self):
        pass

    def top_words(self, n=10):
        pass

    def vocabulary_richness(self):
        pass

    def sentiment(self):
        pass

    def reading_level(self):
        """Estimate reading difficulty (simple formula)."""
        pass

    def compare(self, other):
        """Compare this text with another TextAnalyzer instance."""
        pass

    def report(self):
        """Generate a formatted analysis report."""
        pass
```

Test with at least 3 different text samples. Generate reports for each and a comparison between two of them.

### Optional: API Integration

If you have access to an AI API (Hugging Face free tier), add a method:

```python
def ai_sentiment(self, api_key):
    """Get sentiment from AI API and compare with local analysis."""
    pass
```

## Expected Output

```
=== Text Analysis Report ===
Text: "Python Programming Article"
Words: 245
Sentences: 18
Paragraphs: 4
Avg word length: 5.2 characters
Avg sentence length: 13.6 words
Vocabulary richness: 62.4%
Reading level: Intermediate
Sentiment: Positive (72%)
Top words: python (8), programming (5), code (4), learn (3), ...

=== Comparison ===
                     Text A      Text B
Words                245         312
Sentences            18          24
Vocabulary richness  62.4%       55.1%
Reading level        Intermediate Advanced
Sentiment            Positive    Neutral
```

## Assessment

1. What are the advantages and disadvantages of using AI APIs versus building your own ML models?
2. Why should API keys never be stored in source code or committed to Git?
3. How would you handle a situation where an AI API returns incorrect or biased results?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-10/day-097/`

Include:
- `text_analyzer.py`
- `sample_texts/` (directory with your test texts)
- `analysis_output.txt` (reports generated by your tool)

## Additional Resources

- [Hugging Face Inference API](https://huggingface.co/docs/api-inference/)
- [Python requests library](https://docs.python-requests.org/)

## Reflection

- How might AI APIs change the way software is built in the next few years?
- What are the ethical considerations of sending user data to external AI services?
