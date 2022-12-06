"""
while/else
"""
string = "ValorQualquer"

i = 0
while i < len(string):
    letra = string[i]

    if letra == " ":
        break

    print(letra)
    i += 1
else:
    print("Executa somente quando While faz o loop completo")
print("Fora do while")