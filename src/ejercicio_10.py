#Ejercicio 10 – while
##Enunciado:
##Mediante un ciclo while, solicita al usuario que escriba palabras. El proceso termina cuando el usuario escriba la palabra “fin”. 
##Al final, muestra cuántas palabras se leyeron (sin contar “fin”).

contador_palabras = 0
palabra = ""
while palabra != "fin":
    palabra = input("Escribe una palabra (escribe 'fin' para terminar): ")
    if palabra != "fin":
        contador_palabras += 1
        print(f"palabra leída: {palabra}")

        print(f"palabras leídas hasta ahora: {contador_palabras}")

    print (f"Total de palabras leídas (sin contar 'fin'): {contador_palabras}")
print("Proceso terminado.")



