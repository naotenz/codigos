# Algoritmo de suma lineal
# Conjunto: [3, 5, 7, 2]
#
#  ┌────────────────────┐
#  │   Conjunto A =     │
#  │   [3, 5, 7, 2]     │
#  └─────────┬──────────┘
#            │
#            ▼
#  ┌────────────────────┐
#  │   Inicializar suma │
#  │   suma = 0         │
#  └─────────┬──────────┘
#            │
#            ▼
#  ...
#
# El código que implementa el algoritmo:
def suma_elementos(conjunto):
    suma = 0
    for elemento in conjunto:
        suma += elemento
    return suma

print(suma_elementos([3, 5, 7, 2]))
