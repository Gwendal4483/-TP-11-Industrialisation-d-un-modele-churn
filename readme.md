# Projet Churn
 
## Objectif
Prédire le churn client à partir de données Telco.
 
## Dataset
Telco Customer Churn (Kaggle)
 
## Structure du projet
```
churn_project/
│
├── data/
│   └── churn.csv            # Dataset brut Telco Customer Churn
│
├── model/
│   └── churn_pipeline.pkl   # Modèle entraîné sauvegardé
│
├── src/
│   ├── data.py              # Chargement du fichier CSV
│   ├── preprocessing.py     # Nettoyage et encodage de la variable cible
│   ├── train.py             # Construction du pipeline et entraînement du modèle
│   └── evaluate.py          # Calcul de l'accuracy sur le jeu de test
│
├── app.py                   # API FastAPI exposant le modèle via HTTP
├── dashboard.py             # Dashboard Streamlit pour visualiser les données
├── main.py                  # Point d'entrée principal du projet
├── requirements.txt         # Dépendances Python
└── README.md
```
 
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
```json
{
  "tenure": 10,
  "MonthlyCharges": 70,
  "Contract": "Month-to-month",
  "InternetService": "Fiber optic"
}
```
 
Output:
```json
{
  "prediction": 1
}
```
 