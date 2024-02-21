from os import system
from datetime import datetime

input("Pressione ENTER para continaur:")
system("clear")
num_int = input("Digite um número inteiro: ")

# Formas de virificar se um número é inteiro ou nao
# usando o valor.isdigit() que retorna se um valor é inteiro ou nao
# usando o type(valor) para identificar o tipo da variavel

if num_int.isdigit():
    num_int_validated = int(num_int)
    num_checked = num_int_validated%2 == 0
    if num_checked:
        print(f"O valor {num_int_validated} é um número par")
    else:
        print(f"O valor {num_int_validated} é um número ímpar")
else:
    print('Por favor, digite um número inteiro')

input("Pressione ENTER para continaur:")
system("clear")

name = input("Digite seu nome: ")
DATE = datetime.now()
hours = DATE.strftime("%H:%M:%S")

hour = hours[0:2]

if name:
    if hour >= 0 and hour < 12:
        print(f"Bom dia {name}")
    elif hour >= 12 and hour < 18:
        print(f"Boa tarde {name}")
    elif hour >= 18 and hour < 24:
        print(f"Boa noite {name}")
    else:
        print("Horário incorreto")

    input("Pressione ENTER para continaur:")
    system("clear")

    tamanho_name = len(name)
    if tamanho_name <= 4:
        print("Seu nome é muito curto")
    elif tamanho_name > 4 and tamanho_name <= 6:
        print("Seu nome tem um tamanho normal")
    elif tamanho_name > 6:
        print("Seu nome é muito grande")
else:
    print("Digite o seu nome da proxima vez")