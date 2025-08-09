def edad_mayor():
    edad = 0
    mayor = 0
    while edad != -1:
        edad = int(input("Ingrese una edad (o -1 para terminar): "))
        if edad > mayor:
            mayor = edad
    if mayor != 0:
        print("La edad mayor ingresada es:", mayor)
    else:
        print("No se ingresaron edades válidas.")
edad_mayor()
