# Validación simple#

def dividir_seguro(dividendo, divisor):
    if divisor == 0:
        return "Error No se puede dividir por cero."
    return dividendo / divisor

print("\n---Ejercicio 20---")
print(f"Resultado de 10/2: {dividir_seguro(10, 2)}")
print(f"Resultado de 10/0: {dividir_seguro(10, 0)}\n")