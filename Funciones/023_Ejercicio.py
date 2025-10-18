# Uso de **kwargs #

def mostrar_perfil(**datos):
    print("Datos de perfil:")
    for clave, valor in datos.items():
        print(f"- {clave.capitalize()}: {valor}")

print("\n---Ejercicio 23---")
mostrar_perfil(nombre="Erwin", edad=43, pais="Colombia")