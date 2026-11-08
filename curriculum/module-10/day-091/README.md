# Day 091: Introduction to Machine Learning

## Learning Objectives

- Define machine learning and explain how it differs from traditional programming.
- Identify the three main types of machine learning: supervised, unsupervised, and reinforcement learning.
- Describe the standard machine learning workflow from data collection to deployment.
- Recognize real-world applications of machine learning across industries.
- Understand when machine learning is appropriate and when simpler solutions are better.

## Introduction

In traditional programming, you write explicit rules: "If the temperature is above 30 degrees, turn on the air conditioner." You tell the computer exactly what to do for every situation. Machine learning flips this around: instead of writing rules, you give the computer data and let it discover the rules on its own.

For example, instead of writing rules to classify emails as spam or not spam, you give a machine learning model thousands of labeled emails ("this one is spam, this one is not") and the model learns the patterns that distinguish spam from legitimate mail. Once trained, the model can classify new emails it has never seen before.

Machine learning is not magic, and it is not always the right tool. If you can write a simple rule that solves the problem, do that. Machine learning shines when the patterns are too complex for humans to articulate explicitly, when you have enough data to learn from, and when the cost of getting it wrong some of the time is acceptable.

## Concepts

### Traditional Programming vs Machine Learning

**Traditional programming:**
```
Input + Rules --> Output
```

**Machine learning:**
```
Input + Output --> Rules (the model)
```

### Types of Machine Learning

**Supervised Learning**: The training data includes both inputs and correct outputs (labels). The model learns to map inputs to outputs.
- Classification: Predict a category (spam or not spam, pass or fail).
- Regression: Predict a number (house price, temperature).

**Unsupervised Learning**: The training data has inputs but no labels. The model finds structure in the data on its own.
- Clustering: Group similar items together (customer segments).
- Dimensionality reduction: Simplify data while preserving important patterns.

**Reinforcement Learning**: An agent learns by interacting with an environment, receiving rewards for good actions and penalties for bad ones.
- Game-playing AI, robotics, recommendation systems.

### The Machine Learning Workflow

```
1. Define the problem
       |
2. Collect and explore data
       |
3. Prepare and clean data
       |
4. Choose a model
       |
5. Train the model
       |
6. Evaluate the model
       |
7. Tune and improve
       |
8. Deploy and monitor
```

### Key Vocabulary

| Term | Definition |
|------|-----------|
| **Feature** | An input variable used for prediction (e.g., age, income) |
| **Label/Target** | The output variable the model predicts (e.g., pass/fail) |
| **Training set** | Data used to train the model |
| **Test set** | Data held back to evaluate the model |
| **Model** | The learned pattern from training data |
| **Overfitting** | Model memorizes training data but fails on new data |
| **Underfitting** | Model is too simple to capture the patterns |

## Practical Examples

### Example: Your first scikit-learn model

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 1. Load a dataset
iris = load_iris()
X = iris.data      # Features: sepal length, sepal width, petal length, petal width
y = iris.target     # Labels: 0=setosa, 1=versicolor, 2=virginica

print(f"Dataset size: {len(X)} samples")
print(f"Features: {iris.feature_names}")
print(f"Classes: {iris.target_names}")

# 2. Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"Training samples: {len(X_train)}, Test samples: {len(X_test)}")

# 3. Choose and train a model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# 4. Make predictions
predictions = model.predict(X_test)

# 5. Evaluate
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2%}")
```

### Example: Understanding features and labels

```python
# Imagine a dataset of students
# Features (inputs): hours_studied, attendance_rate, previous_gpa
# Label (output): pass_or_fail

import pandas as pd

data = {
    "hours_studied": [2, 5, 1, 8, 3, 7, 4, 6],
    "attendance_rate": [0.6, 0.9, 0.4, 0.95, 0.7, 0.85, 0.75, 0.8],
    "previous_gpa": [2.0, 3.5, 1.5, 3.8, 2.5, 3.2, 2.8, 3.0],
    "passed": [0, 1, 0, 1, 0, 1, 1, 1],  # 0=fail, 1=pass
}

