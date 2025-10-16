# Importamos la biblioteca necesaria para la cola (usaremos una lista simple por simplicidad)
class Pila:
    def __init__(self):
        """Inicializa la pila como una lista vacía."""
        self.items = []  # Lista para almacenar los elementos
    
    def push(self, elemento):
        """Agrega un elemento a la pila (al final de la lista, para LIFO)."""
        self.items.append(elemento)  # Agrega al final
    
    def pop(self):
        """Remueve y devuelve el último elemento de la pila (el que entró último)."""
        if not self.isEmpty():
            return self.items.pop()  # Remueve el último elemento
        else:
            raise IndexError("La pila está vacía, no se puede remover elemento")
    
    def peek(self):
        """Devuelve el último elemento de la pila sin removerlo."""
        if not self.isEmpty():
            return self.items[-1]  # Accede al último elemento
        else:
            raise IndexError("La pila está vacía")
    
    def isEmpty(self):
        """Verifica si la pila está vacía."""
        return len(self.items) == 0  # Retorna True si no hay elementos

class Cola:
    def __init__(self):
        """Inicializa la cola como una lista vacía."""
        self.items = []  # Lista para almacenar los elementos
    
    def enqueue(self, elemento):
        """Agrega un elemento al final de la cola (para FIFO)."""
        self.items.append(elemento)  # Agrega al final
    
    def dequeue(self):
        """Remueve y devuelve el primer elemento de la cola (el que entró primero)."""
        if not self.isEmpty():
            return self.items.pop(0)  # Remueve el primer elemento
        else:
            raise IndexError("La cola está vacía, no se puede remover elemento")
    
    def peek(self):
        """Devuelve el primer elemento de la cola sin removerlo."""
        if not self.isEmpty():
            return self.items[0]  # Accede al primer elemento
        else:
            raise IndexError("La cola está vacía")
    
    def isEmpty(self):
        """Verifica si la cola está vacía."""
        return len(self.items) == 0  # Retorna True si no hay elementos

# Ejemplo de uso para la pila
print("Ejemplo con Pila (LIFO):")
pila = Pila()
pila.push("A")  # Primer valor que entra
pila.push("B")  # Segundo valor
pila.push("C")  # Último valor

print("Tope de la pila:", pila.peek())  # Debería ser C
print("Removiendo elementos:")
print(pila.pop())  # Sale C (último que entró)
print(pila.pop())  # Sale B
print(pila.pop())  # Sale A (primero que entró)
print("¿La pila está vacía?", pila.isEmpty())  # True

# Ejemplo de uso para la cola
print("\nEjemplo con Cola (FIFO):")
cola = Cola()
cola.enqueue("A")  # Primer valor que entra
cola.enqueue("B")  # Segundo valor
cola.enqueue("C")  # Último valor

print("Frente de la cola:", cola.peek())  # Debería ser A
print("Removiendo elementos:")
print(cola.dequeue())  # Sale A (primero que entró)
print(cola.dequeue())  # Sale B
print(cola.dequeue())  # Sale C (último que entró)
print("¿La cola está vacía?", cola.isEmpty())  # True