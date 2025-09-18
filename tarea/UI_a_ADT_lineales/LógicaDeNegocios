## a) Conjuntos
class Conjunto:
    def __init__(self, elementos=None):
        self.elementos = set(elementos) if elementos else set()

    def union(self, otro):
        return Conjunto(self.elementos | otro.elementos)

    def interseccion(self, otro):
        return Conjunto(self.elementos & otro.elementos)

    def __str__(self):
        return str(self.elementos)
## b) Polinomios    
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
## c) Algoritmos Lineales (Ejemplo suma de lista)    
def suma_lineal(lista):
    suma = 0
    pasos = []
    for i, numero in enumerate(lista):
        suma += numero
        pasos.append((i+1, numero, suma))
    return suma, pasos

## Librerías de Control

def procesar_suma_lista(input_texto):
    lista = [int(x) for x in input_texto.split(",")]
    suma, pasos = suma_lineal(lista)
    return suma, pasos

def procesar_union_conjuntos(lista1, lista2):
    c1 = Conjunto(lista1)
    c2 = Conjunto(lista2)
    resultado = c1.union(c2)
    return str(resultado)
## a) Web con Streamlit (Python)
import streamlit as st

st.title("Algoritmos Lineales y Estructuras Matemáticas")

# Suma de lista
entrada = st.text_input("Ingresa una lista de números separados por coma:")
if entrada:
    suma, pasos = procesar_suma_lista(entrada)
    st.write("Paso a paso:")
    for i, numero, total in pasos:
        st.write(f"Iteración {i}: sumar {numero} → suma = {total}")
    st.success(f"Suma final: {suma}")

# Conjuntos
c1 = st.text_input("Ingresa elementos del Conjunto 1 separados por coma:")
c2 = st.text_input("Ingresa elementos del Conjunto 2 separados por coma:")
if c1 and c2:
    union = procesar_union_conjuntos([int(x) for x in c1.split(",")], [int(x) for x in c2.split(",")])
    st.success(f"Unión de conjuntos: {union}")
