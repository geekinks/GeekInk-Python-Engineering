# Day 094: Supervised Learning - Regression

## Learning Objectives

- Understand regression as predicting continuous numeric values.
- Build a linear regression model using scikit-learn.
- Evaluate regression models with mean squared error and R-squared.
- Interpret regression coefficients to understand feature relationships.
- Compare linear regression with other regression approaches.

## Introduction

Yesterday you learned classification, where the model predicts a category (pass or fail). Regression is the other major type of supervised learning, where the model predicts a continuous number: a house price, a temperature, a salary, a test score. The fundamental approach is the same --- train on labeled data, make predictions on new data --- but the evaluation metrics are different because you are measuring how close predictions are to the actual values, not whether they exactly match.

Linear regression is the simplest and most widely used regression algorithm. It fits a straight line (or a flat plane in multiple dimensions) through the data that best captures the relationship between features and the target. "Best" means the line that minimizes the total squared distance between the predicted values and the actual values.

Linear regression is often the first model to try because it is fast, interpretable, and works well when the relationship between features and target is approximately linear. Its coefficients tell you exactly how much each feature contributes to the prediction.

## Concepts

### Linear Regression

For a single feature:
```
predicted_price = intercept + coefficient * feature_value
```

For multiple features:
```
predicted_price = intercept + c1*feature1 + c2*feature2 + c3*feature3
```

### Evaluation Metrics

**Mean Squared Error (MSE)**: Average of squared differences between predicted and actual values. Lower is better.

**Root Mean Squared Error (RMSE)**: Square root of MSE. In the same units as the target.

**R-squared (R2)**: Proportion of variance in the target explained by the model. Ranges from 0 to 1. Higher is better. An R2 of 0.85 means the model explains 85% of the variation.

```python
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, predictions)
```

### Interpreting Coefficients

```python
# If the coefficient for 'square_meters' is 15000,
# it means: for every additional square meter,
# the predicted price increases by 15,000.
```

## Practical Examples

### Predicting house prices

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Generate house price data
np.random.seed(42)
n = 200

square_meters = np.random.uniform(50, 300, n)
bedrooms = np.random.randint(1, 6, n)
age_years = np.random.uniform(0, 30, n)
distance_to_center_km = np.random.uniform(1, 25, n)

# Price formula with some noise
price = (
    500_000 +
    square_meters * 12_000 +
    bedrooms * 200_000 +
    age_years * -15_000 +
    distance_to_center_km * -30_000 +
    np.random.normal(0, 100_000, n)
)

df = pd.DataFrame({
    "square_meters": square_meters,
    "bedrooms": bedrooms,
    "age_years": age_years,
    "distance_km": distance_to_center_km,
    "price": price,
})

# Prepare features and target
X = df[["square_meters", "bedrooms", "age_years", "distance_km"]]
y = df["price"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, predictions)

print(f"RMSE: {rmse:,.0f}")
print(f"R-squared: {r2:.4f}")

# Interpret coefficients
print("\nCoefficients:")
print(f"  Intercept: {model.intercept_:,.0f}")
for feature, coef in zip(X.columns, model.coef_):
    print(f"  {feature}: {coef:,.0f}")

# Sample predictions vs actual
print("\nSample predictions:")
comparison = pd.DataFrame({
    "actual": y_test.values[:10],
    "predicted": predictions[:10],
})
comparison["error"] = comparison["actual"] - comparison["predicted"]
comparison["error_pct"] = (
    abs(comparison["error"]) / comparison["actual"] * 100
)
print(comparison.to_string(index=False, float_format=lambda x: f"{x:,.0f}"))
```

### Predicting with a single feature (for visualization)

```python
import numpy as np
from sklearn.linear_model import LinearRegression

# Predict score based on hours studied
hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
scores = np.array([35, 42, 50, 55, 63, 68, 75, 80, 85, 90])

model = LinearRegression()
model.fit(hours, scores)

print(f"Score = {model.intercept_:.1f} + {model.coef_[0]:.1f} * hours_studied")
print(f"R-squared: {model.score(hours, scores):.4f}")

