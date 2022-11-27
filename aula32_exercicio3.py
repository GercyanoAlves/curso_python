"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos, escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

usuario = input("Digite seu nome: ")
qtd_caracter = len(usuario)


if qtd_caracter >=1:
    curto = qtd_caracter <= 4
    normal = qtd_caracter >= 5 and qtd_caracter <= 6
    grande = qtd_caracter > 6
    if curto:
        print(f"Seu nome é curto!")
    elif normal:
        print("Seu nome é normal!")
    elif grande:
        print("Seu nome é muito grande!")
else:
    print("Por gentileza, o nome não pode ficar em branco")