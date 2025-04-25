import pytest
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../modeling")))

from train_model import train_test_split

def test_train_model():
    # Données factices pour le test
    data = {
        "sepal_width": [3.0, 3.2, 3.1, 2.9, 3.3],
        "sepal_length": [4.7, 4.9, 4.8, 4.6, 5.0]
    }
    df = pd.DataFrame(data)
    X = df[['sepal_width']]
    y = df['sepal_length']

    # Split des données
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Entraînement du modèle
    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    # Prédictions
    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)

    # Vérifications
    assert len(preds) == len(y_test), "Le nombre de prédictions doit correspondre au nombre de données de test."
    assert mse >= 0, "La métrique MSE doit être positive."