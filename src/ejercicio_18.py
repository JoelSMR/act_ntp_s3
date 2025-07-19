#Ejercicio 18 – while
##Enunciado:
##Mediante un ciclo while, genera y muestra la secuencia de 
##Fibonacci empezando por 1, 1, 2, 3, 5, … y termina cuando se alcance el primer valor mayor que 1000.

def finbonacci():
    a, b = 1, 1
    while a <= 1000:
        print(a)
        a, b = b, a + b
        print("Siguiente número en la secuencia:", a)
        print("Siguiente número en la secuencia:", b)
        print("Fin de la secuencia")

finbonacci()