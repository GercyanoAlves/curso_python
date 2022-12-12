"""
for in com listas
"""
lista = ["Gercyano", "Ana Paula", "Valentina"]
lista.append("Maria")
indices = range(len(lista))


for i in indices:
    print(i, lista[i])