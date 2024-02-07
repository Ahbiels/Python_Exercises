name = input("Digite o seu nome: ")
idade = input("Digite sua idade: ")

if name:
    print(f"Seu nome é {name}")
    print(f"Seu nome invertido é {name[::-1]}")
    if ' ' in name:
        print("Seu nome tem espaço")
    else:   
        print("Seu nome não tem espaço")
    print(f"Seu nome tem {len(name)} letras")
    print(f"A primeira letra do seu nome é {name[0]}")
    print(f"A última letra do seu nome é {name[len(name)-1]}")
    print(f"Sua idade em binário é igual a: {bin(int(idade))[2:]}")
    print(f"Sua idade em hexadecimal é igual a: {hex(int(idade))}")
else:
    print("Por favor, digite o seu nome")