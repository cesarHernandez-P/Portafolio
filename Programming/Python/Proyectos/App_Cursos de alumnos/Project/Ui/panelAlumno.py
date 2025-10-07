from tkinter import Tk, messagebox, END
from tkinter import ttk
from Script import validacion

registroAlumnos = []

def iniciar_panelAlumno():

    root = Tk()
    root.title("Panel Alumno")
    root.geometry("450x600")
    root.resizable(False,False)

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    ttk.Label(root, text="Ingresar Alumno").grid(row=0, column=0,columnspan=2, pady=5, sticky="n") # Titulo


    # TODOS -- Configuracion para ingresar alumano

    frame_IngresarAlumno = ttk.Frame(root, padding=5) 
    frame_IngresarAlumno.grid(row=1, column=0, pady=8,sticky="nsew")


    #* Nombre alumno
    ttk.Label(frame_IngresarAlumno, text="Nombre del alumno : ").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    txt_nombreAlumno = ttk.Entry(frame_IngresarAlumno, width=30)
    txt_nombreAlumno.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

    #* Cantidad de cursos
    ttk.Label(frame_IngresarAlumno, text="Cantidad de curso : ").grid(row=3, column=0, padx=5, pady=5, sticky="e")
    txt_cantCurso = ttk.Entry(frame_IngresarAlumno, width=30)
    txt_cantCurso.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

    #! funcion para validar datos antes de guardar los datos.

    

    def validarAlumno(label_error,alumno,cursos):
        
        

        if validacion.validar_Alumno(alumno,cursos):
            registroAlumnos.append({"nombre":alumno.get(), "curso":cursos.get()})

            if tabla.exists(registroVacio):
                tabla.delete(registroVacio)

            tabla.insert("", "end", values=(alumno.get(),))

            txt_nombreAlumno.delete(0,END)
            txt_cantCurso.delete(0,END)

        else:
            label_error.config(text="Datos no validos", foreground="red")
            label_error.after(3000, lambda: label_error.config(text=""))

    #* Mensaje de Error

    label_mensaje=ttk.Label(frame_IngresarAlumno, text="", font=("Arial", 10))
    label_mensaje.grid(row=4, column=0, padx=5, pady=5, sticky="e")



    #* Boton Ingresar

    ttk.Button(frame_IngresarAlumno, text="Guardar", command=lambda: validarAlumno(label_mensaje,txt_nombreAlumno,txt_cantCurso)).grid(row=4, column=1, columnspan=2, pady=5 , padx=5, sticky="e")

    # Separador horizontal
    separador = ttk.Separator(root, orient='horizontal')
    separador.grid(row=2, column=0, sticky="ew", padx=10, pady=10)

    #?---------------------------------------------------------------------------------------

    # TODOS -- lista de alumnos

    frame_tabla = ttk.Frame(root)
    frame_tabla.grid(row=3, column=0, columnspan=1, padx=10, pady=10, sticky="nsew")


    frame_tabla.columnconfigure(0, weight=1)
    frame_tabla.columnconfigure(1, weight=1)


    columnas = ("alumno",)
    global tabla
    tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=5)
    tabla.heading("alumno", text="Alumno")
    tabla.column("alumno", width=300)


    # Scrollbar vertical
    scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=tabla.yview)
    tabla.configure(yscrollcommand=scrollbar.set)

    tabla.grid(row=0, column=0, sticky="nsew")
    scrollbar.grid(row=0, column=1, sticky="ns")

    global registroVacio
    registroVacio = tabla.insert("", "end", values=("   ", "   "))

    

        # Separador horizontal
    separador = ttk.Separator(root, orient='horizontal')
    separador.grid(row=4, column=0, sticky="ew", padx=10, pady=10)

    #?---------------------------------------------------------------------------------------

    # TODOS -- Buscar curso alumnos  


    ttk.Label(root, text="Buscar cursos").grid(row=5, column=0,columnspan=2, pady=5, sticky="n") 

    frame_buscarCurso = ttk.Frame(root,padding=5)
    frame_buscarCurso.grid(row=6, column=0, columnspan=1, padx=10, pady=10, sticky="nsew")

    frame_buscarCurso.columnconfigure(0, weight=1)
    frame_buscarCurso.columnconfigure(1, weight=1)
    frame_buscarCurso.rowconfigure(2, weight=1)

    ttk.Label(frame_buscarCurso, text="Nombre del alumno : ").grid(row=0, column=0,padx=5, pady=5, sticky="e") 
    txt_buscarAlumno = ttk.Entry(frame_buscarCurso, width=30)
    txt_buscarAlumno.grid(row=0, column=1, padx=5, pady=5, sticky="ew") 





    #! Funcion para buscar alumno 

    def buscarAlumno(buscarAlumno):

        for item in tabla_alumno.get_children():
            tabla_alumno.delete(item)
 
        alumnoExiste = False
        for alumno in registroAlumnos:
            if alumno["nombre"].lower() == buscarAlumno.lower():
                #messagebox.showerror("ok", "registro encontrado")
                
                txt_buscarAlumno.delete(0,END)
                tabla_alumno.insert("", "end", values=(alumno["nombre"], alumno["curso"]))

                alumnoExiste=True
                break
        if not alumnoExiste:
                messagebox.showerror("Error", "registro no existe")
                
    #* Boton buscar

    ttk.Button(frame_buscarCurso, text="Buscar", command=lambda: buscarAlumno(txt_buscarAlumno.get()) ).grid(row=1, column=1, columnspan=2, pady=5 , padx=5, sticky="e")

    #* tabla para mostrar los datos encontrados

    columnasBuscaralumno = ("alumno","cursos")
    global tabla_alumno
    tabla_alumno = ttk.Treeview(frame_buscarCurso, columns=columnasBuscaralumno, show="headings", height=1)
    tabla_alumno.heading("alumno", text="Alumno")
    tabla_alumno.heading("cursos", text="Cursos")
    tabla_alumno.column("alumno", width=100)
    tabla_alumno.column("cursos", width=100)


    tabla_alumno.grid(row=2, column=0, columnspan=2,sticky="nsew")



    #?---------------------------------------------------------------------------------------


    #* Mensaje de Bienvenida despues de 300 ms milesegundos
        
    root.after(300, lambda: messagebox.showinfo("Bienvenida", "Bienvenido al panel de Alumnos !!!"))




    root.mainloop()