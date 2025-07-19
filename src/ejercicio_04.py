#Ejercicio 04 – while
##Enunciado:
##Utilizando un ciclo while, solicita al usuario que ingrese números. 
##El proceso termina cuando el usuario escriba 0. Al final, muestra la suma total de todos los números ingresados.

suma = 0
numero = None

while numero != 0:
    numero = int(input("Ingrese un número (0 para terminar): "))
    suma += numero

print("La suma total de los números ingresados es:", suma)