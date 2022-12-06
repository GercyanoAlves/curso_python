frase = "O Python é uma linguagem de programação "\
    "multiparadigma. "\
    "Python foi criado por Guido van Rossum."

i = 0
qtd_apareceu_mais_vezes = 0
letra_aparecei_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_letra_apareceu_atual = frase.count(letra_atual)

    if apareceu_mais_vezes < quantas_vezes_letra_apareceu_atual:
        apareceu_mais_vezes = quantas_vezes_letra_apareceu_atual
        letra_aparecei_mais_vezes = letra_atual

    i += 1

print("A letra que mais apareceu mais vezes foi "f"{letra_aparecei_mais_vezes} que apareceu {apareceu_mais_vezes}x")