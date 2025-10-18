# Closure con nonlocal

def fabrica_de_contadores(inicio=0):
    n = inicio
    def incrementar():
        nonlocal n
        n += 1
        return n
    return incrementar

print("\n--- Ejercicio 39 ---")
contador_A = fabrica_de_contadores(10)
print(f"Contador A: {contador_A()}")
print(f"Contador A: {contador_A()}")
print(f"Contador A: {contador_A()}")

