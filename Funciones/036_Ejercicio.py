# Lambda con sorted()

ciudades = ["Villavicencio", "Valledupar", "Bogota", "Nariño", "Boyacá"]

print("\n--- Ejercicio 36 ---")
ordenadas = sorted(ciudades, key=lambda c: len(c)) 
print(f"Ciudades ordenadas por longitud: {ordenadas}")

