# Uso de .get() en **kwargs

def verificar_permiso(**config):
    es_admin = config.get('permiso_admin', False)
    return f"Acceso: {'Permitido' if es_admin else 'Denegado'}"

print("\n---Ejercicio 30---")
print(verificar_permiso(rol="dev", permiso_admin=True))
print(verificar_permiso(rol="user"))