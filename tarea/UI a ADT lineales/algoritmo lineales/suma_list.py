import tkinter as tk
from tkinter import messagebox

def ejecutar_algoritmo():
    entrada = entry.get()
    try:
        lista = [int(x.strip()) for x in entrada.split(',')]
        suma = 0
        pasos = ""
        for i, num in enumerate(lista):
            suma += num
            pasos += f"Paso {i+1}: suma parcial = {suma}\n"
        resultado_label.config(text=f"Suma total: {suma}")
        pasos_text.delete(1.0, tk.END)
        pasos_text.insert(tk.END, pasos)
    except ValueError:
        messagebox.showerror("Error", "Ingrese números enteros separados por comas.")

root = tk.Tk()
root.title("Algoritmo Lineal: Suma de Lista")

tk.Label(root, text="Ingrese números separados por comas:").pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

boton = tk.Button(root, text="Ejecutar", command=ejecutar_algoritmo)
boton.pack(pady=5)

resultado_label = tk.Label(root, text="Suma total: ")
resultado_label.pack(pady=5)

pasos_text = tk.Text(root, height=10, width=40)
pasos_text.pack(pady=5)

root.mainloop()