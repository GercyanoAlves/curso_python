"""
Desempacotamentos em chamada
de métodos e funções
"""
string = "ABCD"
lista = ["Gercyano", "Paula", "Valentina"]
tupla = "Python", "é", "fácil"
salas = [
    # 0             1
    ["Gercyano", "Paula", ], # 0
    # 0
    ["Valentina", ],  # 1
    # 0           1         2
    ["Sergio", "Fatima", "Kercia", ], # 2
]

# a, b, c = lista
# print(a, c)

# for nome in lista:
#     print(nome, end=" ")

# print("Gercyano", "Paula", "Valentina")
# print(*lista)
# print(*string)
# print(*tupla)
print(*salas, sep = "\n")