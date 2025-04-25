# Data Pipeline – Prédiction de la longueur des sépales Iris

**Projet de spécialisation – Promo 2025**  
Ce projet vise à estimer la **longueur des sépales** d'Iris à partir de leur **largeur** en utilisant un pipeline complet de machine learning.

---

## 📂 Contenu du projet

Ce dépôt contient un pipeline de traitement de données dockerisé avec les composants suivants :

1. **Preprocessing** :  
   - Chargement des données et enregistrement dans une base PostgreSQL.

2. **Modélisation** :  
   - Entraînement d’un modèle de machine learning et suivi des expériences via MLflow.

3. **API REST** :  
   - Prédictions en temps réel grâce à FastAPI.

4. **MLflow UI** :  
   - Interface pour visualiser les expériences et les métriques.

5. **Base de données PostgreSQL** :  
   - Stockage des données pour le pipeline.

---

## 🛠️ Prérequis

Avant de commencer, assurez-vous d’avoir les éléments suivants installés sur votre machine :

- **Système d’exploitation** :  
  - Windows 11 (ou un environnement compatible Docker)
  
- **Logiciels nécessaires** :  
  - [Docker Desktop](https://www.docker.com/products/docker-desktop/) installé et fonctionnel  
  - WSL2 activé (Docker vous proposera de le configurer automatiquement si nécessaire)

---

## 🚀 Lancer le projet

Pour démarrer le pipeline, exécutez la commande suivante dans le terminal :

```bash
docker-compose up --build
