from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import os
import mlflow.sklearn
import numpy as np

app = FastAPI()

model = mlflow.sklearn.load_model("/mlflow/artifacts/model")

@app.post("/predict")
def predict(sepal_width: float):
    prediction = model.predict(np.array([[sepal_width]]))[0]
    return {"predicted_sepal_length": prediction}


# Serve static HTML file on GET /predict
@app.get("/predict", response_class=HTMLResponse)
async def get_predict_page():
    return FileResponse("index.html")
