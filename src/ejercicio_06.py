#Ejercicio 06 – while
##Enunciado:
##Mediante un ciclo while, genera y muestra los primeros 15 múltiplos de 3, comenzando desde 3.

i = 1
while i <= 15:
    multiplo = 3 * i
    print(multiplo)
    i += 1
    print(f"El múltiplo de 3 en la posición {i} es: {multiplo}")