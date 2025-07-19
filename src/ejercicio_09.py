#Ejercicio 09 – for
##Enunciado:
##Con un ciclo for, imprime todos los números pares del 2 al 50 (ambos inclusive), cada número en una línea.

for i in range(2, 51, 2):
    print(i)
    print(f"El número par en la posición {i // 2} es: {i}")
    