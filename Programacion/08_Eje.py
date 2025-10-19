# Clase Empleado con Salario y Aumentos 

class Empleado:
    # 1. Constructor (__init__): Inicializa el nombre, puesto y salario.
    def __init__(self, nombre, puesto, salario_mensual):
        self.nombre = nombre
        self.puesto = puesto
        self.salario_mensual = salario_mensual

    # 2. Método para obtener el salario anual.
    def obtener_salario_anual(self):
        return self.salario_mensual * 12

    # 3. Método para aplicar aumento: Valida el porcentaje y actualiza el salario.
    def aplicar_aumento(self, porcentaje_aumento):
        if 0 < porcentaje_aumento <= 100:
            aumento = self.salario_mensual * (porcentaje_aumento / 100)
            self.salario_mensual += aumento
            return f"Salario de {self.nombre} aumentado en {porcentaje_aumento}%. Nuevo salario mensual: ${self.salario_mensual:.2f}."
        else:
            return "El porcentaje de aumento debe estar entre 0 y 100."

    # 4. Método para mostrar toda la información del empleado.
    def mostrar_info(self):
        return f"Empleado: {self.nombre} | Puesto: {self.puesto} | Salario Mensual: ${self.salario_mensual:.2f} | Salario Anual: ${self.obtener_salario_anual():.2f}"

# --- USO DE LA CLASE (FUERA DE LA DEFINICIÓN) ---

empleado1 = Empleado("Carlos Ruiz", "Desarrollador", 3000)
print("\n--- Empleado 1 ---")
print(empleado1.mostrar_info())
print(empleado1.aplicar_aumento(10)) # Aumento del 10%
print(empleado1.mostrar_info())
print(empleado1.aplicar_aumento(5))  # Otro aumento del 5%
print(empleado1.mostrar_info())
print(empleado1.aplicar_aumento(-2)) # Aumento inválido

empleado2 = Empleado("Elena Martín", "Diseñadora", 2500)
print("\n--- Empleado 2 ---")
print(empleado2.mostrar_info())
print(empleado2.aplicar_aumento(15))
print(empleado2.mostrar_info())