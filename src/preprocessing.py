import pandas as pd

def preprocess(df):
    # Supprime les lignes contenant des valeurs manquantes
    df = df.dropna()

    # Convertit la colonne cible Churn de Yes/No en 1/0
    # Nécessaire pour que le modèle puisse interpréter la variable cible
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

    return df