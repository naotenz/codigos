from model import Polinomio

class Controller:
    def __init__(self, view):
        self.view = view

    def crear_polinomio(self, texto):
        # Ejemplo entrada: "3 0 2" → 3 + 0x + 2x²
        coef = list(map(int, texto.split()))
        return Polinomio(coef)

    def sumar(self, p1_texto, p2_texto):
        p1 = self.crear_polinomio(p1_texto)
        p2 = self.crear_polinomio(p2_texto)
        resultado = p1 + p2
        self.view.mostrar_resultado(f"Suma: {resultado}")

    def multiplicar(self, p1_texto, p2_texto):
        p1 = self.crear_polinomio(p1_texto)
        p2 = self.crear_polinomio(p2_texto)
        resultado = p1 * p2
        self.view.mostrar_resultado(f"Producto: {resultado}")

    def evaluar(self, p1_texto, x_valor):
        p1 = self.crear_polinomio(p1_texto)
        resultado = p1.evaluar(int(x_valor))
        self.view.mostrar_resultado(f"Evaluación: {resultado}")
