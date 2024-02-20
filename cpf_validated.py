from os import system

CPF = "198.384.117-01"
cpf_calculate = CPF.split("-")[0].replace(".","") #salva somente os 9 primeiros dígitos somente numero

system("clear")

while True:
    sum_values = 0
    multiplication_value = 0

    if len(cpf_calculate) == 9: #se tiver 9 números, multiplica cada um por por números crescentes a partir do número 2 até o número 10
        multiplication_value = 10
    elif len(cpf_calculate) == 10: #se tiver 9 números, multiplica cada um por por números crescentes a partir do número 2 até o número 11
        multiplication_value = 11
    else: #passou disso, finaliza o programa
        break

    for digit in cpf_calculate:
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
    cpf_calculate = cpf_calculate + str(digit_cpf_end) 

#Formata o cpf no padrão xxx.xxx.xxx-xx
cpf_formatado = f"{cpf_calculate[:3]}.{cpf_calculate[3:6]}.{cpf_calculate[6:9]}-{cpf_calculate[9:]}"

if cpf_formatado == CPF:
    print(f"O seu CPF {cpf_formatado} é válido")
else:
    print(f"O seu CPF '{CPF}' não é válido")
    print(f"Um CPF válido seria '{cpf_formatado}'")
