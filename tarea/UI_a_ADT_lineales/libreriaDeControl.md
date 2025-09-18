def procesar_suma_lista(input_texto):
    lista = [int(x) for x in input_texto.split(",")]
    suma, pasos = suma_lineal(lista)
    return suma, pasos

def procesar_union_conjuntos(lista1, lista2):
    c1 = Conjunto(lista1)
    c2 = Conjunto(lista2)
    resultado = c1.union(c2)
    return str(resultado)
