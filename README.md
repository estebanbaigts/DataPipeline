## Data Pipeline – Prédiction de la longueur des sépales Iris

Projet de spécialisation – Promo 2025  
Estimons la **longueur des sépales** à partir de leur **largeur** via un pipeline de machine learning complet.

---

## Contenu du projet

Ce dépôt contient un pipeline de traitement de données dockerisé avec les composants suivants :

- **Preprocessing** : chargement et enregistrement dans PostgreSQL
- **Modélisation** : entraînement d’un modèle et log dans MLflow
- **API REST** : prédictions en temps réel via FastAPI
- **MLflow UI** : visualisation des expériences
- **Base de données PostgreSQL**

---

## Prérequis

- **Windows 11**
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installé et fonctionnel
- WSL2 activé (Docker vous proposera de le configurer automatiquement)

---

## Lancer le projet

docker-compose up --build
avec curl : curl -X POST "http://localhost:8000/predict?sepal_width=3.5" en remplaçant 3.5 par la mesure désirer
dans un navigateur : localhost:8000/predict
pour MLflow : localhost:5000/