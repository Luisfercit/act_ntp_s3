#"Utilizando un ciclo while, solicita al usuario que ingrese edades una a una.
#  El proceso termina cuando se introduzca -1. Al final, muestra la edad mayor que se haya ingresado.
print("Ejercicio 20:")
edad_maxima = -1
while True:
    edad = int(input("Ingrese una edad (-1 para terminar): "))
    if edad == -1:
        break
    if edad > edad_maxima:
        edad_maxima = edad
print("Edad máxima ingresada:", edad_maxima)