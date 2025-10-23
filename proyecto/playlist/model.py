# model.py

class Estudiante:
    def __init__(self, id, nombre, apellido, calificaciones=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.calificaciones = calificaciones or []

    def promedio(self):
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

    def __str__(self):
        notas = ', '.join(map(str, self.calificaciones))
        # sin promedio aquí
        return f"ID: {self.id}, Nombre: {self.nombre} {self.apellido}, Calificaciones: [{notas}]"


class Nodo:
    def __init__(self, estudiante):
        self.estudiante = estudiante
        self.siguiente = None
