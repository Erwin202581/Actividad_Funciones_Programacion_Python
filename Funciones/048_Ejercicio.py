# Generadores (yield)

def secuencia_par(N):
    n = 0
    while n <= N:
        yield n
        n += 2

print("\n--- Ejercicio 48 (Generador) ---")
print("Números pares generados:")
for num in secuencia_par(10):
    print(num)
