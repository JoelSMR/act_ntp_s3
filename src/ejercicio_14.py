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
        