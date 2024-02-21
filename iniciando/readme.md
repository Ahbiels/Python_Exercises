### Exercicio 1
Calcular o IMC de uma pessoa
- Tecnicas utilizadas:
  - lib os utilizando o método system para limpar a tela
  - Método **round** para para arredondar um valor com base em 2 casas decimais
    - Pode ser substituido por: ``` {IMC:.2f} ```

### Exercicio 2
Brincar com o nome e idade da pessoa
- Tecnicas utilizadas:
  - f-strings com:
    - invertendo o nome da pessoa
    - Vendo quantas letras o nome possui
    - Vendo a primeira e última letra do nome
    - Convertendo a idade para binário e para hexadecimal
      - Em binário usando o 2: para aparecer apenas os valores
    
### Exercicio 3
Brincando com alguns métodos.
- Tecnicas utilizadas
  - ***isdigit*** para verificar se o valor é um número
  - % para verificar se o valor é ímpar ou pâr
  - A lib datetime para extrair a hora do computador
  - fatiamento de string para poder pegar uma parte da hora
  - método ***system*** da lib ***os*** para limpar a tela

### Exercicio 4
Calculadora
- Tecnicas utilizadas
  - try e except
    - Usei o **Exception as err** dentro do except para poder ver a exceção criada
  - **eval** para poder realizar a operação matemática
  - Métodos de string
    - **lower**: converte tudo para minisculo
    - **reaplce**: troca um valor por outro
    - **startswith**: verifica se a string começa com uma letra e retorna True

### Exercicio 5
Contador da maior quantidade de letras em uma frase
- Tecnicas utilizadas
  - **count**: para contar a quantidade de letras que tem dentro de uma frase
  ```py
   if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual
  ```
  - Se a contagem atual de letra_atual (qtd_apareceu_mais_vezes_atual) for maior que qtd_apareceu_mais_vezes, o programa atualiza qtd_apareceu_mais_vezes com esse novo valor máximo e atualiza letra_apareceu_mais_vezes para letra_atual, pois agora essa é a letra que apareceu mais vezes até o momento.

### Exercicio 6
Jogo da forca
- Algorítmo para converter os traços em letras na tela

### Exercicio 7
Lista de compras
- Tecnicas utilizadas
  - try... except para pegar as exceções
    - Pegar cada exceção em um except
  - **capitalize_list = [item.capitalize() for item in list]** para colocar todos os itens da lista com a primeira letra maíuscula
  - **enumerate** para pegar os index de uma lista
  - Métodos de crud em uma lista (adcionar, visualizar e deletar)

### Exercicio 8
Validação de CPF
- Tecnicas utilizadas
  - **split e replace** para pegar os 9 primeiros números do cpf sem os pontos ('.')
  - Lógica matemática
  - Formatação com f-string para o padrão xxx.xxx.xxx-xx

### Exercicio 9
gerador de CPF
- Tecnicas utilizadas
  - Módulo de **random** para sortear números aleatórios
  
