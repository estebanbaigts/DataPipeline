import pandas as pd
from sqlalchemy import create_engine
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import mlflow
import mlflow.sklearn
import os
import shutil



shared_path = "/mlflow/artifacts/model"
# Supprimer l’ancien modèle s’il existe
if os.path.exists(shared_path):
    shutil.rmtree(shared_path)
os.makedirs(shared_path, exist_ok=True)


# Charger données
engine = create_engine('postgresql://user:password@postgres:5432/irisdb')
df = pd.read_sql("SELECT * FROM iris_data", engine)

X = df[['sepal_width']]
y = df['sepal_length']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

with mlflow.start_run():
    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)

    mlflow.log_metric("mse", mse)
    mlflow.sklearn.log_model(model, "model")


mlflow.sklearn.save_model(model, shared_path)
print("✅ Modèle sauvegardé localement à :", shared_path)
