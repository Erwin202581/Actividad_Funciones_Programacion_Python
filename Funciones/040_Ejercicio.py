# Error de valor por defecto mutable (Lista)

def agregar_elemento(item, lista=[]):
    lista.append(item)
    return lista

print("\n--- Ejercicio 40 (Demostración de Error) ---")
print(f"Primera llamada: {agregar_elemento(1)}") 
print(f"Segunda llamada: {agregar_elemento(2)}") 

