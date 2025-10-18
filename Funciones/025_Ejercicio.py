# Combinar Obligatorio, Defecto y **kwargs

def configurar_usuario(nombre, activo=True, **detalles):
    

    print("\n---Ejercicio 25---")
    print(f"Usuario: {nombre}, Activo: {activo}")
    print(f"Detalles adicionales: {detalles}")

configurar_usuario("Leo", activo=False, rol="Admin", fecha_alta="2023-10-20")