# Función que llama a otra #

def sumar(a, b):
    return a + b

def imprimir_suma(a, b):
    total = sumar(a, b)
    print(f"La suma de {a} y {b} es: {total}")

print("\n---Ejercicio 8---")
imprimir_suma(5, 15)