# Predict for a student who studies 6.5 hours
new_hours = np.array([[6.5]])
predicted_score = model.predict(new_hours)
print(f"Predicted score for 6.5 hours: {predicted_score[0]:.1f}")
```

## Guided Practice

1. Run the house price prediction example above.

2. Add a new feature to the dataset:
   ```python
   has_parking = np.random.choice([0, 1], n, p=[0.4, 0.6])
   ```
   Include `has_parking` as a feature that adds 150,000 to the price. Retrain and see if R-squared improves.

3. Try predicting with only one feature at a time. Which single feature gives the best R-squared?

4. Try a different regression model:
   ```python
   from sklearn.tree import DecisionTreeRegressor

   tree_model = DecisionTreeRegressor(max_depth=5, random_state=42)
   tree_model.fit(X_train, y_train)
   tree_predictions = tree_model.predict(X_test)
   tree_r2 = r2_score(y_test, tree_predictions)
   print(f"Decision Tree R-squared: {tree_r2:.4f}")
   ```

## Daily Challenge

Build a regression model to predict house prices in a Nigerian city context.

### Step 1: Create the dataset

```python
import numpy as np
import pandas as pd

np.random.seed(42)
n = 400

data = {
    "area_sqm": np.random.uniform(40, 500, n),
    "bedrooms": np.random.randint(1, 7, n),
    "bathrooms": np.random.randint(1, 4, n),
    "age_years": np.random.uniform(0, 25, n),
    "distance_to_market_km": np.random.uniform(0.5, 15, n),
    "has_generator": np.random.choice([0, 1], n, p=[0.3, 0.7]),
    "has_borehole": np.random.choice([0, 1], n, p=[0.5, 0.5]),
    "floor_level": np.random.randint(0, 5, n),  # 0 = ground floor
}

df = pd.DataFrame(data)

# Generate price based on features
df["price_naira"] = (
    2_000_000 +
    df["area_sqm"] * 25_000 +
    df["bedrooms"] * 500_000 +
    df["bathrooms"] * 300_000 +
    df["age_years"] * -80_000 +
    df["distance_to_market_km"] * -100_000 +
    df["has_generator"] * 400_000 +
    df["has_borehole"] * 300_000 +
    df["floor_level"] * 50_000 +
    np.random.normal(0, 500_000, n)
)

df.to_csv("house_prices.csv", index=False)
```

### Step 2: Build and evaluate models

1. Load the CSV, split into train/test (80/20).
2. Train a `LinearRegression` model.
3. Calculate RMSE and R-squared.
4. Print coefficients with interpretation.
5. Show 15 sample predictions with actual values and percentage error.

### Step 3: Compare models

Train and compare:
- `LinearRegression`
- `DecisionTreeRegressor(max_depth=5)`
- `DecisionTreeRegressor(max_depth=10)`

Create a comparison table with RMSE and R-squared for each.

### Step 4: Feature analysis

- Which feature has the largest positive coefficient?
- Which feature has the largest negative coefficient?
- If you could only use 3 features, which would you choose and why?

## Expected Output

```
=== Linear Regression ===
RMSE: 520,000
R-squared: 0.9200

Coefficients:
  Intercept: 1,950,000
  area_sqm: 24,800
  bedrooms: 510,000
  ...

=== Model Comparison ===
Model                    RMSE         R-squared
LinearRegression         520,000      0.9200
DecisionTree (depth=5)   480,000      0.9350
DecisionTree (depth=10)  510,000      0.9280
```

## Assessment

1. What is the difference between classification and regression in terms of the target variable?
2. If your linear regression model has an R-squared of 0.45, what does that mean?
3. How do you interpret a negative coefficient in a linear regression model?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-10/day-094/`

Include:
- `house_price_predictor.py`
- `house_prices.csv`
- `analysis.txt` (feature analysis)

## Additional Resources

- [scikit-learn Linear Regression](https://scikit-learn.org/stable/modules/linear_model.html)
- [Understanding R-squared](https://scikit-learn.org/stable/modules/model_evaluation.html#r2-score)

## Reflection

- How could a house price prediction model be useful for someone looking to buy or rent a home?
- What real-world factors affect house prices that our model does not capture? How would you add them?
