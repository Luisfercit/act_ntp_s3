    #Utilizando un ciclo while, solicita al usuario que ingrese números. El proceso termina cuando el usuario escriba 0. Al final, muestra la suma total de todos los números ingresados.",#
total = 0
while True:
    n = input("Número (0 para salir): ")
    if n == "0":
        break
    total += int(n)
print("Total:", total)