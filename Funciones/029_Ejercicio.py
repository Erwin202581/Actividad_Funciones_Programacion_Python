# VAlidación con *args

def filtrar_mayores_a_diez(*numeros):
    return [n for n in numeros if n > 10]

print("\n---Ejercicio 29---")
mayores = filtrar_mayores_a_diez(5, 12, 8, 20, 3, 11)
print(f"Números mayores a 10: {mayores}")