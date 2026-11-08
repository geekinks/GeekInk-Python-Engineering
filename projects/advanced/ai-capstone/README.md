# AI-Powered Capstone Project

**Module:** 10 — AI, Machine Learning and Capstone
**Day:** 100
**Difficulty:** Advanced

---

## Problem Statement

The final capstone project challenges students to identify a real-world problem and build an AI-powered Python solution that addresses it. This is the culmination of the 100-day program — students must demonstrate mastery of Python fundamentals, software engineering practices, and machine learning concepts by delivering a complete, working application with a trained model, an API for serving predictions, documentation, and a technical presentation.

## Objectives

- Identify a meaningful problem that can be addressed with machine learning.
- Collect, clean, and prepare a dataset for model training.
- Train and evaluate a machine learning model using scikit-learn.
- Serve model predictions through a REST API.
- Document the project professionally.
- Present and defend technical decisions.

## Requirements

### Problem Selection

Students must choose a problem relevant to their interests or community. Suggested domains:

- **Education:** Predict student performance based on attendance and study habits.
- **Agriculture:** Classify crop health from environmental data.
- **Health:** Predict disease risk from lifestyle factors.
- **Finance:** Detect anomalous transactions.
- **Language:** Classify text sentiment or topic.
- **Environment:** Predict air quality or weather patterns.

The problem must be scoped to be achievable with the tools and data available.

### Technical Requirements

1. **Data preparation:**
   - Dataset with at least 200 rows and 4+ features.
   - Documented data source and collection method.
   - Cleaning, encoding, and scaling applied and documented.
   - Train/test split (at least 80/20).

2. **Model training:**
   - At least 2 models compared (e.g., Decision Tree vs Logistic Regression).
   - Evaluation metrics reported (accuracy, precision, recall, F1-score).
   - Best model selected with justification.

3. **API serving:**
   - A FastAPI endpoint that accepts input features and returns predictions.
   - Pydantic models for request/response validation.
   - Model loaded from a serialized file (pickle or joblib).

4. **Documentation:**
   - README with problem statement, approach, results, and usage instructions.
   - Jupyter notebook showing the analysis and training process.
   - Architecture diagram (text-based is acceptable).

5. **Presentation:**
   - 10-minute technical presentation.
   - Cover: problem, data, approach, results, demo, lessons learned.
   - Be prepared to answer technical questions (defense).

### Responsible AI

- Document any potential biases in the dataset.
- Discuss limitations of the model.
- Consider privacy implications of the data used.
- Do not use personally identifiable information without consent.

## Technologies

- Python 3.10+
- scikit-learn
- Pandas, NumPy
- FastAPI, uvicorn
- Jupyter Notebook
- Matplotlib or Plotly (for visualizations)
- pickle or joblib (model serialization)

## Suggested Architecture

```
ai-capstone/
├── README.md              — Project overview and instructions
├── notebooks/
│   └── analysis.ipynb     — Data exploration, cleaning, training
├── src/
│   ├── main.py            — FastAPI application
│   ├── model.py           — Model loading and prediction logic
│   └── schemas.py         — Pydantic schemas
├── models/
│   └── best_model.pkl     — Serialized trained model
├── data/
│   ├── raw/               — Original dataset
│   └── processed/         — Cleaned dataset
├── tests/
│   └── test_api.py        — API tests
├── requirements.txt
└── presentation/
    └── slides.md          — Presentation outline or slides
```

## Implementation Milestones

| Milestone | Description |
| :--- | :--- |
| 1. Problem definition | Define the problem, identify data sources |
| 2. Data preparation | Collect, clean, and explore the dataset |
| 3. Model training | Train, evaluate, and compare models |
| 4. API development | Build FastAPI endpoints for predictions |
| 5. Documentation | Write README, complete the notebook narrative |
| 6. Testing | Test the API and verify predictions |
| 7. Presentation | Prepare slides and practice the defense |

## Testing Requirements

- Model accuracy must be reported honestly (no cherry-picking).
- API must return correct predictions for sample inputs.
- API must handle invalid inputs gracefully.
- All code must run without errors.

## Expected Deliverables

1. Complete source code with the directory structure above.
2. Jupyter notebook with the full analysis workflow.
3. Trained model file.
4. Working API with at least one prediction endpoint.
5. README with clear setup and usage instructions.
6. Presentation materials.

## Evaluation Criteria

| Criterion | Weight | Description |
| :--- | :--- | :--- |
| Problem selection and framing | 10% | Meaningful problem, clear scope |
| Data handling | 15% | Thorough cleaning, proper preparation |
| Model quality | 20% | Appropriate models, fair evaluation, justified selection |
| API implementation | 15% | Working endpoint, validation, error handling |
| Code quality | 10% | Clean, organized, PEP 8, type hints |
| Documentation | 15% | Complete README, narrative notebook |
| Presentation and defense | 15% | Clear delivery, answers questions confidently |

## Presentation Guidelines

### Structure

1. **Introduction** (2 minutes) — The problem and why it matters.
2. **Data** (2 minutes) — Source, size, features, cleaning process.
3. **Approach** (2 minutes) — Models tried, evaluation metrics, results.
4. **Demo** (2 minutes) — Live demonstration of the API.
5. **Lessons learned** (2 minutes) — Challenges, what you would do differently.

### Defense Questions (Examples)

- Why did you choose this model over alternatives?
- What are the limitations of your approach?
- How would you improve the model with more time?
- What ethical considerations apply to your project?
- How would you deploy this in production?
