nome = input('Digite seu nome: ')
idade = int(input('Qual a sua idade: '))
salario = float(input('Qual o seu salário: '))
sexo = input('Qual seu sexo F p/ feminino e M p/ masculino: ')

estado_civil = input('Qual seu estado civil (s,c,v,d)')

while len(nome) <= 3:
    nome = input('O nome tem que ter mais que 3 letras: ')

while (idade <= 0) or (idade >= 150):
    idade = int(input('Idade tem que está entre 0 e 150 anos: '))

while salario <= 0:
    salario = float(input('Salario tem que ser maior que 0: '))

while (sexo != 'm') and (sexo != 'f'):
    sexo = input('O sexo tem que ser f ou m : ')

while (estado_civil != 's') and (estado_civil != 'c') and (estado_civil != 'v') and (estado_civil != 'd'):
    estado_civil = input('O estado civil é CASADO (c), SOLTEIRO (s), VIÚVO (v), DIVORCIADO (d): ')
