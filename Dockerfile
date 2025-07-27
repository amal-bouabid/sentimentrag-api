FROM python:3.10-slim

# Crée un dossier pour l'app
WORKDIR /app

# Copie uniquement les fichiers nécessaires
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code
COPY app/ app/
COPY app/api/main.py .

# Exposer le port
EXPOSE 8000

# Commande de lancement
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
