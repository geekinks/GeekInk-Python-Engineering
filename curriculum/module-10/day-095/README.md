# Day 095: Model Evaluation

## Learning Objectives

- Evaluate classification models using confusion matrix, precision, recall, and F1-score.
- Understand the trade-off between precision and recall.
- Use cross-validation for more reliable model evaluation.
- Recognize overfitting and underfitting from evaluation metrics.
- Choose appropriate evaluation metrics for different problems.

## Introduction

Accuracy tells you what percentage of predictions were correct, but it can be misleading. Imagine a disease screening model where only 1% of patients have the disease. A model that always predicts "no disease" achieves 99% accuracy while being completely useless --- it never catches a single sick patient. For problems like this, you need metrics that tell a more nuanced story about model performance.

The confusion matrix breaks down predictions into four categories: true positives (correctly predicted positive), true negatives (correctly predicted negative), false positives (predicted positive but actually negative), and false negatives (predicted negative but actually positive). From these four numbers, you derive precision (of the ones you predicted positive, how many actually were?) and recall (of the ones that were actually positive, how many did you catch?).

Cross-validation goes further by testing the model multiple times on different subsets of the data. Instead of a single train/test split, it gives you a more reliable estimate of how the model will perform on truly unseen data.

## Concepts

### Confusion Matrix

```
                    Predicted
                 Positive  Negative
Actual Positive    TP        FN
Actual Negative    FP        TN
```

- **TP (True Positive)**: Predicted positive, actually positive.
- **TN (True Negative)**: Predicted negative, actually negative.
- **FP (False Positive)**: Predicted positive, actually negative (Type I error).
- **FN (False Negative)**: Predicted negative, actually positive (Type II error).

### Metrics Derived from Confusion Matrix

| Metric | Formula | What it measures |
|--------|---------|-----------------|
| Accuracy | (TP + TN) / Total | Overall correctness |
| Precision | TP / (TP + FP) | Of predicted positives, how many are correct? |
| Recall (Sensitivity) | TP / (TP + FN) | Of actual positives, how many did we catch? |
| F1-Score | 2 * (Precision * Recall) / (Precision + Recall) | Harmonic mean of precision and recall |

### When to Prioritize Which Metric

- **Precision matters most** when false positives are costly: spam filter (marking good email as spam is annoying).
- **Recall matters most** when false negatives are costly: disease screening (missing a sick patient is dangerous).
- **F1 balances both** when you want a single number that considers both.

### Cross-Validation

Instead of one train/test split, cross-validation:
1. Divides data into K equal parts (folds).
2. Trains on K-1 folds, tests on the remaining fold.
3. Repeats K times, each fold serving as the test set once.
4. Averages the K results.

### Overfitting vs Underfitting

- **Overfitting**: Model memorizes training data, performs well on training but poorly on test data.
- **Underfitting**: Model is too simple, performs poorly on both training and test data.

## Practical Examples

### Complete evaluation of the student classifier

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score, confusion_matrix, classification_report,
    precision_score, recall_score, f1_score,
)

# Generate data (same as Day 093)
np.random.seed(42)
n = 500

data = {
    "hours_studied": np.random.uniform(0, 12, n),
    "attendance": np.random.uniform(40, 100, n),
    "assignments": np.random.randint(0, 11, n),
    "prev_score": np.random.uniform(20, 100, n),
}
df = pd.DataFrame(data)

criteria = (
    (df["hours_studied"] > 4).astype(int) +
    (df["attendance"] > 65).astype(int) +
    (df["prev_score"] > 55).astype(int)
)
df["passed"] = (criteria >= 2).astype(int)
noise_idx = np.random.choice(n, size=int(n * 0.05), replace=False)
df.loc[noise_idx, "passed"] = 1 - df.loc[noise_idx, "passed"]

