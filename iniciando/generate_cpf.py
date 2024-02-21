import random #modulo que chama valores aleatorios
from os import system

nine_digits_for_cpf_generate = ""
for digit in range(9):
    nine_digits_for_cpf_generate += str(random.randint(0,9)) #gera números int aleatórios de 0 a 9

system("clear")
print(nine_digits_for_cpf_generate)

while True:
    sum_values = 0
    multiplication_value = 0

    if len(nine_digits_for_cpf_generate) == 9: #se tiver 9 números, multiplica cada um por por números crescentes a partir do número 2 até o número 10
        multiplication_value = 10
    elif len(nine_digits_for_cpf_generate) == 10: #se tiver 9 números, multiplica cada um por por números crescentes a partir do número 2 até o número 11
        multiplication_value = 11
    else: #passou disso, finaliza o programa
        break

    for digit in nine_digits_for_cpf_generate:
        sum_values += int(digit) * multiplication_value #Multiplica cada número da lista somando-os
        multiplication_value -= 1
    
    quotient_of_sum = sum_values%11 #Pega o quociente

    if quotient_of_sum < 2:
        # - Se o resto da divisão for menor que 2, então o dígito é igual a 0 (Zero).
        digit_cpf_end = 0
    elif quotient_of_sum >= 2:
        # - Se o resto da divisão for maior ou igual a 2, então o dígito verificador é igual a 11 menos o resto da divisão (11 - resto).
        digit_cpf_end = 11 - quotient_of_sum

    #Adciona o número descoberto ao CPF 
    nine_digits_for_cpf_generate = nine_digits_for_cpf_generate + str(digit_cpf_end) 

#Formata o cpf no padrão xxx.xxx.xxx-xx
cpf_formatado = f"{nine_digits_for_cpf_generate[:3]}.{nine_digits_for_cpf_generate[3:6]}.{nine_digits_for_cpf_generate[6:9]}-{nine_digits_for_cpf_generate[9:]}"

print(f"O CPF gerado foi {cpf_formatado}")