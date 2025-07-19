#Ejercicio 16 – while
##Enunciado:
##Utilizando un ciclo while, simula un reloj digital que muestre cada segundo desde 00:00 hasta 00:59 
##en formato MM:SS, cada valor en una línea.

import time 

def reloj_digital():
    minuto = 0
    segundo = 0
    while minuto < 1:
        print(f"{minuto:02}:{segundo:02}")
        time.sleep(1)
        segundo += 1
        if segundo == 60:
            segundo = 0
            minuto += 1
        if minuto == 1:
            break
    print("Fin del reloj digital.")
reloj_digital()

