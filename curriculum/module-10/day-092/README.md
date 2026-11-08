# Day 092: Data Preparation for Machine Learning

## Learning Objectives

- Understand why data preparation is the most time-consuming and important step in ML.
- Handle categorical data using one-hot encoding and label encoding.
- Apply feature scaling with StandardScaler and MinMaxScaler.
- Split data properly into training and test sets.
- Identify and handle missing values in datasets.

## Introduction

Data scientists often say they spend 80% of their time preparing data and only 20% building models. This is not an exaggeration. A machine learning model is only as good as the data it learns from. If your data has missing values, inconsistent formats, or features on wildly different scales, the model will either fail to train, produce poor predictions, or learn the wrong patterns.

Data preparation, also called data preprocessing, transforms raw data into a format that machine learning algorithms can work with effectively. Most algorithms require numeric input, so categorical values like "male"/"female" or "Kano"/"Lagos"/"Abuja" must be converted to numbers. Many algorithms are sensitive to the scale of features, so a feature measured in millions (like salary) can dominate one measured in single digits (like years of experience) unless you scale them to comparable ranges.

Getting this step right is often the difference between a model that works and one that does not.

## Concepts

### Handling Missing Values

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "name": ["Amina", "Ibrahim", "Fatima", None],
    "age": [22, None, 25, 20],
    "score": [85, 90, None, 78],
})

# Check for missing values
print(df.isnull().sum())

# Strategy 1: Drop rows with any missing values
df_dropped = df.dropna()

# Strategy 2: Fill with a default value
df_filled = df.fillna({"name": "Unknown", "age": df["age"].mean(), "score": 0})

# Strategy 3: Fill with the median (robust to outliers)
df["age"] = df["age"].fillna(df["age"].median())
```

### Encoding Categorical Data

**Label Encoding**: Assigns each category a number (0, 1, 2...). Good for ordinal data (data with a natural order).

```python
from sklearn.preprocessing import LabelEncoder

departments = ["CS", "EE", "ME", "CS", "EE"]
encoder = LabelEncoder()
encoded = encoder.fit_transform(departments)
print(encoded)  # [0, 1, 2, 0, 1]
print(encoder.classes_)  # ['CS', 'EE', 'ME']
```

**One-Hot Encoding**: Creates a binary column for each category. Good for nominal data (no natural order).

```python
import pandas as pd

df = pd.DataFrame({"city": ["Kano", "Lagos", "Abuja", "Kano"]})
one_hot = pd.get_dummies(df, columns=["city"], dtype=int)
print(one_hot)
#    city_Abuja  city_Kano  city_Lagos
# 0          0          1           0
# 1          0          0           1
# 2          1          0           0
# 3          0          1           0
```

### Feature Scaling

**StandardScaler**: Transforms data to have mean=0 and standard deviation=1.

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
data = [[100, 0.5], [200, 0.8], [150, 0.6], [300, 0.9]]
scaled = scaler.fit_transform(data)
print(scaled)
```

**MinMaxScaler**: Transforms data to a [0, 1] range.

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaled = scaler.fit_transform(data)
print(scaled)
```

### Train/Test Split

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,       # 20% for testing
    random_state=42,     # Reproducible split
    stratify=y,          # Maintain class proportions
)
```

## Practical Examples

### Complete data preparation pipeline

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Create a sample dataset
np.random.seed(42)
n = 100

df = pd.DataFrame({
    "age": np.random.randint(18, 35, n),
    "study_hours": np.random.uniform(0, 12, n),
    "department": np.random.choice(["CS", "EE", "ME"], n),
    "scholarship": np.random.choice(["yes", "no"], n),
    "gpa": np.round(np.random.uniform(1.0, 4.0, n), 2),
})

# Add some missing values
df.loc[5, "age"] = None
df.loc[12, "study_hours"] = None
df.loc[20, "gpa"] = None

print("Before preparation:")
print(df.head(10))
print(f"\nMissing values:\n{df.isnull().sum()}")

# Step 1: Handle missing values
df["age"] = df["age"].fillna(df["age"].median())
df["study_hours"] = df["study_hours"].fillna(df["study_hours"].mean())
df["gpa"] = df["gpa"].fillna(df["gpa"].median())

# Step 2: Encode categorical variables
# Label encode binary column
le = LabelEncoder()
df["scholarship_encoded"] = le.fit_transform(df["scholarship"])

# One-hot encode multi-category column
df = pd.get_dummies(df, columns=["department"], dtype=int)

# Step 3: Define features and target
target = (df["gpa"] >= 3.0).astype(int)  # Binary: high GPA or not

