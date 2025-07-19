#Ejercicio 20 – while
##Enunciado:
##Utilizando un ciclo while, solicita al usuario que ingrese edades una a una. 
##El proceso termina cuando se introduzca -1. Al final, muestra la edad mayor que se haya ingresado.

def edad_mayor():
    edad = 0
    mayor = 0
    while edad != -1:
        edad = int(input("Ingrese una edad (o -1 para terminar): "))
        if edad > mayor:
            mayor = edad
    if mayor != 0:
        print("La edad mayor ingresada es:", mayor)
    else:
        print("No se ingresaron edades válidas.")
edad_mayor()
