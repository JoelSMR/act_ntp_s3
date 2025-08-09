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



