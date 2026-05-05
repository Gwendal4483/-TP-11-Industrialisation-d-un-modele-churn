import pandas as pd

def load_data(path):
    # Lit le fichier CSV depuis le chemin fourni en paramètre
    # Retourne un DataFrame pandas avec toutes les colonnes brutes
    df = pd.read_csv(path)
    return df