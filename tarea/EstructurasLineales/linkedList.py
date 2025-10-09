# Definición del nodo
class Nodo:
    def __init__(self, data):
        self.data = data     # almacena el dato
        self.next = None     # apunta al siguiente nodo

# Definición de la lista enlazada
class ListaEnlazada:
    def __init__(self):
        self.head = None     # inicio de la lista

    # Insertar al final
    def insertar(self, data):
        nuevo = Nodo(data)
        if not self.head:
            self.head = nuevo
            return
        actual = self.head
        while actual.next:
            actual = actual.next
        actual.next = nuevo

    # Mostrar todos los elementos
    def mostrar(self):
        actual = self.head
        while actual:
            print(actual.data, end=" -> ")
            actual = actual.next
        print("None")

# Ejemplo de uso
lista = ListaEnlazada()
lista.insertar("Lechuga")
lista.insertar("Tomate")
lista.insertar("Cebolla")

lista.mostrar()
