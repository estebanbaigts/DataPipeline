import pandas as pd
import psycopg2
from sqlalchemy import create_engine

df = pd.read_csv("iris.csv")

# Nettoyage si nécessaire (ici simple)
df.columns = [c.strip().replace('.', '_') for c in df.columns]

# Connexion à PostgreSQL
engine = create_engine('postgresql://user:password@postgres:5432/irisdb')
df.to_sql("iris_data", engine, if_exists="replace", index=False)

print("✅ Données chargées dans PostgreSQL.")
