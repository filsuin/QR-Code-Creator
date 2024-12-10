# Générateur de QR Code Personnalisé

Ce projet est un générateur de QR codes basé sur une interface web. Il permet aux utilisateurs de créer des QR codes à partir d'un lien et de personnaliser leur couleur. L'application fonctionne localement avec Flask.

## Fonctionnalités

- Génération de QR codes à partir d'un lien fourni.
- Personnalisation de la couleur des pixels via un sélecteur de couleur.
- Interface web moderne avec des boutons arrondis et un design épuré.
- Téléchargement direct du QR code au format PNG.

## Prérequis

Avant de lancer le projet, assurez-vous d'avoir Python installé ainsi que les bibliothèques suivantes :

- Flask
- qrcode[pil]

Installez-les avec la commande suivante :

```bash
pip install Flask qrcode[pil]
```

## Installation

1. Clonez ce repository sur votre machine locale :
   ```bash
   git clone https://github.com/yourusername/qr-code-generator.git
   cd qr-code-generator
   ```

2. Assurez-vous que toutes les dépendances sont installées (voir la section Prérequis).

## Utilisation

1. Lancez le serveur Flask :
   ```bash
   python app.py
   ```

2. Ouvrez un navigateur et accédez à `http://127.0.0.1:5000/`.

3. Étapes pour générer un QR code :
   - Entrez l'URL dans le champ prévu à cet effet.
   - Choisissez une couleur pour le QR code à l'aide du sélecteur.
   - Cliquez sur "Générer QR Code".
   - Téléchargez l'image générée au format PNG.

## Structure du projet

- `app.py` : Script principal contenant l'application Flask.
- `templates/index.html` : Fichier HTML pour l'interface utilisateur.
- `static/` : Dossier pour les fichiers CSS et JS (si ajoutés ultérieurement).

## Améliorations futures

- Support de la personnalisation de la taille des QR codes.
- Ajout d'options pour inclure des logos au centre des QR codes.
- Hébergement de l'application sur une plateforme web (ex. Heroku).

---

Contribuez ou signalez des problèmes via des pull requests ou des issues sur GitHub.
```
