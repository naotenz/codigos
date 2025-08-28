class Automovil:
    def __init__(self, marca, modelo, anio, color):
        self._marca = marca
        self._modelo = modelo
        self._anio = anio
        self._color = color

    # Getters
    def get_marca(self):
        return self._marca

    def get_modelo(self):
        return self._modelo

    def get_anio(self):
        return self._anio

    def get_color(self):
        return self._color

    # Setters
    def set_marca(self, marca):
        self._marca = marca

    def set_modelo(self, modelo):
        self._modelo = modelo

    def set_anio(self, anio):
        self._anio = anio

    def set_color(self, color):
        self._color = color

    def mostrar(self):
        print(f"Marca: {self._marca}, Modelo: {self._modelo}, Año: {self._anio}, Color: {self._color}")

# Lista fija de automóviles (estructura estática)
automoviles = [
    Automovil("Toyota", "Corolla", 2020, "Rojo"),
    Automovil("Honda", "Civic", 2019, "Negro"),
    Automovil("Ford", "Fiesta", 2018, "Blanco"),
    Automovil("Chevrolet", "Onix", 2021, "Azul"),
    Automovil("Nissan", "Sentra", 2022, "Gris")
]

for auto in automoviles:
    auto.mostrar()

# Ejemplo de uso de setters
automoviles[0].set_modelo("Yaris")
automoviles[1].set_color("Blanco")

print("\nDespués de modificar:")
for auto in automoviles:
    print(f"Marca: {auto.get_marca()}, Modelo: {auto.get_modelo()}, Año:")