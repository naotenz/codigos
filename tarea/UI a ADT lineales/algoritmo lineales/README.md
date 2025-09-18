# Algoritmo Lineal

## Descripción
Un **algoritmo lineal** es aquel cuyo **tiempo de ejecución crece de manera proporcional al tamaño de la entrada**.  
Si la entrada tiene `n` elementos, el algoritmo realiza aproximadamente `n` operaciones.  

Se caracteriza por su **eficiencia y simplicidad**, y suele expresarse como **O(n)** en notación Big O.

---

## Ejemplo

Supongamos que queremos **sumar todos los elementos de una lista**:

```python
def suma_lineal(lista):
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma

# Uso
numeros = [1, 2, 3, 4, 5]
print(suma_lineal(numeros))  # Salida: 15
