#Ejercicio 16 – while
##Enunciado:
##Utilizando un ciclo while, simula un reloj digital que muestre cada segundo desde 00:00 hasta 00:59 
##en formato MM:SS, cada valor en una línea.

import time
minuto = 0
segundo = 0

while segundo <= 59 :
    print(f"{minuto:02}:{segundo:02}")
    time.sleep(1)  
    
    segundo += 1

