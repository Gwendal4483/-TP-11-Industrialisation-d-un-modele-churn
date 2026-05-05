from sklearn.metrics import accuracy_score

def evaluate(model, X_test, y_test):
    # Génère les prédictions du modèle sur le jeu de test
    preds = model.predict(X_test)

    # Calcule le pourcentage de prédictions correctes
    acc = accuracy_score(y_test, preds)

    print("Accuracy:", acc)