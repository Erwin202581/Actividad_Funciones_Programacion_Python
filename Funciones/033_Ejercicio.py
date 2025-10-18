# Modificar Variable Global

contador = 0

def incrementar():
    global contador
    contador += 1
    print(f"Contador actual: {contador}")

print("\n--- Ejercicio 33 ---")
incrementar()
incrementar()
incrementar()
print(f"Valor global final del contador: {contador}")


