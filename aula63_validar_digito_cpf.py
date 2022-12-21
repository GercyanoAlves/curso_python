"""
Calculo do primeiro dígito do CPF
CPF: 219.075.720-74
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  219.075.720-74 (21907572074)
   10  9  8  7  6  5  4  3  2
*  2   1  9  0  7  5  7  2  0
   20  9 72  0 42 25 28  6  0
Somar todos os resultados: 
20+9+72+0+42+25+28+6+0 = 202
Multiplicar o resultado anterior por 10
301 * 10 = 2020
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""
cpf = input("Digite um CPF: ")

# Algoritimo para primeiro digito
nove_digitos = cpf[:9]
contador_regressivo = 10
resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo
    contador_regressivo -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

# Calculo para segundo digito, pega o resulta do for anterior e joga neste abaixoCurso Básico Pyhton, Lógica
contador_regressivo_2 = 0
dez_digitos = nove_digitos + str(digito_1)
resultado_digito_2 = 0
for digito_2 in dez_digitos:
    resultado_digito_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

calculo_cpf = f"{nove_digitos}{digito_1}{digito_2}"

if cpf == calculo_cpf:
    print(f"{cpf} é válido")
else:
    print(f"{cpf} é inválido")


