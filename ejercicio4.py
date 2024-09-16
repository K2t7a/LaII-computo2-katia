from tkinter import *

def ventana_datos_mascotas():
    base = Tk()
    base.geometry("400x300")
    base.title("Datos de Mascotas")

    for i in range(3):
        Label(base, text=f"Mascota {i+1}").grid(row=i*3, column=0, padx=10, pady=10)
        Label(base, text="Nombre:").grid(row=i*3+1, column=0)
        Entry(base).grid(row=i*3+1, column=1)

        Label(base, text="Edad:").grid(row=i*3+2, column=0)
        Entry(base).grid(row=i*3+2, column=1)

    base.mainloop()

ventana_datos_mascotas()
