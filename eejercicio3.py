from tkinter import *

def ventana_cedula_nombre():
    base = Tk()
    base.geometry("400x200")
    base.title("Datos Personales")

    Label(base, text="Número de Cédula:").grid(row=0, column=0, padx=10, pady=10)
    Label(base, text="Nombre Completo:").grid(row=1, column=0, padx=10, pady=10)

    Entry(base).grid(row=0, column=1, padx=10, pady=10)
    Entry(base).grid(row=1, column=1, padx=10, pady=10)

    base.mainloop()

ventana_cedula_nombre()
