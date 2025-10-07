
from tkinter import Tk, messagebox, END
from tkinter import ttk
from Script  import validacion
from panelAlumno import  iniciar_panelAlumno


def iniciar_login():

    root = Tk()
    root.title("Inicio de sesión")
    root.geometry("400x200")
    root.resizable(False,False)

    # Configurar el layout general

    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    # Crear frame centrado

    frame = ttk.Frame(root, padding=20)
    frame.grid(row=0, column=0, pady=30,sticky="nsew")

    # Centrar el contenido dentro del frame

    frame.columnconfigure(1,weight=1)

    # Usuario
    ttk.Label(frame, text="Usuario:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    txt_usuario = ttk.Entry(frame, width=10)
    txt_usuario.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    # Contraseña
    ttk.Label(frame, text="Contraseña:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    txt_contrasena = ttk.Entry(frame, show="*",width=10)
    txt_contrasena.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    #! funcion para validar usuario y contraseña

    def intentar_login():
        usuario = txt_usuario.get()
        contrasena = txt_contrasena.get()

        if  validacion.validar_usuario(usuario, contrasena):

            root.destroy() #? eliminar ventana iniciar login
            iniciar_panelAlumno()
        

        else:
            messagebox.showerror("Error", "Credenciales inválidas")
            txt_usuario.delete(0,END)
            txt_contrasena.delete(0,END)

    
    # Botón centrado en 2 columnas
    ttk.Button(frame, text="Ingresar", command= intentar_login).grid(row=2, column=0, columnspan=2, pady=10)



    root.mainloop()