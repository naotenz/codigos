class Nodo:
    def __init__(self, data):
        """Inicializa un nodo con un valor (data) y un puntero next como None."""
        self.data = data  # El valor que almacena el nodo
        self.next = None  # Puntero al siguiente nodo, inicialmente None

class ListaEnlazada:
    def __init__(self):
        """Inicializa la lista enlazada con el head (primer nodo) como None."""
        self.head = None  # El primer nodo de la lista, inicialmente vacío
    
    def append(self, data):
        """Agrega un nuevo valor al final de la lista enlazada.
        
        - Si la lista está vacía (head es None), el nuevo nodo se convierte en head.
        - Si no, recorre la lista hasta el último nodo (donde next es None) y agrega el nuevo nodo allí.
        """
        nuevo_nodo = Nodo(data)  # Crea un nuevo nodo con el valor proporcionado
        
        if self.head is None:  # Si la lista está vacía
            self.head = nuevo_nodo  # El nuevo nodo se convierte en el head
        else:
            actual = self.head  # Comienza desde el head
            while actual.next is not None:  # Recorre hasta el final de la lista
                actual = actual.next  # Avanza al siguiente nodo
            # Ahora, actual es el último nodo, así que enlaza el nuevo nodo
            actual.next = nuevo_nodo  # El next del último nodo apunta al nuevo nodo
    
    def mostrar(self):
        """Imprime los elementos de la lista enlazada para verificar su contenido.
        
        Recorre la lista desde el head hasta el final.
        """
        if self.head is None:
            print("La lista está vacía.")
            return
        actual = self.head
        print("Elementos en la lista: ", end="")
        while actual is not None:  # Mientras haya nodos
            print(actual.data, end=" -> ")  # Imprime el data del nodo
            actual = actual.next  # Avanza al siguiente nodo
        print("None")  # Indica el final de la lista

# Ejemplo de uso para la lista enlazada
print("Ejemplo con Lista Enlazada:")

lista = ListaEnlazada()  # Crea una nueva lista enlazada

# Agregamos valores uno por uno
lista.append(1)  # Primer valor: Se convierte en el head, con next = None
print("Después de agregar 1:")
lista.mostrar()  # Debería mostrar: Elementos en la lista: 1 -> None

lista.append(2)  # Segundo valor: Se agrega al final del primer nodo
print("Después de agregar 2:")
lista.mostrar()  # Debería mostrar: Elementos en la lista: 1 -> 2 -> None

lista.append(3)  # Tercer valor: Se agrega al final
print("Después de agregar 3:")
lista.mostrar()  # Debería mostrar: Elementos en la lista: 1 -> 2 -> 3 -> None

lista.append(4)  # Cuarto valor: Se agrega al final
print("Después de agregar 4:")
lista.mostrar()  # Debería mostrar: Elementos en la lista: 1 -> 2 -> 3 -> 4 -> None

# Verificación: Si intentamos agregar a una lista vacía (crea una nueva para probar)
nueva_lista = ListaEnlazada()  # Lista vacía
nueva_lista.append(5)  # Agrega el primer valor
print("Después de agregar 5 a una lista vacía:")
nueva_lista.mostrar()  # Debería mostrar: Elementos en la lista: 5 -> None