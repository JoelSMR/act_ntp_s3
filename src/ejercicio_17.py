numero = input("Ingresa un número entero psositivo: ")
suma_digitos = 0 
for digito in numero:
    if digito.isdigit():
        suma_digitos += int(digito)
print(f"La suma de los dígitos de {numero} es: {suma_digitos}")
