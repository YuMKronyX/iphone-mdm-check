# iphone-mdm-check 
📱 iPhone MDM Check

Diagnostic iPhone depuis Linux — interface en français

iPhone MDM Check est un outil open source conçu pour diagnostiquer la connexion USB d’un iPhone depuis Linux et aider à comprendre les problèmes rencontrés pendant la configuration.

✨ Fonctionnalités

* 🔌 Détection des appareils iOS connectés en USB
* 🔍 Vérification des outils de diagnostic installés
* 📱 Lecture des informations de base lorsqu’elles sont accessibles
* 🛠️ Conseils de dépannage
* 📋 Guide pour demander la libération officielle d’un appareil géré

💻 Installation sur Zorin OS / Ubuntu 

```sudo apt update
sudo apt install python3-tk libimobiledevice-utils ifuse
```

🚀 Lancement

```python3 iphone_mdm_check.py```

⚠️ À propos du MDM

Cet outil ne supprime pas et ne contourne pas la gestion à distance.

Si l’écran « Gestion à distance » apparaît pendant la configuration, contacte l’organisation affichée et demande-lui de retirer l’appareil de sa gestion et, si nécessaire, de le libérer d’Apple Business Manager.

🔒 Confidentialité

Les diagnostics sont effectués localement. Le programme n’est pas conçu pour envoyer les informations de l’appareil à un serveur.

Ne publie jamais ton numéro de série ou d’autres identifiants privés.

📄 Licence

Projet distribué sous licence MIT. Voir le fichier LICENSE.
