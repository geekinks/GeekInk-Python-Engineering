# Day 093: Supervised Learning - Classification

## Learning Objectives

- Understand what classification is and when to use it.
- Use scikit-learn's API to train and evaluate classification models.
- Build a DecisionTreeClassifier and understand how it makes decisions.
- Measure model performance using accuracy.
- Interpret predictions and identify where the model succeeds or fails.

## Introduction

Classification is a type of supervised learning where the model predicts which category or class a data point belongs to. The output is a discrete label, not a continuous number. Examples include predicting whether an email is spam or not spam, whether a student will pass or fail, whether a transaction is fraudulent or legitimate, or which disease a patient has based on their symptoms.

The decision tree is one of the most intuitive classification algorithms. It works by asking a series of yes/no questions about the features, splitting the data at each step. Think of it like a flowchart: "Is the student's attendance above 70%? If yes, are their study hours above 5? If yes, predict pass." The tree learns which questions to ask and what thresholds to use from the training data.

Decision trees are popular because they are easy to understand and visualize. You can trace exactly why the model made a specific prediction. This interpretability is especially valuable in domains like education and healthcare where you need to explain your decisions.

## Concepts

### The scikit-learn API Pattern

Every model in scikit-learn follows the same pattern:

```python
from sklearn.tree import DecisionTreeClassifier

# 1. Create the model
model = DecisionTreeClassifier()

# 2. Train it on data
model.fit(X_train, y_train)

# 3. Make predictions
predictions = model.predict(X_test)

# 4. Evaluate
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, predictions)
```

### How Decision Trees Work

A decision tree splits the data recursively based on feature values:

```
                Is attendance > 70%?
               /                    \
            Yes                      No
             |                        |
    Is hours_studied > 4?        PREDICT: Fail
    /                  \
  Yes                   No
   |                     |
PREDICT: Pass     Is GPA > 2.5?
                  /            \
                Yes             No
                 |               |
            PREDICT: Pass   PREDICT: Fail
```

### Key Parameters

| Parameter | Description |
|-----------|-------------|
| `max_depth` | Maximum tree depth (prevents overfitting) |
| `min_samples_split` | Minimum samples to split a node |
| `min_samples_leaf` | Minimum samples in a leaf node |
| `random_state` | Seed for reproducibility |

## Practical Examples

### Building a student pass/fail classifier

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Generate student data
np.random.seed(42)
n = 300

hours_studied = np.random.uniform(0, 12, n)
attendance = np.random.uniform(40, 100, n)
previous_gpa = np.random.uniform(1.0, 4.0, n)

# Students pass if they meet at least 2 of 3 criteria
criteria_met = (
    (hours_studied > 4).astype(int) +
    (attendance > 65).astype(int) +
    (previous_gpa > 2.5).astype(int)
)
passed = (criteria_met >= 2).astype(int)
# Add some noise
noise_idx = np.random.choice(n, size=int(n * 0.05), replace=False)
passed[noise_idx] = 1 - passed[noise_idx]

df = pd.DataFrame({
    "hours_studied": hours_studied,
    "attendance": attendance,
    "previous_gpa": previous_gpa,
    "passed": passed,
})

# Prepare features and target
X = df[["hours_studied", "attendance", "previous_gpa"]]
y = df["passed"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train
model = DecisionTreeClassifier(max_depth=4, random_state=42)
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2%}")

# Feature importance
for feature, importance in zip(X.columns, model.feature_importances_):
    print(f"  {feature}: {importance:.3f}")
```

### Visualizing the tree (text format)

```python
from sklearn.tree import export_text

tree_rules = export_text(
    model,
    feature_names=list(X.columns),
    max_depth=3,
)
print(tree_rules)
```

### Comparing predictions with actual values

```python
results = pd.DataFrame({
    "hours": X_test["hours_studied"].values,
    "attendance": X_test["attendance"].values,
    "gpa": X_test["previous_gpa"].values,
    "actual": y_test.values,
    "predicted": predictions,
})
results["correct"] = results["actual"] == results["predicted"]

