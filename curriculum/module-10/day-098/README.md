# Day 098: Responsible AI and Data Privacy

## Learning Objectives

- Understand the ethical responsibilities of building AI-powered applications.
- Identify sources of bias in datasets and machine learning models.
- Apply fairness checks to detect biased predictions across groups.
- Understand data privacy principles and their importance.
- Document ethical considerations as part of the development process.

## Introduction

Machine learning models learn from data, and data reflects the world that produced it --- including its biases, inequalities, and historical patterns. A hiring model trained on past decisions may learn to discriminate. A loan approval model trained on historical data may perpetuate financial inequality. A facial recognition system trained mostly on one demographic may fail to recognize others.

As engineers, we have a responsibility to understand these risks and take steps to mitigate them. Responsible AI is not about avoiding AI altogether; it is about building systems that are fair, transparent, and accountable. This means checking your data for bias, testing your model's performance across different groups, being transparent about how your model works and what it cannot do, and protecting the privacy of the people whose data you use.

Data privacy is equally critical. People's personal information --- health records, financial data, location history, academic records --- deserves protection. Regulations like GDPR (European Union), NDPR (Nigeria Data Protection Regulation), and similar laws worldwide establish legal requirements for how personal data must be handled. Even where regulations are not enforced, ethical engineering demands that you treat people's data with care.

## Concepts

### Sources of Bias in ML

| Source | Example |
|--------|---------|
| Historical bias | Training data reflects past discrimination |
| Representation bias | Some groups are underrepresented in data |
| Measurement bias | Data collected differently for different groups |
| Aggregation bias | One model for diverse subgroups that need different models |
| Label bias | Labels assigned by humans with their own biases |

### Fairness Metrics

- **Demographic parity**: Equal positive prediction rate across groups.
- **Equal opportunity**: Equal true positive rate across groups.
- **Predictive parity**: Equal precision across groups.

### Data Privacy Principles

1. **Purpose limitation**: Collect data only for a stated purpose.
2. **Data minimization**: Collect only the minimum data needed.
3. **Storage limitation**: Do not keep data longer than necessary.
4. **Consent**: Get informed consent before collecting personal data.
5. **Anonymization**: Remove personally identifiable information when possible.
6. **Security**: Protect data against unauthorized access.
7. **Transparency**: Tell people what data you collect and how you use it.

### Responsible AI Checklist

Before deploying an AI system, ask:
- What data was used to train it? Is it representative?
- Have you tested performance across different demographic groups?
- Can you explain why the model makes specific predictions?
- What happens if the model is wrong? What is the impact?
- Who is accountable for the model's decisions?
- How will you monitor the model after deployment?
- Have you documented the model's limitations?

## Practical Examples

### Example 1: Detecting bias in a dataset

```python
import pandas as pd
import numpy as np

# Simulated student scholarship dataset
np.random.seed(42)
n = 500

data = {
    "gpa": np.random.uniform(2.0, 4.0, n),
    "test_score": np.random.uniform(50, 100, n),
    "extracurriculars": np.random.randint(0, 6, n),
    "gender": np.random.choice(["M", "F"], n),
    "region": np.random.choice(
        ["Urban", "Rural"],
        n,
        p=[0.65, 0.35],  # Unequal representation
    ),
}
df = pd.DataFrame(data)

# Add a biased award decision
score = df["gpa"] * 15 + df["test_score"] * 0.5 + df["extracurriculars"] * 3
# Bias: urban students get a hidden advantage
score[df["region"] == "Urban"] += 5
df["awarded"] = (score > 75).astype(int)

# Analyze for bias
print("=== Dataset Composition ===")
print(f"Total students: {len(df)}")
print(f"Region distribution:\n{df['region'].value_counts()}")
print(f"Gender distribution:\n{df['gender'].value_counts()}")

print("\n=== Award Rates by Group ===")
for group_col in ["gender", "region"]:
    print(f"\nBy {group_col}:")
    rates = df.groupby(group_col)["awarded"].mean()
    for group, rate in rates.items():
        print(f"  {group}: {rate:.2%}")
    rate_diff = abs(rates.values[0] - rates.values[1])
    if rate_diff > 0.05:
        print(f"  WARNING: {rate_diff:.2%} difference in award rates")
```

### Example 2: Evaluating model fairness

```python
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Prepare data (drop region from features to avoid direct discrimination)
feature_cols = ["gpa", "test_score", "extracurriculars"]
X = df[feature_cols]
y = df["awarded"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier(max_depth=4, random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)

print(f"\nOverall accuracy: {accuracy_score(y_test, predictions):.2%}")

# Check fairness: does the model predict equally across groups?
test_df = X_test.copy()
test_df["actual"] = y_test.values
test_df["predicted"] = predictions
test_df["region"] = df.loc[X_test.index, "region"].values
test_df["gender"] = df.loc[X_test.index, "gender"].values

print("\n=== Fairness Analysis ===")
for group_col in ["gender", "region"]:
    print(f"\nBy {group_col}:")
    for group in test_df[group_col].unique():
        subset = test_df[test_df[group_col] == group]
        acc = accuracy_score(subset["actual"], subset["predicted"])
        pred_positive_rate = subset["predicted"].mean()
        actual_positive_rate = subset["actual"].mean()
        print(f"  {group}:")
        print(f"    Accuracy: {acc:.2%}")
        print(f"    Predicted positive rate: {pred_positive_rate:.2%}")
        print(f"    Actual positive rate: {actual_positive_rate:.2%}")
```

