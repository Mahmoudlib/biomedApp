# BioMed Sénégal - Progressive Web App (PWA)

Une plateforme Progressive Web App (PWA) éducative et industrielle dédiée au secteur de la maintenance et de la distribution des équipements biomédicaux au Sénégal.

## 🚀 Fonctionnalités (Phase 1)
- **Tableau de Bord / Accueil** : Vue d'ensemble, recherche globale et raccourcis rapides.
- **Catalogue des Appareils** : Liste complète d'équipements médicaux filtrables par spécialités (Imagerie, Bloc, Laboratoire, Cardiologie, Réanimation) et recherche dynamique.
- **Fiches Techniques Détaillées** : Description clinique, principes de fonctionnement physiques, protocoles complets de maintenance préventive étape par étape, sources certifiées (OMS) et badges de vérification.
- **Annuaire des Entreprises** : Répertoire géolocalisé (Sénégal) des entreprises partenaires et fournisseurs d'équipements biomédicaux avec actions directes (envoi d'email, site officiel, LinkedIn).
- **Intégration PWA** : Fonctionnalités hors ligne via un Service Worker personnalisé et manifeste pour une installation sur mobile.

## 🛠️ Installation et Lancement Local

### Prérequis
- Python 3.10+
- Git

### Lancement
1. **Cloner le projet**
   ```bash
   git clone https://github.com/Mahmoudlib/biomedApp.git
   cd biomedApp
   ```

2. **Créer l'environnement virtuel et installer les dépendances**
   ```bash
   python -m venv .venv
   # Sur Windows:
   .\.venv\Scripts\activate
   # Installer Django:
   pip install -r requirements.txt
   ```

3. **Exécuter les migrations & Charger les données initiales**
   ```bash
   python manage.py migrate
   python manage.py seed_data
   ```

4. **Lancer le serveur de développement**
   ```bash
   python manage.py runserver
   ```
   Accédez à l'application via `http://127.0.0.1:8000/`.

## 🧪 Tests Unitaires
Pour exécuter les tests de conformité de l'application :
```bash
python manage.py test
```

## ⚖️ Licence
Distribué sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.
