import qrcode

# Étape 1 : Demander le lien à l'utilisateur
lien = input("Entrez le lien que vous souhaitez convertir en QR code : ")

# Étape 2 : Générer le QR code
qr = qrcode.QRCode(
    version=1,  # Taille du QR code (1 = plus petit, 40 = plus grand)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Niveau de correction d'erreur
    box_size=10,  # Taille de chaque boîte
    border=4,  # Largeur de la bordure (en boîtes)
)
qr.add_data(lien)
qr.make(fit=True)

# Étape 3 : Créer une image du QR code
image = qr.make_image(fill_color="black", back_color="white")

# Étape 4 : Enregistrer le QR code
nom_fichier = "qr_code.png"
image.save(nom_fichier)
print(f"QR code enregistré sous le nom : {nom_fichier}")
