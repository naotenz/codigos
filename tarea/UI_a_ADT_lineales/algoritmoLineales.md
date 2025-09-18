def suma_lineal(lista):
    suma = 0
    pasos = []
    for i, numero in enumerate(lista):
        suma += numero
        pasos.append((i+1, numero, suma))
    return suma, pasos
