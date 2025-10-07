


def validar_usuario (usuario,contrasena):
    
    if usuario == "cesar" and contrasena == "1234":
        return True
    else:
        return False
    
def validar_Alumno (nombre,curso):
    cant_curso = curso.get()
    nombre = nombre.get()
    if cant_curso.isdigit() and nombre != "":
        return True
    else:
        return False