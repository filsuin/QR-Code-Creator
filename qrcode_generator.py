import qrcode

# Étape 1 : Demander les informations à l'utilisateur
lien = input("Entrez le lien que vous souhaitez convertir en QR code : ")
couleur_pixels = input("Entrez la couleur des pixels (par ex. black, red, blue) : ").lower()
couleur_fond = input("Entrez la couleur de fond (par ex. white, yellow, green) : ").lower()

# Étape 2 : Générer le QR code
qr = qrcode.QRCode(
    version=1,  # Taille du QR code (1 = plus petit, 40 = plus grand)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Niveau de correction d'erreur
    box_size=10,  # Taille de chaque boîte
    border=4,  # Largeur de la bordure (en boîtes)
)
qr.add_data(lien)
qr.make(fit=True)

# Étape 3 : Créer une image du QR code avec les couleurs choisies
image = qr.make_image(fill_color=couleur_pixels, back_color=couleur_fond)

# Étape 4 : Enregistrer le QR code
nom_fichier = "qr_code_personnalise.png"
image.save(nom_fichier)
print(f"QR code enregistré sous le nom : {nom_fichier}")
