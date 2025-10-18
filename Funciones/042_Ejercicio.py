# Función de Parámetros Flexibles (Posición o Nombre)

def datos_flexibles(a, b):
    return f"Valor de A: {a}, Valor de B: {b}"

print("\n--- Ejercicio 42 (Solo Posicional) ---")
resultado_posicional = datos_flexibles(100, 200)
print(f"Llamada Posicional: {resultado_posicional}")

resultado_nombre = datos_flexibles(b=300, a=400)
print(f"Llamada por Nombre (Keyword): {resultado_nombre}")


