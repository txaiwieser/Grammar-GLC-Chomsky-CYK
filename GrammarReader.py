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
import RemoveUselessSymbols

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
    print("6 - Resultado da Remoção de Símbolos Inúteis")
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
        printGrammar(terminals, variables, initial, rules)

    elif option == "6":
        G2 = RemoveUselessSymbols.removeUselessSymbols(terminals, variables, initial, rules)
        printGrammar(G2[0], G2[1], G2[2], G2[3])

    else:
        return -1

    input("\nPressione uma tecla para continuar.")
    return showMenu()

def printList(list):
    string = ', '.join(list)
    print(string)

def printGrammar(t, v, i, r):
    print("Terminais: ")
    printList(t)
    print("\nVariaveis:")
    printList(v)
    print("\nSimbolo Inicial:")
    print("".join(i))
    print("\nRegras:")
    print("\n".join(map(lambda x: x[0] + " -> " + " | ".join(x[1]), r)))

def start():
    fileName = FileManager.askForFileName()
    fullFile = FileManager.readFileWith(fileName)
    FileManager.extractGrammar(fullFile, terminals, variables, initial, rules)
