from os import system
system("clear")

#Closure e funcoes que chamam outras funcoes
"""
Um closure ocorre quando uma função interna lembra o estado de seu ambiente 
quando foi criada, mesmo depois de o escopo externo ter sido encerrado. 
O exemplo ilustra um closure: as funções internal_multiplier 
lembram o valor de multiplicador mesmo após a conclusão da execução de 
multiplication_calculator.
"""

def multiplication_calculator(value_for_mult):
    def internal_multiplier(number):
        return number * value_for_mult
    return internal_multiplier #sem "()"

duplicate = multiplication_calculator(2)
tiple = multiplication_calculator(3)
quadruple = multiplication_calculator(4)

print("Digite um número para duplicar, triplicar q quadruplicar ele: ")
number = input(": ")

try:
    number = int(number)
    system("clear")
    
    print(duplicate(number))
    print(tiple(number))
    print(quadruple(number))
except ValueError as err:
    print(err)