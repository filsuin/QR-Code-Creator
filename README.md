# Générateur de QR Code Personnalisé

Ce projet permet de générer des QR codes personnalisés à partir d'un lien fourni par l'utilisateur. L'utilisateur peut choisir la couleur des pixels, la couleur de fond et même utiliser un sélecteur de couleur pour plus de flexibilité. Le QR code généré peut être enregistré dans un fichier image au format PNG.

## Fonctionnalités

- Générer un QR code à partir d'un lien.
- Personnaliser la couleur des pixels et de l'arrière-plan.
- Utiliser un sélecteur de couleur pour choisir les couleurs facilement.
- Interface graphique conviviale avec Tkinter.

## Prérequis

Avant de pouvoir exécuter ce projet, vous devez avoir installé les bibliothèques suivantes :

- `qrcode` pour la génération du QR code.
- `Pillow` (PIL) pour la gestion des images.
- `tkinter` pour l'interface graphique.

Vous pouvez installer ces dépendances avec la commande suivante :

```bash
pip install qrcode[pil] Pillow
```
## Installation

1. Clonez ou téléchargez ce repository sur votre machine locale :
```bash
git clone https://github.com/yourusername/qr-code-generator.git
cd qr-code-generator
```
2. Assurez-vous d'avoir installé toutes les dépendances requises, comme mentionné ci-dessus.

## Utilisation

1. Ouvrez le terminal ou l'invite de commande et exécutez le script Python :
```bash
python qr_code_generator.py
```
2. Une interface graphique s'ouvrira. Voici les étapes :

- Entrez un lien dans le champ prévu à cet effet.
- Sélectionnez la couleur des pixels (par exemple, noir, rouge, etc.).
- Sélectionnez la couleur de fond (par exemple, blanc, jaune, etc.).
- Cliquez sur le bouton Générer le QR Code pour créer le QR code personnalisé.

3. Le QR code généré sera enregistré sous le nom `qr_code_personnalise.png` dans le répertoire courant.
