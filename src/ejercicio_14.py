#Mediante un ciclo while, implementa un juego de adivinanza: el programa genera un número aleatorio del 1 al 10 y solicita al usuario que lo adivine. El proceso se repite hasta que el usuario acierte. Muestra un mensaje de felicitación al final.",
print("Ejercicio 14:")
import random
numero_secreto = random.randint(1, 10)
intento = None
while intento != numero_secreto:
    intento = int(input("Adivina el número (1-10): "))
print("¡Felicidades! Adivinaste el número.")
print()