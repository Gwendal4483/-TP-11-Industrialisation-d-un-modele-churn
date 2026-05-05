# Point d'entrée principal du projet
# Orchestre le chargement des données, le preprocessing, l'entraînement et l'évaluation

import src.data as data
import src.evaluate as evaluate
import src.preprocessing as preprocessing
import src.train as train

if __name__ == "__main__":
    # Chargement du fichier CSV depuis le dossier data/
    df = data.load_data("data/churn.csv")
    print(df.head())

    # Nettoyage et préparation des données brutes
    df = preprocessing.preprocess(df)

    # Entraînement du modèle et récupération des données de test
    model, X_test, y_test = train.train_model(df)

    # Évaluation des performances du modèle sur les données de test
    evaluate.evaluate(model, X_test, y_test)