X = df[["hours_studied", "attendance", "assignments", "prev_score"]]
y = df["passed"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = DecisionTreeClassifier(max_depth=4, random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)

# --- Confusion Matrix ---
cm = confusion_matrix(y_test, predictions)
print("Confusion Matrix:")
print(cm)
print(f"  True Negatives:  {cm[0][0]}")
print(f"  False Positives: {cm[0][1]}")
print(f"  False Negatives: {cm[1][0]}")
print(f"  True Positives:  {cm[1][1]}")

# --- Classification Report ---
print("\nClassification Report:")
print(classification_report(y_test, predictions, target_names=["Fail", "Pass"]))

# --- Individual Metrics ---
print(f"Accuracy:  {accuracy_score(y_test, predictions):.4f}")
print(f"Precision: {precision_score(y_test, predictions):.4f}")
print(f"Recall:    {recall_score(y_test, predictions):.4f}")
print(f"F1-Score:  {f1_score(y_test, predictions):.4f}")

# --- Cross-Validation ---
cv_scores = cross_val_score(model, X, y, cv=5, scoring="f1")
print(f"\n5-Fold Cross-Validation F1 Scores: {cv_scores}")
print(f"Mean F1: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")
```

### Detecting overfitting

```python
# Train on full training set and evaluate on both train and test
model.fit(X_train, y_train)

train_accuracy = accuracy_score(y_train, model.predict(X_train))
test_accuracy = accuracy_score(y_test, predictions)

print(f"\nTrain accuracy: {train_accuracy:.4f}")
print(f"Test accuracy:  {test_accuracy:.4f}")

if train_accuracy - test_accuracy > 0.1:
    print("Warning: Possible overfitting (large gap between train and test)")

# Compare different depths
print("\nOverfitting analysis:")
for depth in [1, 2, 3, 5, 10, None]:
    m = DecisionTreeClassifier(max_depth=depth, random_state=42)
    m.fit(X_train, y_train)
    train_acc = accuracy_score(y_train, m.predict(X_train))
    test_acc = accuracy_score(y_test, m.predict(X_test))
    gap = train_acc - test_acc
    label = f"depth={depth}" if depth else "depth=unlimited"
    print(f"  {label:20s}  Train: {train_acc:.4f}  Test: {test_acc:.4f}  Gap: {gap:.4f}")
```

## Guided Practice

1. Run the complete evaluation example above.

2. Examine the confusion matrix. Answer:
   - How many students were correctly predicted to pass?
   - How many students were predicted to pass but actually failed?
   - How many students were predicted to fail but actually passed?

3. Change the class balance: make only 15% of students pass (change the threshold). Run the evaluation again. How do precision and recall change?

4. Run the overfitting analysis. At which depth does the gap between train and test accuracy start to grow?

## Daily Challenge

Perform a thorough evaluation of the Day 093 student pass/fail classifier.

### Requirements

1. **Build the classifier** using the dataset from Day 093 (or generate a new one with at least 500 samples).

2. **Compute and display**:
   - Confusion matrix with labeled rows and columns.
   - Accuracy, precision, recall, and F1-score.
   - Full classification report.

3. **Cross-validation**:
   - Perform 5-fold and 10-fold cross-validation.
   - Report mean and standard deviation for accuracy and F1-score.

4. **Overfitting analysis**:
   - Train models with `max_depth` values of 1, 2, 3, 5, 10, 15, and None.
   - For each, report train accuracy and test accuracy.
   - Identify the best depth (highest test accuracy without significant overfitting).

5. **Model comparison**:
   - Compare `DecisionTreeClassifier` and `KNeighborsClassifier` (try k=3, 5, 7).
   - For each model, report accuracy, precision, recall, and F1 using cross-validation.
   - Create a summary table.

6. **Analysis**:
   - Which model performed best overall?
   - Is precision or recall more important for predicting student failure? Justify your answer.
   - At what tree depth does overfitting become a problem?

## Expected Output

```
=== Confusion Matrix ===
              Predicted Fail  Predicted Pass
Actual Fail            35              5
Actual Pass             3             57

=== Metrics ===
Accuracy:  0.9200
Precision: 0.9194
Recall:    0.9500
F1-Score:  0.9344

=== Cross-Validation (5-fold) ===
Accuracy: 0.9120 (+/- 0.0250)
F1-Score: 0.9300 (+/- 0.0180)

=== Overfitting Analysis ===
Depth   Train Acc   Test Acc    Gap
1       0.8200      0.8100      0.0100
3       0.9100      0.9050      0.0050
5       0.9400      0.9200      0.0200
10      0.9900      0.9100      0.0800  <-- overfitting starts
None    1.0000      0.8900      0.1100  <-- overfitting

Best depth: 5

=== Model Comparison ===
Model               Accuracy    Precision   Recall   F1
DecisionTree(d=5)   0.9200      0.9194      0.9500   0.9344
KNN(k=3)            0.8800      0.8700      0.9200   0.8944
KNN(k=5)            0.9000      0.8900      0.9300   0.9096
KNN(k=7)            0.8900      0.8850      0.9250   0.9046
```

## Assessment

1. A model has 95% accuracy but only 40% recall for the positive class. What does this mean in practical terms?
2. Explain why a model with 100% train accuracy and 70% test accuracy is problematic.
3. How does 5-fold cross-validation give a more reliable estimate than a single train/test split?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-10/day-095/`

Include:
- `model_evaluation.py` (complete evaluation script)
- `evaluation_report.txt` (your analysis)

## Additional Resources

- [scikit-learn Model Evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html)
- [scikit-learn Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html)

## Reflection

- Before today, did you think accuracy was sufficient for evaluating a model? How has your thinking changed?
- In a school context, which is worse: telling a passing student they will fail, or telling a failing student they will pass? How does this relate to precision vs recall?
