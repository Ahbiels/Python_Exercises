from os import system

system("clear")
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opcoes': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opcoes': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opcoes': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
score = 0

def clean():
    input("Pressione ENTER para continuar")
    system("clear")

def response_validation(pergunta, *opcs):
    #usando o while para caso o usuádio nao digite um número válido de 1 a 4
    while True:
        try:
            print(f"{pergunta}\n")
            for index, item in enumerate(list(opcs[0])):
                #Mostra as opcoes enumeradas
                print(f"{index+1}) {item}")
            resposta = int(input("Resposta (opções de 1 a 4): "))
            if resposta < 1 or resposta > 4: 
                #Caso o usuário digite uma senha q n seja de 1 a 4 gera um erro
                raise ValueError("Choose an option between 1 to 4")
            break #quebra o while se o usuário digitar um valor válico
        except ValueError as err:
            print(err)
            clean()
            continue
    def validated(value):
        global score
        #Faz a validacao para saber se o usuário acertou
        resultado = int(opcs[0][resposta-1]) == int(value)
        if resultado:
            score += 1
            return True #Se acertou, retorna True
        return False #Se errou, retorna False
    return validated

for item in perguntas:
    resultado = response_validation(item["Pergunta"],item["Opcoes"])(item["Resposta"])
    print("Voce acertou" if resultado else "Voce Errou")
    item.update(Resultado=resultado)#Atualiza o dicionário dizendo se houve um acerto ou não
    clean()

# for resultado in perguntas:
#     if resultado["Resultado"] == True:
#         score += 1 #Calcula os score
#     else:
#         continue

print(f"Voce acertou {score}/{len(perguntas)}")