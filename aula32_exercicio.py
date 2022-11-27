"""
Faça um programa que peça ao usuário para digitar um numero inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número
inteiro, informe que não é um numero inteiro.
"""

num = input("Digite um número inteiro: ")

if num.isdigit():
    num_int = int(num)
    num_par = num_int % 2 == 0
    num_impar = num_int % 2 == 1
    if num_par:
        print(f"{num} é numero Par")
    elif num_impar:
        print(f"{num} é numero impar")
else:
    print("Por favor, nada de LETRAS!!!")
