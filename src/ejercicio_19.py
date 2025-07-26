#"Con un ciclo for, cuenta cuántas vocales
#  (sin distinción de mayúsculas/minúsculas) hay en la frase frase = \"programacion es divertida\" y muestra el total.
print("Ejercicio 19:")
frase = "programacion es divertida"
vocales = "aeiou"
contador = 0
for letra in frase.lower():
    if letra in vocales:
        contador += 1
print("Cantidad de vocales:", contador)
print()