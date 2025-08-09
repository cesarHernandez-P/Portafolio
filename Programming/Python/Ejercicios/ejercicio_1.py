""" 
#Todos Ejercicio: Calculadora de Promedios con Validación
Descripción:
Escribe un programa que pida al usuario ingresar varias notas (números entre 0 y 100). 
El usuario puede ingresar tantas notas como quiera, y cuando escriba "fin" el programa debe detenerse.
El programa debe:
Validar que cada nota sea un número válido entre 0 y 100.
Guardar todas las notas válidas en una lista.
Calcular el promedio de las notas ingresadas.
Mostrar el promedio con dos decimales.
Si no se ingresó ninguna nota válida, mostrar un mensaje indicando que no hay datos.
"""

def solicitar_notas():

    notas = []

    while True :
        
        nota = input("Ingresar una nota, para salir ingresa la palabra 'fin' : ")

        if nota.lower == "fin":
            break #* si el valor es ingresado es fin se detiene el programa

def main():
    

if __name__ == "__main__":
    main()