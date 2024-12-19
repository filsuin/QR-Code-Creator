document.getElementById("generate").addEventListener("click", function () {
    const url = document.getElementById("url").value;
    const color = document.getElementById("color").value;
    const size = document.getElementById("size").value * 10; // Taille multipliée pour un meilleur rendu

    // Vérifie si l'URL est vide
    if (!url) {
        alert("Veuillez entrer une URL.");
        return;
    }

    // Efface le QR Code précédent
    const qrContainer = document.getElementById("qrcode");
    qrContainer.innerHTML = "";

    // Génère le QR Code
    const qrcode = new QRCode(qrContainer, {
        text: url,
        width: size,
        height: size,
        colorDark: color,
        colorLight: "#ffffff",
        correctLevel: QRCode.CorrectLevel.H
    });

    // Attendre la génération du QR Code pour préparer le téléchargement
    setTimeout(() => {
        const canvas = qrContainer.querySelector("canvas");
        if (canvas) {
            const imageUrl = canvas.toDataURL("image/png"); // Convertir en image PNG
            const downloadLink = document.getElementById("downloadLink");
            downloadLink.href = imageUrl;
            downloadLink.style.display = "block";
        }
    }, 100);
});
