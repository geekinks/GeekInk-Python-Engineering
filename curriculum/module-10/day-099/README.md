# Day 099: Building AI-Powered Applications

## Learning Objectives

- Combine machine learning models with web applications to serve predictions.
- Serialize trained models using pickle and joblib for reuse.
- Build a FastAPI endpoint that accepts input and returns predictions.
- Structure an end-to-end ML project from training to deployment.
- Understand the ML application lifecycle: train, save, load, serve.

## Introduction

Training a model in a Jupyter notebook is only half the work. For a model to be useful, real users need to interact with it. This means building an application --- a web API, a desktop tool, or a mobile app --- that accepts user input, passes it through the trained model, and returns the prediction in a useful format.

The standard approach is to train and save the model as a separate step, then build an API that loads the saved model and uses it to make predictions on incoming requests. This separation means you can retrain the model without changing the API code, and you can scale the API independently of the training process.

Today you will build a complete pipeline: generate data, train a model, save it, build a FastAPI application that loads the model and serves predictions, and write tests to verify it all works together.

## Concepts

### Model Serialization

Serialization means saving a Python object to a file so you can reload it later without retraining.

**pickle** (Python standard library):
```python
import pickle

# Save
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

# Load
with open("model.pkl", "rb") as f:
    loaded_model = pickle.load(f)
```

**joblib** (better for large NumPy arrays):
```python
import joblib

# Save
joblib.dump(model, "model.joblib")

# Load
loaded_model = joblib.load("model.joblib")
```

### End-to-End Project Structure

```
ml-app/
├── train.py          # Train and save the model
├── model.joblib      # Saved model
├── scaler.joblib     # Saved scaler
├── app.py            # FastAPI application
├── requirements.txt
└── tests/
    └── test_app.py
```

### The ML Serving Pattern

1. **Train** the model on historical data.
2. **Save** the trained model and any preprocessors (scalers, encoders).
3. **Load** them in the API at startup.
4. **Predict** on incoming requests using the loaded model.

## Practical Examples

### Step 1: Train and save the model

```python
# train.py

import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Generate training data
np.random.seed(42)
n = 500

data = {
    "hours_studied": np.random.uniform(0, 12, n),
    "attendance_pct": np.random.uniform(40, 100, n),
    "assignments_done": np.random.randint(0, 11, n),
    "previous_score": np.random.uniform(30, 100, n),
}
df = pd.DataFrame(data)

# Target: pass if strong enough combination of factors
score = (
    df["hours_studied"] * 3 +
    df["attendance_pct"] * 0.4 +
    df["assignments_done"] * 4 +
    df["previous_score"] * 0.3 +
    np.random.normal(0, 5, n)
)
df["passed"] = (score > 75).astype(int)

# Features and target
feature_cols = ["hours_studied", "attendance_pct", "assignments_done", "previous_score"]
X = df[feature_cols]
y = df["passed"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scale
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train
model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train_scaled, y_train)

# Evaluate
predictions = model.predict(X_test_scaled)
print("Model Performance:")
print(f"Accuracy: {accuracy_score(y_test, predictions):.2%}")
print(classification_report(y_test, predictions, target_names=["Fail", "Pass"]))

# Save
joblib.dump(model, "model.joblib")
joblib.dump(scaler, "scaler.joblib")
joblib.dump(feature_cols, "features.joblib")
print("Model, scaler, and feature list saved.")
```

### Step 2: Build the API

```python
# app.py

import joblib
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# Load model and scaler at startup
model = joblib.load("model.joblib")
scaler = joblib.load("scaler.joblib")
feature_names = joblib.load("features.joblib")

app = FastAPI(title="Student Pass/Fail Predictor")


class StudentInput(BaseModel):
    """Input data for a student prediction."""
    hours_studied: float = Field(ge=0, le=24, description="Weekly study hours")
    attendance_pct: float = Field(ge=0, le=100, description="Attendance percentage")
    assignments_done: int = Field(ge=0, le=10, description="Assignments completed out of 10")
    previous_score: float = Field(ge=0, le=100, description="Previous test score")


class PredictionResponse(BaseModel):
    """Prediction result."""
    prediction: str
    passed: bool
    confidence: float
    input_data: dict


@app.get("/")
def root():
    return {
        "service": "Student Pass/Fail Predictor",
        "version": "1.0.0",
        "endpoints": {
            "/predict": "POST - Make a prediction",
            "/health": "GET - Check service health",
        },
    }


@app.get("/health")
def health():
    return {"status": "healthy", "model_loaded": model is not None}


@app.post("/predict", response_model=PredictionResponse)
def predict(student: StudentInput):
    """Predict whether a student will pass or fail."""
    features = np.array([[
        student.hours_studied,
        student.attendance_pct,
        student.assignments_done,
        student.previous_score,
    ]])

    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)[0]
    probabilities = model.predict_proba(features_scaled)[0]
    confidence = float(max(probabilities))

    return PredictionResponse(
        prediction="Pass" if prediction == 1 else "Fail",
        passed=bool(prediction),
        confidence=round(confidence, 4),
        input_data=student.model_dump(),
    )


@app.post("/predict/batch")
def predict_batch(students: list[StudentInput]):
    """Predict for multiple students at once."""
    results = []
    for student in students:
        features = np.array([[
            student.hours_studied,
            student.attendance_pct,
            student.assignments_done,
            student.previous_score,
        ]])
        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)[0]
        probabilities = model.predict_proba(features_scaled)[0]

        results.append({
            "prediction": "Pass" if prediction == 1 else "Fail",
            "passed": bool(prediction),
            "confidence": round(float(max(probabilities)), 4),
        })

    return {"predictions": results, "count": len(results)}
```

