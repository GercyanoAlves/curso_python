"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de indices inexistentes na lista
"""
import os
lista = []


while True:
    opcao = input("""
        Selecione uma opção!

        1 - Adicionar Item
        2 - Deletar Item
        3 - Listar Item
        4 - Sair
            Digite sua opção: """)

    if opcao == "1": # Adiciona itens
        adicionar = input("\nDigite um item para adicionar: ")
        lista.append(adicionar)
        os.system("clear")

    elif opcao == "2": # Deleta itens
        deletar = input("\nQual indice deseja deletar: ")
        # Evitar de aparecer algum erro
        try:
            os.system("clear")
            deletar_int = int(deletar)
            del lista[deletar_int]
        
        except IndexError:
            print("Indice inexistente")

        except ValueError:
            print("Digite somente números")
        
        # --------------------------------------------

            #listar itens
    elif opcao == "3": 
        os.system("clear")
        if len(lista) == 0:
            print("Lista vazia")
        for indice, item in enumerate(lista):
            print(indice, item)
    # ----------------------------------------------------


        # Encerra o programa e mostra a lista
    elif opcao == "4": 
        os.system("clear")
        print(f"Essa é sua lista: ")
        for i, j in enumerate(lista):
            print(i, j)
        break

        #----------------------------------------

        # Caso não digite o que for digitado        
    else:
        os.system("clear")
        print("Digite somente as opções pedidas.")

