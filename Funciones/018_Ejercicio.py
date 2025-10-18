# Cadena de texto con defecto #

def crear_etiqueta(texto, simbolo='*'):
    return f"{simbolo * 5} {texto} {simbolo * 5}"

print("\n---Ejercicio 18---")
print(crear_etiqueta("Titulo"))
print(crear_etiqueta("Destacado", "#"))