#Ejercicio 14 – while
##Enunciado:
##Mediante un ciclo while, implementa un juego de adivinanza: el programa genera un número aleatorio del 1 al 10 y solicita 
##al usuario que lo adivine. El proceso se repite hasta que el usuario acierte. Muestra un mensaje de felicitación al final.

import random 

numero_aleatorio = random.randint(1, 10)
adivinanza = None
while adivinanza != numero_aleatorio:
    adivinanza = int(input("Adivina el número (entre 1 y 10): "))
    if adivinanza < numero_aleatorio:
        print("Demasiado bajo, intenta de nuevo.")
    elif adivinanza > numero_aleatorio:
        print("Demasiado alto, intenta de nuevo.")

        print("¡Felicidades! Adivinaste el número.")
        