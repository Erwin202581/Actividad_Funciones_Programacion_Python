#  Recursión: Factorial

def factorial(n):
    if n <= 1: # Caso base
        return 1
    return n * factorial(n - 1) # Caso recursivo

print("\n--- Ejercicio 45 (Factorial) ---")
print(f"5 es factor de : {factorial(5)}") 
