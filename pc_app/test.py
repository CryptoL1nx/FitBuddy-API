import cv2
from pyzbar.pyzbar import decode

img = cv2.imread("1.jpg")

if img is None:
    print("❌ Erreur : image non trouvée.")
else:
    decoded = decode(img)
    if decoded:
        for qr in decoded:
            print("✅ QR code détecté :", qr.data.decode())
    else:
        print("❌ Aucun QR code détecté.")
