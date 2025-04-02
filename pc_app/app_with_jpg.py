# -*- coding: utf-8 -*-
from PIL import Image
from pyzbar.pyzbar import decode
import requests
import tkinter as tk
from tkinter import messagebox, ttk

API_URL = "http://localhost:8000/sensor/"
IMAGE_PATH = "1.jpg"  

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

def scan_qr_from_image(image_path):
    image = Image.open(image_path)
    decoded_objects = decode(image)
    for obj in decoded_objects:
        text = obj.data.decode('utf-8')
        if text.startswith("Fitbuddy:"):
            try:
                return int(text.split(":")[1])
            except:
                continue
    return None

if __name__ == '__main__':
    sid = scan_qr_from_image(IMAGE_PATH)
    if sid is not None:
        result = fetch_sensor_data(sid)
        if isinstance(result, list) and result:
            display_data(result)
        elif isinstance(result, list) and not result:
            messagebox.showinfo("Aucune donn e", f"Aucune donnée trouvée pour sensor_id={sid}.")
        else:
            messagebox.showerror("Erreur", result)
    else:
        messagebox.showwarning("QR non d tect ", "Aucun QR code détecté  dans l'image.")
