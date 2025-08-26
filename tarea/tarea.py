personas = [
    {"nombre": "Ana", "edad": 11},
    {"nombre": "Luis", "edad": 13},
    {"nombre": "María", "edad": 34},
    {"nombre": "Carlos", "edad": 55},
    {"nombre": "Sofía", "edad": 20}
]

total_recaudado = 0

for persona in personas:
    if persona["edad"] >= 18:
        print(f'{persona["nombre"]} es adulto y paga 10')
        total_recaudado += 10
    else:
        print(f'{persona["nombre"]} es niño y paga 5')
        total_recaudado += 5

print("Total recaudado:", total_recaudado)