print("\nSample predictions:")
print(results.head(15).to_string(index=False))

print(f"\nCorrect: {results['correct'].sum()} / {len(results)}")
```

## Guided Practice

1. Run the student pass/fail classifier above.

2. Experiment with `max_depth`:
   - Set `max_depth=1`. What happens to accuracy?
   - Set `max_depth=None` (unlimited). Does accuracy improve on test data?
   - What `max_depth` gives the best test accuracy?

3. Print the decision tree rules for each `max_depth` and observe how complexity changes.

4. Try a different classifier:

```python
from sklearn.neighbors import KNeighborsClassifier

knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)
knn_predictions = knn_model.predict(X_test)
knn_accuracy = accuracy_score(y_test, knn_predictions)
print(f"KNN Accuracy: {knn_accuracy:.2%}")
```

Compare the accuracy of both models.

## Daily Challenge

Build a classifier that predicts whether a student will pass or fail their exam based on multiple features.

### Step 1: Create the dataset

```python
import numpy as np
import pandas as pd

np.random.seed(42)
n = 500

data = {
    "hours_studied_weekly": np.random.uniform(0, 20, n),
    "attendance_pct": np.random.uniform(30, 100, n),
    "assignments_completed": np.random.randint(0, 11, n),  # out of 10
    "previous_test_score": np.random.uniform(20, 100, n),
    "sleep_hours_avg": np.random.uniform(4, 10, n),
}

df = pd.DataFrame(data)

# Determine pass/fail based on a combination of factors
score = (
    df["hours_studied_weekly"] * 2 +
    df["attendance_pct"] * 0.3 +
    df["assignments_completed"] * 3 +
    df["previous_test_score"] * 0.4 +
    df["sleep_hours_avg"] * 1.5 +
    np.random.normal(0, 5, n)  # noise
)
df["passed"] = (score > 75).astype(int)
```

### Step 2: Build the classifier

1. Split the data (80/20 with stratification).
2. Train a `DecisionTreeClassifier` with `max_depth=5`.
3. Calculate accuracy on the test set.
4. Print feature importances, sorted from most to least important.
5. Print the decision tree rules.
6. Show 20 sample predictions with actual values.

### Step 3: Compare models

Train and evaluate at least 3 different configurations:
- `DecisionTreeClassifier(max_depth=3)`
- `DecisionTreeClassifier(max_depth=5)`
- `DecisionTreeClassifier(max_depth=10)`
- `KNeighborsClassifier(n_neighbors=5)`

Create a summary table showing each model's accuracy.

### Step 4: Analysis

Write a brief analysis (in comments or a separate text file):
- Which feature is most important for predicting pass/fail?
- Which model performed best?
- Are there students the model consistently gets wrong? What might explain that?

## Expected Output

```
=== DecisionTreeClassifier (max_depth=5) ===
Accuracy: 92.00%

Feature Importances:
  hours_studied_weekly:  0.35
  attendance_pct:        0.25
  assignments_completed: 0.20
  previous_test_score:   0.12
  sleep_hours_avg:       0.08

=== Model Comparison ===
DecisionTree (depth=3):  89.00%
DecisionTree (depth=5):  92.00%
DecisionTree (depth=10): 90.00%
KNN (k=5):              88.00%
```

## Assessment

1. What is the difference between classification and regression?
2. Why might a decision tree with unlimited depth perform worse on test data than one with `max_depth=5`?
3. What does "feature importance" tell you, and how can it be useful?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-10/day-093/`

Include:
- `student_classifier.py` (your complete solution)
- `analysis.txt` (your analysis of the results)

## Additional Resources

- [scikit-learn Decision Trees](https://scikit-learn.org/stable/modules/tree.html)
- [scikit-learn Classification documentation](https://scikit-learn.org/stable/supervised_learning.html)

## Reflection

- How does a decision tree's structure mirror the way you might make decisions yourself?
- If you were a university administrator using this model, what would you do with the feature importance information?
