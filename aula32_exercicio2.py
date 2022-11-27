"""
Faça um programa que pergunte a hora_int ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa Tarde 12-17 e Boa noite 18-23.
"""
hora = input("Digite somente a hora: ")

if hora.isdigit():

    hora_int = int(hora)
    bomdia = hora_int > 0 and hora_int <= 11
    boa_tarde = hora_int >= 12 and hora_int <= 17
    boa_noite = hora_int >= 18 and hora_int <= 23
    hora_invalida = hora_int < 0 and hora_int > 24

    if bomdia:
        print("Bom dia!")
    elif boa_tarde:
        print("Boa tarde!")
    elif boa_noite:
        print("Boa noite!")
    else:
        print("Digite a hora entre 0 e 23")
else:
    print("Não digite LETRAS por favor!")