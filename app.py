import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# Initialisation de l'application FastAPI
app = FastAPI()

# Chargement du modèle sauvegardé depuis le disque au démarrage de l'API
# Le modèle est chargé une seule fois en mémoire pour toutes les requêtes
model = joblib.load("model/churn_pipeline.pkl")

# Définition du schéma de données attendu pour une requête de prédiction
# Pydantic valide automatiquement les types à la réception de la requête
class Client(BaseModel):
    tenure: int
    MonthlyCharges: float
    Contract: str
    InternetService: str

@app.get("/")
def home():
    # Endpoint de vérification : permet de tester que l'API est bien en ligne
    return {"message": "API OK"}

@app.post("/predict")
def predict(client: Client):
    # Conversion des données reçues en DataFrame pour être compatible avec le pipeline
    df = pd.DataFrame([{
        "tenure": client.tenure,
        "MonthlyCharges": client.MonthlyCharges,
        "Contract": client.Contract,
        "InternetService": client.InternetService
    }])

    # Prédiction via le pipeline (preprocessing + modèle)
    pred = model.predict(df)

    # Retourne la prédiction : 1 = client à risque, 0 = client stable
    return {"prediction": int(pred[0])}