import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer


def train_model(df):
    # Définition des colonnes catégorielles et numériques utilisées pour la prédiction
    categorical_cols = ["Contract", "InternetService"]
    numerical_cols = ["tenure", "MonthlyCharges"]

    # Création du preprocesseur :
    # - OneHotEncoder pour encoder les colonnes catégorielles en colonnes binaires
    # - passthrough pour laisser les colonnes numériques telles quelles
    preprocessor = ColumnTransformer(transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
        ("num", "passthrough", numerical_cols)
    ])

    # Création du pipeline : enchaîne le preprocessing et le classifieur
    # Permet d'appliquer automatiquement le même preprocessing en production
    model = Pipeline(steps=[
        ("preprocessing", preprocessor),
        ("classifier", RandomForestClassifier(n_estimators=10, random_state=42))
    ])

    # Séparation des features (X) et de la variable cible (y)
    X = df[categorical_cols + numerical_cols]
    y = df["Churn"]

    # Découpage en jeu d'entraînement (80%) et jeu de test (20%)
    # random_state=42 garantit la reproductibilité du découpage
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entraînement du pipeline complet sur les données d'entraînement
    model.fit(X_train, y_train)

    # Création du dossier model/ s'il n'existe pas déjà
    os.makedirs("model", exist_ok=True)

    # Sauvegarde du modèle entraîné sur le disque au format pickle
    # Permet de le recharger plus tard sans réentraîner
    joblib.dump(model, "model/churn_pipeline.pkl")

    return model, X_test, y_test