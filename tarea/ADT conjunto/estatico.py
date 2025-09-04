class ConjuntoEstatico:
    def __init__(self, capacidad=10):
        self._elementos = [None] * capacidad
        self._tam = 0
        self._capacidad = capacidad

    def get_elementos(self):
        return [e for e in self._elementos if e is not None]

    def set_elementos(self, elementos):
        unicos = list(set(elementos))
        if len(unicos) <= self._capacidad:
            self._elementos = unicos + [None] * (self._capacidad - len(unicos))
            self._tam = len(unicos)

    def agregar(self, elemento):
        if elemento not in self.get_elementos() and self._tam < self._capacidad:
            self._elementos[self._tam] = elemento
            self._tam += 1
# Crear un conjunto estático de tamaño 5
c_estatico = ConjuntoEstatico(capacidad=5)

# Usar setter
c_estatico.set_elementos([1, 2, 3, 3])
print("Conjunto estático después del setter:", c_estatico.get_elementos())

# Agregar un elemento
c_estatico.agregar(4)
print("Después de agregar 4:", c_estatico.get_elementos())
