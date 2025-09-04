import json

class ConjuntoDisco:
    def __init__(self, archivo="conjunto.json"):
        self.archivo = archivo
        self._elementos = []
        self._cargar()

    def get_elementos(self):
        return self._elementos

    def set_elementos(self, elementos):
        self._elementos = list(set(elementos))
        self._guardar()

    def _guardar(self):
        with open(self.archivo, "w") as f:
            json.dump(self._elementos, f)

    def _cargar(self):
        try:
            with open(self.archivo, "r") as f:
                self._elementos = json.load(f)
        except FileNotFoundError:
            self._elementos = []
# Crear un conjunto en disco
c_disco = ConjuntoDisco("mis_datos.json")

# Usar setter
c_disco.set_elementos([10, 20, 20, 30])
print("Conjunto en disco después del setter:", c_disco.get_elementos())

# Volvemos a cargar para comprobar que se guardó
nuevo = ConjuntoDisco("mis_datos.json")
print("Conjunto cargado desde el archivo:", nuevo.get_elementos())
