#
# Versão do Python: 3.6.5
#
# Trabalho LINGUAGENS FORMAIS E AUTOMATOS
#
# Grupo:
# 00230091 - Rodrigo Rech
# 00229724 - Flávio Keglevich
# 00217052 - Txai Wieser
#

import FileManager

terminals = set()
variables = set()
initial = set()
rules = set()

def showMenu():
    print("Leitor de Grámatica, escolha uma opção para exibir:\n")
    print("1 - Terminais")
    print("2 - Variaveis")
    print("3 - Simbolo Inicial")
    print("4 - Regras de Producao")
    print("5 - Tudo")
    print("X - Sair")

    option = input("-> ")
    option = str(option)
    print("\n")

    if option == "1": 
        print("Terminais: ")
        printList(terminals)

    elif option == "2": 
        print("Variaveis:")
        printList(variables)

    elif option == "3":
        print("Simbolo Inicial:")
        print("".join(initial))

    elif option == "4":
        print("Regras:")
        print("\n".join(map(lambda x: x[0] + " -> " + " | ".join(x[1]), rules)))

    elif option == "5":
        printGrammar()

    else:
        return -1

    input("\nPressione uma tecla para continuar.")
    return showMenu()

def printList(list):
    string = ', '.join(list)
    print(string)

def printGrammar():
    print("Terminais: ")
    printList(terminals)
    print("\nVariaveis:")
    printList(variables)
    print("\nSimbolo Inicial:")
    print("".join(initial))
    print("\nRegras:")
    print("\n".join(map(lambda x: x[0] + " -> " + " | ".join(x[1]), rules)))

def start():
    fileName = FileManager.askForFileName()
    fullFile = FileManager.readFileWith(fileName)
    FileManager.extractGrammar(fullFile, terminals, variables, initial, rules)
