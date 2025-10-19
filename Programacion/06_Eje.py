# Clase Estudiante con Calificaciones 

class Estudiante:
    def __init__(self, nombre, id_estudiante):
        self.nombre = nombre
        self.id_estudiante = id_estudiante
        self.calificaciones = []

    def agregar_calificacion(self, calificacion):
        if 0 <= calificacion <= 100:
            self.calificaciones.append(calificacion)
            return f"Calificación {calificacion} agregada a {self.nombre}."
        else:
            return "Calificación inválida. Debe estar entre 0 y 100."

    def obtener_promedio(self):
        if not self.calificaciones:
            return "El estudiante aún no tiene calificaciones."
        return sum(self.calificaciones) / len(self.calificaciones)

    def mostrar_info(self):
        promedio = self.obtener_promedio()
        promedio_str = f"{promedio:.2f}" if isinstance(promedio, float) else promedio
        return f"Estudiante: {self.nombre} (ID: {self.id_estudiante}) | Calificaciones: {self.calificaciones} | Promedio: {promedio_str}"

estudiante1 = Estudiante("Ana García", "E101")
print(estudiante1.mostrar_info())
print(estudiante1.agregar_calificacion(85))
print(estudiante1.agregar_calificacion(90))
print(estudiante1.agregar_calificacion(78))
print(estudiante1.agregar_calificacion(105))
print(estudiante1.mostrar_info())
print(f"El promedio de {estudiante1.nombre} es: {estudiante1.obtener_promedio():.2f}")

estudiante2 = Estudiante("Juan Pérez", "E102")
print(estudiante2.agregar_calificacion(70))
print(estudiante2.agregar_calificacion(65))
print(estudiante2.mostrar_info())