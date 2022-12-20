"""
Lista de listas e seus indices
"""
salas = [
    # 0             1
    ["Gercyano", "Paula", ], # 0
    # 0
    ["Valentina", ],  # 1
    # 0           1         2
    ["Sergio", "Fatima", "Kercia", ], # 2
]

# print(salas[0][1])
# print(salas[2][3][3])

for sala in salas:
    for aluno in  sala:
        print(aluno)