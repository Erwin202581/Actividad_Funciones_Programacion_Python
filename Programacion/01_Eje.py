# Clase Persona Básica

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre}."

    def cumplir_anios(self):
        self.edad += 1
        return f"Feliz cumpleaños, {self.nombre}. Ahora tienes {self.edad} años."

# Creación de instancias
persona1 = Persona("Erwin", 43)
print(persona1.saludar())
print(persona1.cumplir_anios())

persona2 = Persona("Carlos", 25)
print(persona2.saludar())