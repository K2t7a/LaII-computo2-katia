from tkinter import *

def ventana_datos_persona():
    base = Tk()
    base.geometry("500x400")
    base.title("Datos Característicos de una Persona")

    etiquetas = ["Nombre", "Apellido", "Edad", "Género", "Dirección", "Teléfono", "Correo", "Estado Civil", "Ocupación", "Nacionalidad"]
    
    for i, etiqueta in enumerate(etiquetas):
        Label(base, text=f"{etiqueta}:").grid(row=i, column=0, padx=10, pady=5)
        Entry(base).grid(row=i, column=1, padx=10, pady=5)

    base.mainloop()

ventana_datos_persona()
