"""
Cuidados com dados mutáveis
= - copiando o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ["Gercyano", "Ana Paula"]
lista_b = lista_a.copy()

lista_a[0] = "Qualquer valor"
print(lista_b)