### Step 3: Test the API

```python
# test_app.py

import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Student Pass/Fail Predictor" in response.json()["service"]


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_predict_pass():
    response = client.post("/predict", json={
        "hours_studied": 8,
        "attendance_pct": 90,
        "assignments_done": 9,
        "previous_score": 85,
    })
    assert response.status_code == 200
    data = response.json()
    assert data["prediction"] in ["Pass", "Fail"]
    assert "confidence" in data


def test_predict_fail():
    response = client.post("/predict", json={
        "hours_studied": 1,
        "attendance_pct": 40,
        "assignments_done": 2,
        "previous_score": 30,
    })
    assert response.status_code == 200


def test_predict_validation():
    response = client.post("/predict", json={
        "hours_studied": -1,  # Invalid
        "attendance_pct": 90,
        "assignments_done": 9,
        "previous_score": 85,
    })
    assert response.status_code == 422  # Validation error


def test_predict_batch():
    students = [
        {"hours_studied": 8, "attendance_pct": 90,
         "assignments_done": 9, "previous_score": 85},
        {"hours_studied": 2, "attendance_pct": 50,
         "assignments_done": 3, "previous_score": 40},
    ]
    response = client.post("/predict/batch", json=students)
    assert response.status_code == 200
    assert response.json()["count"] == 2
```

### Running the application

```bash
# 1. Train the model
python train.py

# 2. Start the API
uvicorn app:app --reload

# 3. Test with curl
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"hours_studied": 7, "attendance_pct": 85, "assignments_done": 8, "previous_score": 75}'

# 4. Run tests
pytest test_app.py -v
```

## Guided Practice

1. Run `train.py` to train and save the model.
2. Run `app.py` with uvicorn and test the endpoints.
3. Send 5 different prediction requests and examine the responses.
4. Run the test suite.
5. Modify the model: retrain with `max_depth=3` instead of 5. Save it (overwriting the old file). Restart the API. Does it still work? How has the confidence changed?

## Daily Challenge

Build a complete AI-powered application that predicts house affordability.

### Requirements

1. **train.py**: Generate house data (area, bedrooms, bathrooms, age, location category). Train a model that predicts whether a house is "Affordable" (below a threshold) or "Premium". Save the model, scaler, and any encoders.

2. **app.py**: FastAPI application with:
   - `POST /predict` --- Predict if a house is affordable or premium.
   - `POST /predict/batch` --- Batch predictions.
   - `GET /model/info` --- Return model metadata (features used, training date, accuracy).
   - `GET /health` --- Health check.

3. **test_app.py**: At least 10 tests covering all endpoints, valid inputs, invalid inputs, and edge cases.

4. **requirements.txt**: List all dependencies.

5. **README.md**: Project documentation with setup, usage, and API reference.

The project should be structured properly:

```
house-predictor/
├── README.md
├── requirements.txt
├── train.py
├── app.py
├── model.joblib
├── scaler.joblib
└── tests/
    └── test_app.py
```

## Expected Output

```bash
$ python train.py
Training model on 500 samples...
Accuracy: 91.00%
Model saved to model.joblib

$ pytest tests/ -v
tests/test_app.py::test_root PASSED
tests/test_app.py::test_health PASSED
tests/test_app.py::test_predict_affordable PASSED
...
10 passed in 0.5s

$ curl -X POST http://localhost:8000/predict \
    -H "Content-Type: application/json" \
    -d '{"area_sqm": 80, "bedrooms": 2, "bathrooms": 1, "age_years": 5, "location": "suburban"}'
{
    "prediction": "Affordable",
    "confidence": 0.87,
    "input_data": {...}
}
```

## Assessment

1. Why do we save the scaler along with the model?
2. What would happen if you scaled the input data differently at prediction time than during training?
3. What are the advantages of serving an ML model through an API compared to running it directly in a script?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-10/day-099/`

Include the complete project directory.

## Additional Resources

- [FastAPI documentation](https://fastapi.tiangolo.com/)
- [joblib documentation](https://joblib.readthedocs.io/)
- [scikit-learn Model Persistence](https://scikit-learn.org/stable/model_persistence.html)

## Reflection

- You have now built an end-to-end ML application: data, training, saving, serving, and testing. Which step was most challenging?
- How would you monitor this application in production to ensure the model continues to perform well?
