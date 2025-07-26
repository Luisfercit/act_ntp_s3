#"Utilizando un ciclo while, simula un reloj digital que muestre cada segundo desde 00:00 hasta 00:59 en formato MM:SS, cada valor en una línea.
print("Ejercicio 16:")
minuto = 0
segundo = 0
while segundo < 60:
    print(f"{minuto:02d}:{segundo:02d}")
    segundo += 1
print()