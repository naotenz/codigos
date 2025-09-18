# model.py
class Polinomio:
    def __init__(self, coeficientes=None):
        # coeficientes[i] corresponde a x^i
        self.coef = coeficientes if coeficientes else []

    def __str__(self):
        terms = []
        for i, c in enumerate(self.coef):
            if c != 0:
                terms.append(f"{c}x^{i}" if i > 0 else str(c))
        return " + ".join(reversed(terms)) if terms else "0"

    def __add__(self, other):
        max_len = max(len(self.coef), len(other.coef))
        nuevo = [0] * max_len
        for i in range(max_len):
            a = self.coef[i] if i < len(self.coef) else 0
            b = other.coef[i] if i < len(other.coef) else 0
            nuevo[i] = a + b
        return Polinomio(nuevo)

    def evaluar(self, x):
        return sum(c * (x ** i) for i, c in enumerate(self.coef))
