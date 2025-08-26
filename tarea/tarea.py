personas = [
    {"nombre": "Ana", "edad": 17},
    {"nombre": "Luis", "edad": 22},
    {"nombre": "María", "edad": 15},
    {"nombre": "Carlos", "edad": 30},
    {"nombre": "Sofía", "edad": 18}
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