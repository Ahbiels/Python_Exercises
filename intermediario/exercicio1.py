from os import system

system("clear")

def mult(*args):
    total = 1
    for item in args:
        total *= item #Multiplica todos os itens da tupla

    def impar_par(value): #Funcao que diz se o número é ímpar ou par
        if value%2 == 0:
            return True
        return False
    definition_value = "Par" if impar_par(total) else "Impar"
    return f"A multiplicação desse número é igual a {total}," \
        f" que é um número {definition_value}"

# value = 3,4,7,2
try:
    value = tuple(input("Digite uma sequência de números: "))
    new_value = []
    for item in value:
        if item == ",": #As vírgulas irão causar um erro na hora de fazer a multiplicacao
            continue
        new_value.append(int(item)) #Salva cada item da tupla em uma lista, menos as vírgulas
    result = mult(*tuple(new_value)) #Manda os valores da lista em forma de tupla
    print(result) #Mostra o resultado da multiplicacao
except ValueError as err:
    print("Digite somente números")
    print(err)
