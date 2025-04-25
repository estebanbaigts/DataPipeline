import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Chargement des données
df = pd.read_csv("iris.csv")

# Nettoyage des colonnes
df.columns = [c.strip().replace('.', '_') for c in df.columns]

# valeur nulle
df = df.dropna()
print(f"✅ Lignes avec des valeurs nulles supprimées. Nombre de lignes restantes : {len(df)}")

# valeur abberantes
for col in df.select_dtypes(include=['float64', 'int64']).columns:
    mean = df[col].mean()
    std = df[col].std()
    lower_bound = mean - 3 * std
    upper_bound = mean + 3 * std
    df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
    print(f"✅ Valeurs aberrantes supprimées dans la colonne '{col}'. Nombre de lignes restantes : {len(df)}")

engine = create_engine('postgresql://user:password@postgres:5432/irisdb')
df.to_sql("iris_data", engine, if_exists="replace", index=False)

print("✅ Données nettoyées et chargées dans PostgreSQL.")
