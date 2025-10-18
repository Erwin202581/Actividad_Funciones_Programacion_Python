# Unpacking de tupla con función

def coord(x, y):
    return f"Coodenada: ({x}, {y})"

print("\n---Ejercicio 26---")
punto = (3, 5)
print(f"Resultado de unpacking de tupla: {coord(*punto)}\n")