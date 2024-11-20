import qrcode
import tkinter as tk
from tkinter import colorchooser
from tkinter import messagebox

# Fonction pour générer le QR code avec les paramètres de l'utilisateur
def generate_qr_code():
    # Récupérer les valeurs des champs
    lien = entry_lien.get()
    couleur_pixels = entry_couleur_pixels.get()
    couleur_fond = entry_couleur_fond.get()

    # Vérifier si le lien est valide
    if not lien:
        messagebox.showerror("Erreur", "Veuillez entrer un lien valide.")
        return

    # Générer le QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(lien)
    qr.make(fit=True)

    # Créer l'image avec les couleurs
    try:
        image = qr.make_image(fill_color=couleur_pixels, back_color=couleur_fond)
    except ValueError:
        messagebox.showerror("Erreur", "Couleur invalide. Veuillez entrer des couleurs valides.")
        return

    # Enregistrer le QR code
    nom_fichier = "qr_code_personnalise.png"
    image.save(nom_fichier)

    messagebox.showinfo("Succès", f"QR code enregistré sous le nom : {nom_fichier}")

# Fonction pour ouvrir un sélecteur de couleur pour la couleur des pixels
def choisir_couleur_pixels():
    couleur = colorchooser.askcolor(title="Choisir la couleur des pixels")[1]
    if couleur:
        entry_couleur_pixels.delete(0, tk.END)
        entry_couleur_pixels.insert(0, couleur)

# Fonction pour ouvrir un sélecteur de couleur pour la couleur de fond
def choisir_couleur_fond():
    couleur = colorchooser.askcolor(title="Choisir la couleur de fond")[1]
    if couleur:
        entry_couleur_fond.delete(0, tk.END)
        entry_couleur_fond.insert(0, couleur)

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Générateur de QR Code")

# Créer les widgets
label_lien = tk.Label(fenetre, text="Entrez le lien que vous souhaitez convertir :")
label_lien.pack(pady=5)

entry_lien = tk.Entry(fenetre, width=50)
entry_lien.pack(pady=5)

label_couleur_pixels = tk.Label(fenetre, text="Entrez la couleur des pixels (ex. black, red, blue) :")
label_couleur_pixels.pack(pady=5)

entry_couleur_pixels = tk.Entry(fenetre, width=50)
entry_couleur_pixels.pack(pady=5)

# Bouton pour choisir la couleur des pixels via un sélecteur
button_couleur_pixels = tk.Button(fenetre, text="Choisir la couleur des pixels", command=choisir_couleur_pixels)
button_couleur_pixels.pack(pady=5)

label_couleur_fond = tk.Label(fenetre, text="Entrez la couleur de fond (ex. white, yellow, green) :")
label_couleur_fond.pack(pady=5)

entry_couleur_fond = tk.Entry(fenetre, width=50)
entry_couleur_fond.pack(pady=5)

# Bouton pour choisir la couleur de fond via un sélecteur
button_couleur_fond = tk.Button(fenetre, text="Choisir la couleur de fond", command=choisir_couleur_fond)
button_couleur_fond.pack(pady=5)

# Bouton pour générer le QR code
button_generer_qr = tk.Button(fenetre, text="Générer le QR Code", command=generate_qr_code)
button_generer_qr.pack(pady=20)

# Lancer la boucle principale de Tkinter
fenetre.mainloop()