df = pd.DataFrame(data)
print(df)
print(f"\nFeatures (X): hours_studied, attendance_rate, previous_gpa")
print(f"Label (y): passed")
print(f"\nPass rate: {df['passed'].mean():.0%}")
```

### Example: When NOT to use machine learning

```python
# Problem: Determine if a number is even or odd.
# Solution: A simple rule. ML is overkill.

def is_even(n):
    return n % 2 == 0

# Problem: Predict which customers will churn based on usage patterns.
# Solution: ML is appropriate --- patterns are complex and data-driven.
```

## Guided Practice

1. Install scikit-learn if you have not already:

```bash
pip install scikit-learn pandas
```

2. Run the Iris classification example above and observe the output.

3. Experiment with the model:
   - Change `test_size` to 0.3 and 0.5. How does accuracy change?
   - Change `random_state` to different values. Does the accuracy vary?
   - Print the first 10 predictions alongside the actual labels to see where the model is right and wrong.

```python
print("\nPrediction vs Actual (first 10):")
for pred, actual in zip(predictions[:10], y_test[:10]):
    status = "correct" if pred == actual else "WRONG"
    print(f"  Predicted: {iris.target_names[pred]}, "
          f"Actual: {iris.target_names[actual]} [{status}]")
```

4. Try a different model. Replace `DecisionTreeClassifier` with:

```python
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3)
```

Compare the accuracy. Which model performed better on this dataset?

## Daily Challenge

### Part 1: ML Application Analysis

List 10 real-world applications of machine learning that you encounter or could encounter in daily life (in Nigeria or globally). For each one, identify:

1. What type of ML it uses (supervised classification, supervised regression, unsupervised clustering, or reinforcement learning).
2. What the features (inputs) might be.
3. What the label or output is.

Example:
- **Application**: Mobile money fraud detection
- **Type**: Supervised classification
- **Features**: Transaction amount, time of day, location, sender history, recipient history
- **Label**: Fraudulent (yes/no)

### Part 2: First ML Experiment

Using the student pass/fail dataset concept from the examples above, create a complete ML experiment:

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Generate synthetic student data
np.random.seed(42)
n_students = 200

data = {
    "hours_studied": np.random.uniform(0, 10, n_students),
    "attendance_rate": np.random.uniform(0.3, 1.0, n_students),
    "previous_gpa": np.random.uniform(1.0, 4.0, n_students),
}

df = pd.DataFrame(data)

# Create a label: students pass if they study enough AND attend enough
df["passed"] = (
    (df["hours_studied"] > 3) &
    (df["attendance_rate"] > 0.6) &
    (df["previous_gpa"] > 2.0)
).astype(int)

# Your task:
# 1. Split the data into training and test sets (80/20 split)
# 2. Train a DecisionTreeClassifier
# 3. Calculate accuracy on the test set
# 4. Print 5 example predictions with actual labels
# 5. Try KNeighborsClassifier and compare accuracy
```

## Expected Output

- Part 1: A document with 10 ML applications, each with type, features, and label.
- Part 2: A Python script that trains two models, compares their accuracy, and prints example predictions.

## Assessment

1. In your own words, explain the difference between supervised and unsupervised learning.
2. What is the purpose of splitting data into training and test sets?
3. Give an example of a problem where machine learning is a good fit and one where a simple rule would be better.

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-10/day-091/`

Include:
- `ml_applications.md` (Part 1)
- `first_ml_experiment.py` (Part 2)

## Additional Resources

- [scikit-learn Getting Started](https://scikit-learn.org/stable/getting_started.html)
- [Google's Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)

## Reflection

- Before this lesson, what did you think machine learning was? How has your understanding changed?
- What real-world problem in your community could potentially be addressed with machine learning?
