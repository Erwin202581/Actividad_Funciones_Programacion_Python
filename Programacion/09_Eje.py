# Clase Rectángulo con Cálculo de Área y Perímetro 

class Rectangulo:
    # 1. Constructor (__init__): Inicializa el largo y el ancho.
    def __init__(self, largo, ancho):
        # Valida que el largo y el ancho sean positivos; si no, lanza un error.
        if largo > 0 and ancho > 0:
            self.largo = largo
            self.ancho = ancho
        else:
            # Uso de 'raise ValueError' para forzar una excepción si los datos son incorrectos.
            raise ValueError("El largo y el ancho deben ser valores positivos.")

    # 2. Método para calcular el área.
    def calcular_area(self):
        return self.largo * self.ancho

    # 3. Método para calcular el perímetro.
    def calcular_perimetro(self):
        return 2 * (self.largo + self.ancho)

    # 4. Método para mostrar las dimensiones.
    def mostrar_dimensiones(self):
        return f"Rectángulo con Largo: {self.largo} unidades, Ancho: {self.ancho} unidades."

# --- USO DE LA CLASE (FUERA DE LA DEFINICIÓN) ---

# Uso de un bloque try...except para manejar la posible excepción ValueError
try:
    rectangulo1 = Rectangulo(10, 5)
    print("\n--- Rectángulo 1 (Válido) ---")
    print(rectangulo1.mostrar_dimensiones())
    print(f"Área: {rectangulo1.calcular_area()} unidades cuadradas.")
    print(f"Perímetro: {rectangulo1.calcular_perimetro()} unidades.")

    rectangulo2 = Rectangulo(7.5, 3)
    print("\n--- Rectángulo 2 (Decimal) ---")
    print(rectangulo2.mostrar_dimensiones())
    print(f"Área: {rectangulo2.calcular_area()} unidades cuadradas.")
    print(f"Perímetro: {rectangulo2.calcular_perimetro()} unidades.")

    # Intentar crear un rectángulo con dimensiones inválidas (provoca el error)
    print("\n--- Intento de Rectángulo Inválido ---")
    rectangulo_invalido = Rectangulo(-5, 2)
except ValueError as e:
    print(f"Error al crear rectángulo: {e}")