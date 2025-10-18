# Decorador Básico

def log_llamada(func):
    def wrapper(*args, **kwargs):
        print(f"\n--- Iniciando {func.__name__} ---")
        resultado = func(*args, **kwargs)
        print(f"--- Finalizando {func.__name__} ---")
        return resultado
    return wrapper

@log_llamada
def procesar_datos(data):
    return data.upper()

print("\n--- Ejercicio 50 (Decorador) ---")
print(f"Resultado: {procesar_datos('ejemplo de funcion')}")


