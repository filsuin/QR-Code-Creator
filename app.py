from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        color = request.form["color"].lstrip("#")
        size = int(request.form["size"])  # Récupérer la taille depuis le formulaire

        # Limiter la taille pour éviter les erreurs
        size = max(1, min(size, 40))  

        # Génération du QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=size,  # Appliquer la taille ici
            border=4
        )
        qr.add_data(url)
        qr.make(fit=True)

        rgb_color = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
        img = qr.make_image(fill_color=rgb_color, back_color="white")

        img_io = BytesIO()
        img.save(img_io, "PNG")
        img_io.seek(0)

        return send_file(img_io, mimetype="image/png", as_attachment=True, download_name="qr_code.png")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
