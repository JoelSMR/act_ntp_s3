#Ejercicio 12 – while
##Enunciado:
##Utilizando un ciclo while, calcula el factorial de un número entero n introducido por el usuario y muestra el resultado.

n = int(input("Introduce un número entero para calcular su factorial: "))
factorial = 1
contador = 1
while contador <= n:
        factorial *= contador
        contador += 1 
print(f"El factorial de {n} es {factorial}")
