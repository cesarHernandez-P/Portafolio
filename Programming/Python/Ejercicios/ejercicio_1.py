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
        
        ingreso_nota = input("Ingresar una nota, para salir ingresa la palabra 'fin' : ")

        if ingreso_nota.lower() == 'fin':

            break #* si el valor es ingresado es fin se detiene el programa
        try:
            nota = float(ingreso_nota)

            if 0 <= nota <= 100 :

                notas.append(nota)

            else:

                print ("Error : ingrese un numero valido") 

        except ValueError:

            print ("Error : ingrese un numero valido")
    return notas

def promedioNotas(notas):

    if len(notas) == 0 or notas is None:

        return None
    else:

        return sum(notas)/ len(notas)

def main():

    notas = solicitar_notas()

    promedio = promedioNotas(notas)

    if promedio is None:

        print ("No hay notas validas")

    else :

        print(f"El promedio de notas es : {promedio:.2f}")



if __name__ == "__main__":
    main()
