# Solución a valor por defecto mutable

def agregar_elemento_ok(item, lista=None):
    if lista is None:
        lista = []
    lista.append(item)
    return lista

print("\n--- Ejercicio 41 (Solución) ---")
print(f"Primera llamada: {agregar_elemento_ok(1)}") 
print(f"Segunda llamada: {agregar_elemento_ok(2)}") 
