#Mediante un ciclo while, genera y muestra la secuencia de Fibonacci
#  empezando por 1, 1, 2, 3, 5, … y termina cuando se alcance el primer valor mayor que 1000.
print("Ejercicio 18:")
a, b = 1, 1
print(a)
while b <= 1000:
    print(b)
    a, b = b, a + b
print()
