class Polinomio:
    def __init__(self, coeficientes):
        self.coeficientes = coeficientes

    def __add__(self, otro):
        longitud = max(len(self.coeficientes), len(otro.coeficientes))
        nuevo = [0] * longitud
        for i in range(longitud):
            a = self.coeficientes[i] if i < len(self.coeficientes) else 0
            b = otro.coeficientes[i] if i < len(otro.coeficientes) else 0
            nuevo[i] = a + b
        return Polinomio(nuevo)

    def __mul__(self, otro):
        nuevo = [0] * (len(self.coeficientes) + len(otro.coeficientes) - 1)
        for i, a in enumerate(self.coeficientes):
            for j, b in enumerate(otro.coeficientes):
                nuevo[i + j] += a * b
        return Polinomio(nuevo)

    def __str__(self):
        return " + ".join(f"{coef}x^{i}" for i, coef in enumerate(self.coeficientes) if coef != 0)
