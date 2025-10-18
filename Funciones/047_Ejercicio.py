# Memoización con lru_cache

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_rapido(n):
    if n < 2:
        return n
    return fibonacci_rapido(n-1) + fibonacci_rapido(n-2)

print("\n--- Ejercicio 47 (Memoización) ---")
print(f"Fibonacci de 40 (rápido): {fibonacci_rapido(40)}") 



