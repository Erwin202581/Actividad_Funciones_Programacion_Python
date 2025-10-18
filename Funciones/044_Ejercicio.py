# Combinación Avanzada

def completa(posicional, /, estandar, *, nombrado):
    return f"Posicional: {posicional}, Estándar: {estandar}, Nombrado: {nombrado}"

print("\n--- Ejercicio 44 ---")
print(completa(1, 2, nombrado=3))
