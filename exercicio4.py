from os import system

calculator_active = True
system("clear")

while calculator_active:
    print("Digite uma operação matemática: ")
    operation = input(": ")
    
    try:
        result_operation = eval(operation)
        print(result_operation)
        exit_calculator = input("Deseja sair da calculadora? ")[0].lower().replace("s","y").startswith("y")
        system("clear")
        if exit_calculator is True :
            print("Calculadora Encerrada")
            break
    except Exception as err:
        input(f"Digite uma operação válida, {err}")
        system("clear")