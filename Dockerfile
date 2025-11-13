# Utilise une image Python officielle
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .
COPY app.py .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Lancer le script
CMD ["python", "app.py"]
