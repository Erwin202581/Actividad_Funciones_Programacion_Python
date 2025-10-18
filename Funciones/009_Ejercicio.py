# Función con un parámetro Opcional #

def buscar_usuario(id, base_datos=None):
    if base_datos is None:
        print(f"Buscar usuario {id} en la base de datos por defecto.")
    else:
        print(f"Buscando usuario {id} en la base de datos: {base_datos}")


print("\n---Ejercicio 9---")
buscar_usuario(101)
buscar_usuario(202, base_datos="Producción\n")