### Example 3: Data anonymization

```python
import hashlib


def anonymize_record(record):
    """Remove or mask personally identifiable information.

    Args:
        record: Dictionary with student data.

    Returns:
        Anonymized copy of the record.
    """
    anonymized = record.copy()

    # Hash the student ID (one-way, cannot be reversed)
    if "student_id" in anonymized:
        hashed = hashlib.sha256(
            anonymized["student_id"].encode()
        ).hexdigest()[:12]
        anonymized["student_id"] = f"ANON_{hashed}"

    # Remove direct identifiers
    for field in ["name", "email", "phone", "address"]:
        if field in anonymized:
            del anonymized[field]

    # Generalize age to range
    if "age" in anonymized:
        age = anonymized["age"]
        if age < 20:
            anonymized["age_group"] = "under_20"
        elif age < 30:
            anonymized["age_group"] = "20-29"
        else:
            anonymized["age_group"] = "30+"
        del anonymized["age"]

    return anonymized


# Example
student = {
    "student_id": "STU12345",
    "name": "Amina Yusuf",
    "email": "amina@example.com",
    "age": 22,
    "gpa": 3.5,
    "department": "Computer Science",
}

print("Original:", student)
print("Anonymized:", anonymize_record(student))
```

## Guided Practice

1. Run the bias detection example. Answer:
   - Is there a significant difference in award rates between urban and rural students?
   - Is there a difference between genders?

2. Run the fairness analysis on the trained model. Answer:
   - Does the model's prediction rate differ across regions, even though region is not a feature?
   - Why might this happen? (Hint: think about what other features correlate with region.)

3. Modify the dataset to remove the bias (eliminate the +5 boost for urban students). Retrain the model. Does the fairness gap shrink?

4. Write an `anonymize_dataframe()` function that anonymizes an entire pandas DataFrame.

## Daily Challenge

### Part 1: Bias Audit

Analyze the following dataset for potential bias and document your findings.

```python
import numpy as np
import pandas as pd

np.random.seed(42)
n = 600

gender = np.random.choice(["M", "F"], n)
region = np.random.choice(["North", "South", "West"], n, p=[0.5, 0.3, 0.2])
school_type = np.random.choice(["Public", "Private"], n, p=[0.7, 0.3])

# Base academic score
base_score = np.random.normal(65, 15, n)

# Introduce systematic biases
score = base_score.copy()
score[school_type == "Private"] += 8     # Private school advantage
score[region == "South"] += 3            # Regional advantage

gpa = np.clip(score / 25, 0, 4.0).round(2)
admitted = (score > 70).astype(int)

df = pd.DataFrame({
    "gender": gender,
    "region": region,
    "school_type": school_type,
    "entrance_score": np.round(score, 1),
    "gpa_predicted": gpa,
    "admitted": admitted,
})
```

Your bias audit should:

1. Calculate admission rates by gender, region, and school type.
2. Identify which groups have significantly different admission rates.
3. Determine whether the biases are in the data, the model, or both.
4. Propose at least 3 specific actions to reduce the identified biases.

### Part 2: Privacy Impact Assessment

Write a Privacy Impact Assessment (PIA) document for a hypothetical student performance prediction system. The system collects:
- Student academic records
- Attendance data
- Demographic information
- Family income level
- Health records

Your PIA should address:
1. What data is collected and why.
2. Which data is necessary and which could be eliminated (data minimization).
3. How data should be stored and protected.
4. Who should have access to the data.
5. How long data should be retained.
6. What rights students and parents should have over their data.
7. Risks of data misuse and mitigation strategies.

### Part 3: Responsible AI Documentation

Create a "Model Card" for the student admission classifier. A Model Card is a standardized document that describes:
- Model details (type, version, developers).
- Intended use (and misuse scenarios).
- Training data description.
- Performance metrics (overall and per-group).
- Limitations and known biases.
- Ethical considerations.

## Expected Output

Three documents:
- `bias_audit.py` (code and analysis)
- `privacy_assessment.md` (Privacy Impact Assessment)
- `model_card.md` (Model Card for the classifier)

## Assessment

1. Give an example of how historical bias in training data can lead to unfair model predictions.
2. What is the difference between removing a sensitive attribute from features and ensuring the model is fair?
3. Name three data privacy principles and explain why each matters.

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-10/day-098/`

Include:
- `bias_audit.py`
- `privacy_assessment.md`
- `model_card.md`

## Additional Resources

- [Google Responsible AI Practices](https://ai.google/responsibility/responsible-ai-practices/)
- [Nigeria Data Protection Regulation (NDPR)](https://ndpc.gov.ng/)

## Reflection

- Think about an AI system you interact with regularly. What biases might it have? How would you test for them?
- If you were building a student grading AI for your school, what ethical guidelines would you set for yourself?
