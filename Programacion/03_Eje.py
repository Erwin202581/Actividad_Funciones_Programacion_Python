# Clase Cuenta Bancaria 

class CuentaBancaria:
    # 1. Constructor (__init__): Inicializa el saldo con un valor por defecto (0).
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial  # Atributo 'saldo' del objeto

    # 2. Método depositar: Aumenta el saldo si la cantidad es positiva.
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return f"Depósito de {cantidad} realizado. Nuevo saldo: {self.saldo}"
        else:
            return "La cantidad a depositar debe ser positiva."

    # 3. Método retirar: Disminuye el saldo si hay fondos suficientes y la cantidad es positiva.
    def retirar(self, cantidad):
        if cantidad > 0:
            if self.saldo >= cantidad:
                self.saldo -= cantidad
                return f"Retiro de {cantidad} realizado. Nuevo saldo: {self.saldo}"
            else:
                return "Saldo insuficiente."
        else:
            return "La cantidad a retirar debe ser positiva."

    # 4. Método consultar_saldo: Devuelve el saldo actual.
    def consultar_saldo(self):
        return f"Saldo actual: {self.saldo}"

# --- USO DE LA CLASE (FUERA DE LA DEFINICIÓN) ---

# Creación de la instancia con un saldo inicial de 1000
cuenta = CuentaBancaria(1000)
print("\n--- Transacciones de Prueba ---")
print(cuenta.consultar_saldo())
print(cuenta.depositar(500))  # Saldo: 1500
print(cuenta.retirar(200))    # Saldo: 1300
print(cuenta.retirar(1500))   # Falla (Saldo insuficiente)
print(cuenta.consultar_saldo())
print(cuenta.depositar(-100)) # Falla (Cantidad negativa)





























