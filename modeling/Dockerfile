FROM python:3.10-slim

WORKDIR /app

COPY train_model.py .

RUN pip install --no-cache-dir pandas scikit-learn sqlalchemy psycopg2-binary mlflow

CMD ["python", "train_model.py"]
