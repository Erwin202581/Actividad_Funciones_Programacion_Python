# Función Anidada


def calcular_total(base, iva):
    def aplicar_impuesto(monto):
        return monto * (1 + iva)
    
    return aplicar_impuesto(base)

print("\n--- Ejercicio 34 ---")
print(f"Total con IVA (19%): {calcular_total(100, 0.19):.2f}")

