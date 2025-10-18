# Recursión: Fibonacci

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("\n--- Ejercicio 46 (Fibonacci) ---")
print(f"El número de Fibonacci en posición 7 es: {fibonacci(7)}")
