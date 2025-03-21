# deploiement local et futur AWS

# Utilisation de l’image officielle de Python
FROM python:3.9

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances et les installer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le projet dans le conteneur
COPY . .

# Exposer le port sur lequel l'API tournera
EXPOSE 8000

# Lancer l'API FastAPI avec Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
