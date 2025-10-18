# Argumentos nombrados básicos #

def mostrar_detalle(producto, cantidad, precio):
    print(f"{cantidad} unidades de {producto} a ${precio} cada una. Total ${cantidad * precio}")

    
print("\n---Ejercicio 13---")
mostrar_detalle(precio=2500, producto="Leche", cantidad=5)