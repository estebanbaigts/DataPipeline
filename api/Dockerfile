FROM python:3.10-slim

WORKDIR /app

COPY app.py ./
COPY index.html ./

RUN pip install --no-cache-dir fastapi uvicorn mlflow scikit-learn numpy

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
