# Tipado y Docstrings

import math

def area_circulo(radio: float) -> float:
    """Calcula el área de un círculo.
    
    Args:
        radio: Radio del círculo.
    
    Returns:
        El área calculada.
    """
    return math.pi * radio ** 2

print("\n--- Ejercicio 49 (Tipado) ---")
print(f"Área del círculo de radio 3: {area_circulo(3.0):.2f}")

