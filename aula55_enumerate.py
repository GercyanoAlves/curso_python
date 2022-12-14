"""
Enumerate - enumera iteráveis (índices)
"""
lista = ["Gercyano", "Paula", "Valentina"]
lista.append("Anny")

# Um for com duas variaveis, é o mesmo que um FOR dentro de outro FOR.
for indice, nome in enumerate(lista):
    print(indice, nome)

# --------------------------------------------------------------------

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)

# for tupla_enumerada in enumerate(lista):
#     print("FOR da tupla: ")
#     for valor in tupla_enumerada:
#         print(f"\t{valor}")