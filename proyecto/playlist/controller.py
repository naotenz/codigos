from model import Estudiante, Nodo

class EstudianteController:
    def __init__(self):
        self.cabeza = None

    # ✅ Inscribir estudiante ordenado alfabéticamente por apellido
    def inscribir_estudiante(self, estudiante):
        nuevo_nodo = Nodo(estudiante)
        if not self.cabeza or estudiante.apellido < self.cabeza.estudiante.apellido:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
            return

        actual = self.cabeza
        while actual.siguiente and actual.siguiente.estudiante.apellido < estudiante.apellido:
            actual = actual.siguiente
        nuevo_nodo.siguiente = actual.siguiente
        actual.siguiente = nuevo_nodo

    # ✅ Eliminar estudiante por ID
    def dar_de_baja(self, id):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.estudiante.id == id:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    # ✅ Buscar estudiante por ID
    def buscar_estudiante(self, id):
        actual = self.cabeza
        while actual:
            if actual.estudiante.id == id:
                return actual.estudiante
            actual = actual.siguiente
        return None

    # ✅ Actualizar calificaciones
    def actualizar_calificaciones(self, id, nuevas_calificaciones):
        estudiante = self.buscar_estudiante(id)
        if estudiante:
            estudiante.calificaciones = nuevas_calificaciones
            return True
        return False

    # ✅ Calcular promedio
    def promedio_estudiante(self, id):
        estudiante = self.buscar_estudiante(id)
        if estudiante:
            return estudiante.promedio()
        return None

    # ✅ Generar reporte general
    def generar_reporte(self):
        reporte = []
        actual = self.cabeza
        while actual:
            reporte.append(str(actual.estudiante))
            actual = actual.siguiente
        return "\n".join(reporte) if reporte else "No hay estudiantes registrados."


