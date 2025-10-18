# Reenvio de Argumentos (Wrapper)

def base(a, b):
    return a * b + b

def envoltura(*args, **kwargs):
    
    print("\n---Ejercicio 28---")
    print("Ejecutando envoltura...")
    resultado = base(*args, **kwargs)
    return resultado

print(f"Resultado de la envoltura: {envoltura(5, b=3)}")