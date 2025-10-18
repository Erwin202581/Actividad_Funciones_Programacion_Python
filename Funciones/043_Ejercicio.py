# Función de Parámetros Flexibles (Posición o Nombre)

def datos_flexibles(producto, cantidad):
    return f"Detalle -> Producto: {producto}, Cantidad: {cantidad}"

print("\n--- Ejercicio 43 (Solo Nombrado) ---")
resultado_posicional = datos_flexibles("Naranjas", 12)
print(f"Llamada Posicional: {resultado_posicional}")

resultado_nombre = datos_flexibles(cantidad=8, producto="Peras")
print(f"Llamada por Nombre (Keyword): {resultado_nombre}")




