# 🚗 Flask Garage API

## 📌 Contexte du projet

Ce projet consiste à développer une API REST avec **Flask** connectée à une base de données **PostgreSQL** en utilisant le module **psycopg2**.

L’objectif est de manipuler des données stockées en base via des requêtes SQL exécutées depuis une application Flask, tout en respectant les bonnes pratiques de sécurité (requêtes préparées).

---

## 🎯 Objectifs pédagogiques

- Connecter une application Flask à PostgreSQL  
- Exécuter des requêtes SQL depuis Python  
- Récupérer des données depuis une base  
- Ajouter, modifier et supprimer des données (CRUD)  
- Sécuriser les requêtes contre les injections SQL  
- Tester une API avec un outil comme Bruno  

---

## 🛠️ Technologies utilisées

- Python 3
- Flask
- PostgreSQL
- psycopg2-binary

---

## ⚙️ Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/Ludo-dev-1/flask_garage.git
cd flask_garage
```

### 2. Créer et activer un environnement virtuel

```bash
python -m venv .venv
```

Activation :

```bash
# Linux / Mac
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 3. Installer les dépendances

```bash
pip install psycopg2-binary flask
pip freeze > requirements.txt
```

## 🗄️ Base de données 

### 1. Création de la base 
```bash
CREATE DATABASE flask_garage;
```
### 2. Création de l’utilisateur 

```bash
CREATE USER garadm7841 WITH PASSWORD 'SP7c3$@uwL84jmSEoP3';
GRANT ALL PRIVILEGES ON DATABASE flask_garage TO garadm7841;
```

### 3. Création de la table 
```bash
CREATE TABLE car (
    car_id SERIAL PRIMARY KEY,
    brand VARCHAR(255) NOT NULL,
    model VARCHAR(255) NOT NULL
);
```

## ▶️ Lancement du serveur 
```bash 
flask --app app run --port 5050
```

