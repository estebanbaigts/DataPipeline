FROM python:3.10-slim

WORKDIR /app

COPY preprocess.py .

RUN pip install --no-cache-dir pandas sqlalchemy psycopg2-binary

CMD ["python", "preprocess.py"]
