# Projet Churn

## Objectif
Prédire le churn client à partir de données Telco.

## Dataset
Telco Customer Churn (Kaggle)

## Installation
pip install -r requirements.txt

## Lancer le modèle
python main.py

## Lancer l'API
uvicorn app:app --reload

## Lancer le dashboard
streamlit run dashboard.py

## API

### GET /
Vérifie que l'API est en ligne.

### POST /predict
Prédit si un client va churner.

Input:
{
  "tenure": 10,
  "MonthlyCharges": 70,
  "Contract": "Month-to-month",
  "InternetService": "Fiber optic"
}

Output:
{
  "prediction": 1
}


