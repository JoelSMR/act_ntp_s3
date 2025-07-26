##Ejercicio 19 – for
##Enunciado:
##Con un ciclo for, cuenta cuántas vocales (sin distinción de mayúsculas/minúsculas)
## hay en la frase frase = "programacion es divertida" y muestra el total.

frase = "programacion es divertida"
vocales = "aeiou"
contador = 0
for letra in frase.lower():
    if letra in vocales:
        contador += 1
print("Total de vocales:", contador)

