from os import system

system("clear")

ordered_list = list(range(1,30))
attempt = 0
target = 9

def search_binary(ordered_list, attempt, target):
    list_search = ordered_list
    while True:
        index_search = len(list_search) // 2 #Salva somente uma metade, e busca novamente o meio da lista

        if list_search[index_search] == target:
            return f"A busca binária levou {attempt} temtativas para achar o alvo {target}"
        elif list_search[index_search] > target:
            list_search = list_search[:index_search] #Pega a primeira metade
        elif list_search[index_search] < target:
            list_search = list_search[index_search:] #Pega a segunda metade
        attempt += 1

print(
    search_binary(ordered_list, attempt, target)
)