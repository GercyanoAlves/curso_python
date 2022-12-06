"""
Faça um jogo para o usuário advinhar qual a palavra secreta.
Você vai propor uma palavra secreta qualquer e vai dar a 
possibilidade para o usuário digitar apenas uma letra.
- Qual o usuário digitar uma letra, você vai conferir se a
letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta;
    exiba a letra;
    - Se a letra digitada não estiver na palavra secreta;
    exiba *.
Faça a contagem de tentativas do seu usuário.
"""
import os # exucuta algum comando no terminal no proprio python

palavra_secreta = 'crepusculo'
letra_digitadas = []
chance = 3

while True:

    # Quantidade de chances
    if chance <= 0:
        print('Vc perdeu!!')
        break

    letra = input('Digite uma letra :')
    #####################################

    # Condição para usar somente uma letra.
    if len(letra) > 1:
        print('\nAhh, isso não vale, digite apenas uma letra: ')
        continue
    # ---------------------------------------------------------------

    # caso haja letras irá apendar, caso não, o pop irá deletar a ultima letra
    letra_digitadas.append(letra)
    if letra in palavra_secreta:
        print(f'\nUHUULLL, a letra "{letra}" existe na palavra secreta')
    else:
        print(f'\nAFFzz: a letra "{letra}" não é na palavra secreta.')
        letra_digitadas.pop()
    # ---------------------------------------------------------------


    # Aqui caso haja letra correta irá adicionar a letra na palavra secreta temporaria
    # Caso não haja a letra, a letra será deletada como na condição acima e adicionada *
    palavra_secreta_temporaria = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_digitadas:
            palavra_secreta_temporaria += letra_secreta
        else:
            palavra_secreta_temporaria += '*'

    # -----------------------------------------------------------------------------------

    # Nessa condição, irá verificar se todas as letras e estão iguais, para assim encerrar o programa.
    if palavra_secreta_temporaria == palavra_secreta:
        os.system("clear") #comando para o terminal, nesse caso limpa tudo para trás.
        print(f'Que legal, VC GANHOU!! A palavra secreta é {palavra_secreta_temporaria}\n')
        break
    else:
        print(f'A palavra secreta está assim: {palavra_secreta_temporaria}')

    # Nessa condição, só executará quando a letra não estiver dentro da palavra secreta.
    if letra not in palavra_secreta: 
        chance += -1

    # ------------------------------------------------------------------------------------
    print(f'Vc ainda tem {chance} chances.\n')
