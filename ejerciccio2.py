from tkinter import *

def ventana_clave_secreta():
    base = Tk()
    base.geometry("300x150")
    base.title("Clave Secreta")

    Label(base, text="Ingrese su clave:").pack(pady=10)
    clave_entry = Entry(base, show="*")
    clave_entry.pack(pady=10)

    base.mainloop()

ventana_clave_secreta()
