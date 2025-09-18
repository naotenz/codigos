def suma_elementos_animado(conjunto):
    suma = 0
    print("Conjunto:", conjunto)
    for i, elemento in enumerate(conjunto):
        print(f"Paso {i+1}: suma = {suma} + {elemento} = {suma + elemento}")
        suma += elemento
    print("Resultado final:", suma)

# Ejemplo
A = [3, 5, 7, 2]
suma_elementos_animado(A)
