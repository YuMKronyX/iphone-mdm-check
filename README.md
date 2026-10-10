📱 iPhone MDM Check — V2

Outil graphique Python pour diagnostiquer les problèmes de connexion entre un iPhone et un ordinateur Linux.

✨ Fonctionnalités

* 🔌 Vérification des outils USB et Apple.
* 📱 Détection des appareils connectés.
* ℹ️ Lecture des informations du modèle et de la version iOS.
* 🔗 Vérification du jumelage avec l’iPhone.
* 🛠️ Conseils de dépannage automatiques.
* 📋 Génération et copie d’un rapport de diagnostic.

💻 Compatibilité

* Linux, notamment Zorin OS et Ubuntu.
* Python 3.
* Interface graphique Tkinter.
* Outils libimobiledevice et usbutils.

📦 Installation

Sur Zorin OS ou Ubuntu, ouvre un terminal et exécute :

```sudo apt update
sudo apt install python3 python3-tk usbutils libimobiledevice-utils
```

🚀 Lancement

Dans le dossier du projet :

```python3 iphone_mdm_check.py```

Déverrouille l’iPhone et connecte-le avec un câble USB compatible avec le transfert de données. Si l’appareil le demande, accepte l’autorisation « Faire confiance ».

🔒 À propos du MDM

Cet outil effectue uniquement des diagnostics locaux. Il ne supprime pas les profils MDM, ne contourne pas les restrictions de gestion et ne retire pas le verrouillage d’un appareil.

Pour libérer un appareil géré par une organisation, contacte son administrateur afin qu’il effectue la procédure officielle de retrait dans son système de gestion.

🧪 État du projet

Version : 2.0 — USB Diagnostics

Projet en développement. Les résultats dépendent de la version de Linux, des pilotes et de la configuration de l’iPhone.

📄 Licence

MIT — voir le fichier LICENSE.