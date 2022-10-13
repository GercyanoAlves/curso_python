"""
Funções - def ( parte 1)
"""
def saudacao(msg='Olá', nome='Gercyano'):
    nome = nome.replace('e', '3')
    msg = msg.replace('á','4')
    return f'{msg} {nome}'

variavel = saudacao()

print(variavel)
