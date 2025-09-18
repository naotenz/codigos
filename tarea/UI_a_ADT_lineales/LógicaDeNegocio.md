class Conjunto:
    def __init__(self, elementos=None):
        self.elementos = set(elementos) if elementos else set()

    def union(self, otro):
        return Conjunto(self.elementos | otro.elementos)

    def interseccion(self, otro):
        return Conjunto(self.elementos & otro.elementos)

    def __str__(self):
        return str(self.elementos)
