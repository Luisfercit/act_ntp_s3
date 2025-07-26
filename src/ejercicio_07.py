#Con un ciclo for, cuenta cuántas letras 'a' (minúscula) hay en la cadena texto = \"manzana\" y muestra el total."
print("Ejercicio 07:")
texto = "manzana"
contador = 0
for letra in texto:
    if letra == 'a':
        contador += 1
print("Cantidad de letras 'a':", contador)
print()