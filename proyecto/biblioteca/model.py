class Cancion:
    def __init__(self, titulo, archivo, tipo="audio"):
        self.titulo = titulo       # Nombre de la canción/video
        self.archivo = archivo     # Ruta del archivo
        self.tipo = tipo           # "audio" o "video"

class NodoCancion:
    def __init__(self, cancion):
        self.cancion = cancion
        self.siguiente = None
        self.anterior = None

class ListaMusica:
    def __init__(self):
        self.cabeza = None
        self.actual = None

    def agregar(self, cancion):
        nodo = NodoCancion(cancion)
        if not self.cabeza:
            self.cabeza = nodo
        else:
            nodo_tmp = self.cabeza
            while nodo_tmp.siguiente:
                nodo_tmp = nodo_tmp.siguiente
            nodo_tmp.siguiente = nodo
            nodo.anterior = nodo_tmp

    def cancion_actual(self):
        return self.actual.cancion if self.actual else None

    def siguiente_cancion(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            return self.actual.cancion
        return None

    def anterior_cancion(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
            return self.actual.cancion
        return None

    def eliminar(self, cancion):
        nodo = self.cabeza
        while nodo:
            if nodo.cancion == cancion:
                if nodo.anterior:
                    nodo.anterior.siguiente = nodo.siguiente
                if nodo.siguiente:
                    nodo.siguiente.anterior = nodo.anterior
                if self.actual == nodo:
                    self.actual = nodo.siguiente or nodo.anterior
                return True
            nodo = nodo.siguiente
        return False
