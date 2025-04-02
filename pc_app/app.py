import cv2
import requests
import tkinter as tk
from pyzbar.pyzbar import decode
from tkinter import messagebox, ttk

API_URL = "http://localhost:8000/sensor/"


def fetch_sensor_data(sensor_id):
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        filtered = [d for d in data if d['sensor_id'] == sensor_id]
        return filtered
    except Exception as e:
        return str(e)


def display_data(data):
    window = tk.Tk()
    window.title("FitBuddy - Sensor Data")
    window.geometry("800x400")

    tree = ttk.Treeview(window, columns=list(data[0].keys()), show='headings')
    for col in data[0].keys():
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for entry in data:
        tree.insert('', tk.END, values=list(entry.values()))

    tree.pack(expand=True, fill='both')
    window.mainloop()


def scan_qr_code():
    cap = cv2.VideoCapture(0)
    sensor_id = None
    while True:
        success, frame = cap.read()
        for barcode in decode(frame):
            text = barcode.data.decode('utf-8')
            if text.startswith("Fitbuddy:"):
                try:
                    sensor_id = int(text.split(":")[1])
                    cap.release()
                    cv2.destroyAllWindows()
                    return sensor_id
                except:
                    continue
        cv2.imshow('Scan QR Code (Fitbuddy:X)', frame)
        if cv2.waitKey(1) == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
    return None


if __name__ == '__main__':
    sid = scan_qr_code()
    if sid is not None:
        result = fetch_sensor_data(sid)
        if isinstance(result, list) and result:
            display_data(result)
        elif isinstance(result, list) and not result:
            messagebox.showinfo("Aucune donnée", f"Aucune donnée trouvée pour sensor_id={sid}.")
        else:
            messagebox.showerror("Erreur", result)
    else:
        messagebox.showwarning("QR non détecté", "Aucun QR code détecté.")
