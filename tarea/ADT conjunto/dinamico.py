class Conjunto:
    def __init__(self):
        # Inicializamos el conjunto como una list vacía
        self._elementos = []

    # Getter: obtener los elementos del conjunto
    def get_elementos(self):
        return self._elementos

    # Setter: establecer los elementos del conjunto
    def set_elementos(self, elementos):
        # Aseguramos que no haya elementos duplicados
        self._elementos = list(set(elementos))

    # Método para agregar un elemento al conjunto
    def agregar(self, elemento):
        if elemento not in self._elementos:
            self._elementos.append(elemento)

    # Método para eliminar un elemento del conjunto
    def eliminar(self, elemento):
        if elemento in self._elementos:
            self._elementos.remove(elemento)

    # Método para verificar si un elemento está en el conjunto
    def pertenece(self, elemento):
        return elemento in self._elementos

# Crear un conjunto
mi_conjunto = Conjunto()

# Usar setter para agregar varios elementos
mi_conjunto.set_elementos([1, 2, 3, 3, 4])
print("Conjunto después del setter:", mi_conjunto.get_elementos())

# Agregar un elemento
mi_conjunto.agregar(5)
print("Después de agregar 5:", mi_conjunto.get_elementos())

# Eliminar un elemento
mi_conjunto.eliminar(2)
print("Después de eliminar 2:", mi_conjunto.get_elementos())

# Verificar si un elemento pertenece
print("¿El 3 pertenece al conjunto?", mi_conjunto.pertenece(3))
