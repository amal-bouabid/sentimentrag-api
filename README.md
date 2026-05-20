# SentimentRAG API

**Analyse de sentiment enrichie par RAG** — Une API moderne combinant **Sentiment Analysis** et **Retrieval-Augmented Generation**.

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

## 🎯 Description

**SentimentRAG** est une API REST qui permet d'analyser le sentiment d'un texte (positif, négatif, neutre) tout en enrichissant l'analyse grâce à un système **RAG** (Retrieval-Augmented Generation).

Elle combine :
- Un modèle de **sentiment analysis** puissant (basé sur RoBERTa)
- Un système de récupération contextuelle via **embeddings** et **ChromaDB**
- Stockage persistant des analyses (SQLite)

Idéal pour l'analyse de reviews clients, monitoring de réseaux sociaux, support intelligent, etc.

## ✨ Fonctionnalités

- **Analyse de sentiment** en temps réel avec score de confiance
- **RAG Pipeline** : enrichissement automatique avec contextes pertinents
- **API REST** moderne avec FastAPI (documentation Swagger intégrée)
- **Architecture Singleton** optimisée pour le chargement des modèles
- **Base vectorielle persistante** avec ChromaDB
- **Containerisation Docker** prête pour la production
- **Tests unitaires et d'intégration**
- Health check et logging

## 🛠️ Technologies utilisées

- **Python 3.10**
- **FastAPI** + Uvicorn
- **Hugging Face Transformers** & **Sentence-Transformers**
- **ChromaDB** (Vector Store)
- **SQLite** (historique des analyses)
- **Docker**
- **Pydantic v2**
- **pytest**

**Modèles :**
- Sentiment : `cardiffnlp/twitter-roberta-base-sentiment-latest`
- Embeddings : `all-MiniLM-L6-v2`

---

## 🚀 Installation et Lancement

### 1. Avec Docker (Recommandé)

```bash
# Cloner le repository
git clone https://github.com/votreusername/sentimentrag-api.git
cd sentimentrag-api

# Lancer avec Docker
docker-compose up --build
# ou
docker build -t sentimentrag-api .
docker run -p 8000:8000 sentimentrag-api
