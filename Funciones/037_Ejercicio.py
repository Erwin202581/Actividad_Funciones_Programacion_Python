# Función como Objeto

def sumar_func(a, b): return a + b
def restar_func(a, b): return a - b

def ejecutar_operacion(func, a, b):
    return func(a, b)

print("\n--- Ejercicio 37 ---")
print(f"Resultado de la suma: {ejecutar_operacion(sumar_func, 20, 5)}")
print(f"Resultado de la resta: {ejecutar_operacion(restar_func, 20, 5)}")

