# Unpacking de diccionario con función

def datos_unpacking(nombre, edad):
    return f"{nombre} tiene {edad} años."

print("\n---Ejercicio 27---")
info = {'nombre': 'Erwin', 'edad': 40}
print(f"Resultado del unpacking de diccionario: {datos_unpacking(**info)}")