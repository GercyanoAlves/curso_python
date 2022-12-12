"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimento reutilizáveis - índices e fatiamento
Método úteis: 
    append - Adiciona um item ao final da lista
    insert - Adiciona um item no indice escolhido
    pop - Remove do final ou do indice escolhido
    del - apaga um indice
    clear - Limpa a lista
    extend - Estende a lista
    + - Cpncatena listas
Create Read Update  Delete
Criar, ler, alterar, apagar, = lista[i] (CRUD)
"""
lista = [10, 20, 30, 40]
lista.append("Gercyano")
nome = lista.pop()
lista.append(6)
del lista[-1]
# lista.clear()
lista.insert(100, "Gercyano")
print(lista[4])