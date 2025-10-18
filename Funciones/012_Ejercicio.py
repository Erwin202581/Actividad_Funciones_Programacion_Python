# Múltiples valores por defecto #

def formatear_precio(valor, moneda="$", decimales=2):
    return f"{moneda}{valor:.{decimales}f}"

print("\n---Ejercicio 12---")
print(formatear_precio(19.99))
print(formatear_precio(150, "€", 0))