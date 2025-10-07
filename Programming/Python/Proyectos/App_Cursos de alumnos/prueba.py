import tkinter as tk
from tkinter import ttk

# Lista donde se guardan los alumnos
datos_alumnos = []

def guardar_alumno():
    nombre = entry_nombre.get()
    curso = entry_curso.get()

    if nombre and curso:
        # Guardar alumno en lista
        datos_alumnos.append({"nombre": nombre, "curso": curso})

        # Insertar en la tabla
        tabla.insert("", "end", values=(nombre, curso))

        # Limpiar entradas
        entry_nombre.delete(0, tk.END)
        entry_curso.delete(0, tk.END)

def iniciar_app():
    global entry_nombre, entry_curso, tabla

    root = tk.Tk()
    root.title("Lista de Alumnos")
    root.geometry("400x300")

    # Entradas
    tk.Label(root, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
    entry_nombre = tk.Entry(root)
    entry_nombre.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(root, text="Curso:").grid(row=1, column=0, padx=5, pady=5)
    entry_curso = tk.Entry(root)
    entry_curso.grid(row=1, column=1, padx=5, pady=5)

    # Botón para guardar
    tk.Button(root, text="Agregar Alumno", command=guardar_alumno).grid(row=2, column=0, columnspan=2, pady=10)

    # Tabla Treeview con Scrollbar
    frame_tabla = ttk.Frame(root)
    frame_tabla.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    columnas = ("nombre", "curso")
    tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=5)
    tabla.heading("nombre", text="Nombre")
    tabla.heading("curso", text="Curso")
    tabla.column("nombre", width=150)
    tabla.column("curso", width=100)

    # Scrollbar vertical
    scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=tabla.yview)
    tabla.configure(yscrollcommand=scrollbar.set)

    tabla.grid(row=0, column=0)
    scrollbar.grid(row=0, column=1, sticky="ns")

    root.mainloop()

iniciar_app()