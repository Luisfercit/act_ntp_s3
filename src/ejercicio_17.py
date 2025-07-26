#"Con un ciclo for, solicita al usuario que ingrese un número entero positivo y calcula la suma de sus dígitos, mostrando el resultado final.""

numero = int(input("Ingrese un número entero positivo: "))
suma_digitos = 0
for digito in str(numero):
    suma_digitos += int(digito)
print("Suma de dígitos:", suma_digitos)
print()