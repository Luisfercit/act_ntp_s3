#Utilizando un ciclo while, calcula el factorial de un número entero n introducido por el usuario y muestra el resultado.
print("Ejercicio 12:")
n = int(input("Ingrese un número para calcular su factorial: "))
factorial = 1
contador = 1
while contador <= n:
    factorial *= contador
    contador += 1
print("Factorial:", factorial)
print()