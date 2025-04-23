from fastapi import FastAPI
import mlflow.sklearn
import numpy as np

app = FastAPI()

model = mlflow.sklearn.load_model("/mlflow/artifacts/model")

@app.get("/predict")
def predict(sepal_width: float):
    prediction = model.predict(np.array([[sepal_width]]))[0]
    return {"predicted_sepal_length": prediction}
