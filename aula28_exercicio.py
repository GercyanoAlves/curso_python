"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuario para digitar sua idade
Se o nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Se nome contém (ou não) espaços
        Seu tem {n} letras
        A primeira Letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios"
"""
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ") 

if nome and idade:

    print(f'Olá {nome}, você tem {idade} anos!')
    print(f'Seu nome invertido é :{nome[::-1]}')

    if ' ' in nome:
        print("Se nome CONTÉM    espaços")
    else:
        print("Se nome contém NÃO espaços")
    print(f'Seu nome contem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}.')
    print(f'A última letra do seu nome é {nome[-1]}.')
else:
    print("Desculpe, você deixou campos vazios")


