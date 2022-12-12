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
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b)
print(lista_d)