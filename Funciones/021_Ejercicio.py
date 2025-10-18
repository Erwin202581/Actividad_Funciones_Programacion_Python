# Uso de *args #

def promedio(*numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

print("\n---Ejercicio 21---")
print(f"El promedio de 10, 20, 30, 40 es: {promedio(10,20, 30, 40)}\n")