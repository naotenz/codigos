class Automovil:
    def __init__(self, marca, modelo, anio):
        self._marca = marca
        self._modelo = modelo
        self._anio = anio

    # Getters
    def get_marca(self):
        return self._marca

    def get_modelo(self):
        return self._modelo

    def get_anio(self):
        return self._anio

    # Setters
    def set_marca(self, marca):
        self._marca = marca

    def set_modelo(self, modelo):
        self._modelo = modelo

    def set_anio(self, anio):
        self._anio = anio

    def __str__(self):
        return f"Automovil(marca={self._marca}, modelo={self._modelo}, anio={self._anio})"

# Ejemplo de uso con estructura dinámica (lista)
autos = []

# Crear objetos Automovil y agregarlos a la lista
auto1 = Automovil("Toyota", "Corolla", 2020)
auto2 = Automovil("Honda", "Civic", 2019)
auto3 = Automovil("Ford", "Focus", 2021)

autos.append(auto1)
autos.append(auto2)
autos.append(auto3)

# Mostrar información de los automóviles
for auto in autos:
    print(auto)

# Modificar datos usando setters
autos[0].set_modelo("Yaris")
autos[1].set_anio(2022)

print("\nDespués de modificar:")
for auto in autos:
    print(f"Marca: {auto.get_marca()}, Modelo: {auto.get_modelo()}, Año: {auto.get_anio()}")