from os import system

list = []
listActive = True

while listActive:
    system("clear")
    print("\t\tSelecione uma opção:")
    print("1 - Listar itens")
    print("2 - Inserir itens")
    print("3 - Deletar itens")
    print("4 - Sair da lista")
    opc = input(": ")

    try:
        opc = int(opc)
    except ValueError:
        print("Digite um número válido")
        input("Pressione Enter para continuar")
        continue

    if opc == 1:
        system("clear")
        capitalize_list = [item.capitalize() for item in list] #Primeira letra maiuscula
        if len(list) > 0:
            for index, item in enumerate(capitalize_list, start=1):
                print(f"{index} - {item}")
            input("Pressione Enter para continuar")
        else:
            input("Lista vázia, pressione Enter para continuar")
    elif opc == 2:
        while True:
            system("clear")
            print(list)
            print("Digite o novo item para a lista de compra")
            print("Ou digite 'sair' para voltar ao Menu inicial")
            newItemForList = input(": ")
            if newItemForList.lower() == "sair":
                break
            else:
                list.append(newItemForList)
    elif opc == 3:
        system("clear")
        if len(list) > 0:
            for index, item in enumerate(list, start=1):
                print(f"{index} - {item}")
            try:
                deleteItemList = int(input("Digite o número do item que deseja remover: "))
                deleteItemList -= 1
                itemRemoved = list.pop(deleteItemList)
                input(f"Item {itemRemoved} deletado. Pressione Enter para continuar")
            except ValueError:
                system("clear")
                input("Digite um valor numerico")
                continue
            except IndexError:
                system("clear")
                input(f"Digite um valor entre 1 a {len(list)}")
                continue
        else:
            input("Lista vázia, pressione Enter para continuar")
    elif opc == 4:
        listActive = False
    else:
        continue
else:
    system("clear")
    print("Lista de compra finalizado")
