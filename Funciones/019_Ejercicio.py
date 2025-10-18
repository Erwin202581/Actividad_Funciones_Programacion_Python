# Ordena y Mezcla argumentos #

def calcular_descuento(precio, porcentaje):
    descuento = precio * (porcentaje / 100)
    return precio - descuento

print("\n---Ejercicio 19---")
print(f"Precio original: 100")
print(f"Precio con 10% descuento: {calcular_descuento(100, porcentaje=10)}\n")