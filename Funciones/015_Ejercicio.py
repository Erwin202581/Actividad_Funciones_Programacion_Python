# Devolver múltiples valores (Tupla) #

def operaciones(a, b):
    return a + b, a - b

print("\n---Ejercicio 15---")
suma, resta = operaciones(10, 4)
print(f"Suma:{suma}, resta: {resta}\n")