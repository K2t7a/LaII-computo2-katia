from tkinter import *

def ventana_nombre_edad():
    base = Tk()
    base.geometry("300x200")
    base.title("Datos Personales")
    
    # Configurar el color de fondo de la ventana
    base.config(bg="lightblue")

    Label(base, text="Nombre: Katia Marilin Santos Avelar", font=("Arial", 14), bg="lightblue").place(relx=0.5, rely=0.45, anchor=CENTER)
    Label(base, text="Edad: 21 años", font=("Arial", 14), bg="lightblue").place(relx=0.5, rely=0.5, anchor=CENTER)

    base.mainloop()

ventana_nombre_edad()



