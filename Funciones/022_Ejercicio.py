# Acceder a *args #

def primero_y_ultimo(*elementos):
    if not elementos:
        return None, None
    return elementos[0], elementos[-1]

print("\n---Ejercicio 22---")
primero, ultimo = primero_y_ultimo(1, 2, 3, 4, 5)
print(f"Primer elemento: {primero} Ultimo elemento: {ultimo}\n")