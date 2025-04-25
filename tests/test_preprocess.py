import sys
import os
import pandas as pd

# Ajouter le répertoire parent au PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../preprocessing")))

from preprocess import df

def test_preprocess_cleaning():
    # Vérification des colonnes
    assert all(c.islower() and '_' in c for c in df.columns), "Les colonnes doivent être en minuscules et contenir des underscores."

    # Vérification des valeurs nulles
    assert df.isnull().sum().sum() == 0, "Il ne doit pas y avoir de valeurs nulles dans les données."

    # Vérification des valeurs aberrantes
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        mean = df[col].mean()
        std = df[col].std()
        lower_bound = mean - 3 * std
        upper_bound = mean + 3 * std
        assert df[(df[col] < lower_bound) | (df[col] > upper_bound)].empty, f"Il ne doit pas y avoir de valeurs aberrantes dans la colonne '{col}'."