feature_columns = [
    "age", "study_hours", "scholarship_encoded",
    "department_CS", "department_EE", "department_ME",
]
X = df[feature_columns]
y = target

# Step 4: Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Step 5: Scale numeric features
scaler = StandardScaler()
numeric_cols = ["age", "study_hours"]
X_train[numeric_cols] = scaler.fit_transform(X_train[numeric_cols])
X_test[numeric_cols] = scaler.transform(X_test[numeric_cols])  # Use same scaler

print("\nAfter preparation:")
print(f"Training set: {X_train.shape}")
print(f"Test set: {X_test.shape}")
print(f"\nFirst 5 training samples:")
print(X_train.head())
```

## Guided Practice

1. Create a dataset of 150 students with these columns:
   - `name` (string)
   - `age` (integer, 16-25)
   - `gender` (categorical: M/F)
   - `state` (categorical: at least 5 Nigerian states)
   - `hours_studied` (float, 0-15)
   - `attendance_rate` (float, 0.0-1.0)
   - `passed` (binary: 0 or 1)

2. Randomly insert 10 missing values across numeric columns.

3. Perform the full preparation pipeline:
   - Check and report missing values.
   - Fill missing values appropriately.
   - Label encode `gender`.
   - One-hot encode `state`.
   - Split into 80/20 train/test with stratification.
   - Scale numeric features using StandardScaler.

4. Print the shape and first 5 rows of the prepared training set.

## Daily Challenge

You are given a CSV file with the following structure. Create the CSV first, then build the complete preparation pipeline.

Create `student_data.csv`:

```python
import pandas as pd
import numpy as np

np.random.seed(42)
n = 200

states = ["Kano", "Lagos", "Abuja", "Kaduna", "Borno", "Sokoto"]
departments = ["Computer Science", "Electrical Engineering",
               "Mechanical Engineering", "Civil Engineering"]

df = pd.DataFrame({
    "student_id": range(1, n + 1),
    "age": np.random.randint(17, 30, n),
    "gender": np.random.choice(["M", "F"], n),
    "state": np.random.choice(states, n),
    "department": np.random.choice(departments, n),
    "year_of_study": np.random.randint(1, 5, n),
    "hours_studied_weekly": np.round(np.random.uniform(0, 20, n), 1),
    "attendance_pct": np.round(np.random.uniform(30, 100, n), 1),
    "previous_cgpa": np.round(np.random.uniform(1.0, 4.5, n), 2),
    "has_laptop": np.random.choice(["yes", "no"], n, p=[0.6, 0.4]),
    "current_cgpa": np.round(np.random.uniform(1.0, 4.5, n), 2),
})

# Add missing values
for col in ["age", "hours_studied_weekly", "attendance_pct", "previous_cgpa"]:
    mask = np.random.choice(n, size=8, replace=False)
    df.loc[mask, col] = np.nan

df.to_csv("student_data.csv", index=False)
```

Write a script `prepare_data.py` that:

1. Loads the CSV file.
2. Prints a data summary (shape, dtypes, missing values, descriptive statistics).
3. Handles all missing values with appropriate strategies.
4. Drops `student_id` (not a useful feature) and `current_cgpa` (this is the target).
5. Creates a binary target: `high_performer = 1 if current_cgpa >= 3.0 else 0`.
6. Encodes all categorical variables.
7. Splits into train/test (80/20) with stratification.
8. Scales all numeric features using StandardScaler.
9. Saves the prepared training and test sets to `train_prepared.csv` and `test_prepared.csv`.
10. Prints a summary of the prepared data.

## Expected Output

```
=== Data Summary ===
Shape: (200, 11)
Missing values:
  age                    8
  hours_studied_weekly   8
  attendance_pct         8
  previous_cgpa          8

=== After Preparation ===
Training features shape: (160, 14)
Test features shape: (40, 14)
Feature columns: ['age', 'year_of_study', 'hours_studied_weekly', ...]
Target distribution (train): {0: 72, 1: 88}
```

## Assessment

1. Why is it important to use `scaler.transform()` on the test set instead of `scaler.fit_transform()`?
2. When would you choose one-hot encoding over label encoding?
3. What could go wrong if you scale your data before splitting into train and test sets?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-10/day-092/`

Include:
- `prepare_data.py`
- `student_data.csv` (generated dataset)
- `train_prepared.csv` and `test_prepared.csv`

## Additional Resources

- [scikit-learn Preprocessing documentation](https://scikit-learn.org/stable/modules/preprocessing.html)
- [Pandas handling missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html)

## Reflection

- Why do you think data preparation takes more time than model building in real-world projects?
- What problems could arise if you deployed a model trained on poorly prepared data?
