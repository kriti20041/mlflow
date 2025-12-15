# ML Experiment Tracking & Automated Model Selection

## Overview
This project demonstrates an end-to-end machine learning experiment tracking and model lifecycle workflow using **MLflow**, with an added automation layer for **best model selection**.
The focus of this project is not only on model training, but on **experiment reproducibility, comparison, and automated decision-making**, which are essential in production-grade AI/ML systems.

## Problem Statement
In typical machine learning workflows:
- Multiple experiments are run with different parameters
- Results are logged, but model selection is often manual
- Reproducibility and consistency degrade as experiments scale
This leads to inefficient and error-prone ML lifecycle management.


## Solution
This project addresses the problem by:
- Tracking machine learning experiments using MLflow
- Logging parameters, metrics, and model artifacts
- Adding a custom automation layer to compare experiment runs
- Automatically selecting the best-performing model based on evaluation metrics

## Project Architecture
Dataset
|
v
Model Training
|
v
MLflow Experiment Tracking
|
v
Automated Run Comparison (Custom Logic)
|
v
Best Model Selection


---

## Key Features
- ML experiment tracking with MLflow
- Parameter, metric, and artifact logging
- Automated comparison of experiment runs
- Metric-based best model selection (e.g., RMSE, accuracy)
- Reproducible and auditable ML workflows

---

## Custom Contribution
In addition to using MLflow’s tracking capabilities, this project adds:

- Automated experiment comparison logic that queries MLflow runs
- Metric-based ranking of experiment runs
- Best model identification without manual inspection

This automation improves reliability and scalability of the ML lifecycle.

---

## Example Use Case
1. Train the same model using different hyperparameters
2. Log each experiment run to MLflow
3. Automatically compare runs based on evaluation metrics
4. Select the best-performing model for downstream use

---

## Tech Stack
- Python  
- MLflow  
- scikit-learn  
- Experiment Tracking  
- Model Lifecycle Management  

---

## How to Run
### 1. Install Dependencies
pip install mlflow scikit-learn
2. Run Model Training
Run any ML training script that logs experiments using MLflow.
3. Execute Automated Model Selection
python select_best_model.py
4. View Experiments in MLflow UI
mlflow ui

Key Learnings
Importance of experiment reproducibility
Managing ML workflows beyond model training
Automating decision-making in ML systems
Applying practical MLOps principles
Future Improvements
Register best models in MLflow Model Registry

Add stage-based model promotion (staging to production)
Integrate with pipeline orchestration or CI/CD tools
