# Closure Básico

def crear_mensaje(nombre):
    def saludar():
        return f"Hola {nombre} (usando closure)"
    return saludar

print("\n--- Ejercicio 38 ---")
saludo_a_Erwin = crear_mensaje("Erwin")
print(saludo_a_Erwin())
