from os import system
system("clear")

print("Digite a palavra secreta, sem que seu amigo veja")

word = input(": ").lower()
secret_word = "_"*len(word)
letter_in_word_secret = '' #letras acertadas dentro da palavra secreta
correct_letters = 0 #pontuacao cada vez que acertar
attempts = 0 #tentativas
err = 0 #erros

while True:
    system("clear")
    print(f"Tentativas: {attempts} \t erros: {err} \t Pontuação: {correct_letters}")
    print(secret_word)
    if "_" not in secret_word: #Sai do programa quando acaba as opcoes
        break
    letter = input("Digite uma letra: ") 
    attempts += 1 #Aumenta o número de jogadas tentadas

    if len(letter) > 1 or len(letter) == 0: #verifica se o usuário digitou somente uma letra
        system("clear")
        print("Digite somente ume letra")
        input("\nClique em ENTER para continuar")
    elif letter in word and letter not in letter_in_word_secret: #Verifica se a palavra secreta possui a letra digitada e essa letra já não foi digitada antes
        secret_word = "" #Zera a palavra secreta
        letter_in_word_secret += letter #salva todas as letras acertadas em uma única variável

        for secret_letter in word: #Intera a palavra digitada no começo
            if secret_letter in letter_in_word_secret: #Verifica se as letras da palavra existem nas letras já digitadas
                correct_letters += 1 #Aumenta os pontos com base nas letras acertadas
                secret_word += secret_letter #Se sim, salva as letras na palavra secreta
            else:
                secret_word += "_" #Se nao, salva apenas os traços _
    else:
        err += 1

print(f"Voce venceu o jogo com '{err}' erros, '{attempts}' tentativas e com {correct_letters} pontos")
            
