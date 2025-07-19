#Ejercicio 07 – for
##Enunciado:
##Con un ciclo for, cuenta cuántas letras “a” (minúscula) hay en la cadena texto = "manzana" y muestra el total.

texto = "manzana"
contador_a = 0
for letra in texto:
    if letra == "a":
        contador_a += 1
print(f"El total de letras 'a' en la cadena es: {contador_a}")
