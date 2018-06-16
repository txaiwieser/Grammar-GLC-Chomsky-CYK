# coding=utf-8
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
import RemoveEmptyProductions
import ProductionsSubstituteVariables
import NormalFormOfChomsky
import CYK

terminals = set()
variables = set()
initial = set()
rules = set()


def showMenu():
    print("Leitor de Grámatica, escolha uma opção para exibir:\n")
    print("1  - Terminais")
    print("2  - Variaveis")
    print("3  - Simbolo Inicial")
    print("4  - Regras de Producao")
    print("5  - Imprimir toda a gramática")
    print("6  - Resultado da Remoção de Símbolos Inúteis")
    print("7  - Resultado da Remoção de Produções Vazias")
    print("8  - Resultado das Produções que Substituem Variáveis")
    print("9  - Resultado da Forma Normal de Chomsky")
    print("10 - Executar algoritmo de Cocke-Younger-Kasami")
    print("X  - Sair")

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

    elif option == "7":
        G2 = RemoveEmptyProductions.removeEmptyProductions(terminals, variables, initial, rules)
        printGrammar(G2[0], G2[1], G2[2], G2[3])

    elif option == "8":
        G2 = ProductionsSubstituteVariables.generate(terminals, variables, initial, rules)
        printGrammar(G2[0], G2[1], G2[2], G2[3])

    elif option == "9":
        print("Gramática simplificada:")
        GS = NormalFormOfChomsky.firstStep(terminals, variables, initial, rules)
        printGrammar(GS[0], GS[1], GS[2], GS[3])
        print("\nGramática na FNC:")
        G2 = NormalFormOfChomsky.generate(terminals, variables, initial, rules)
        printGrammar(G2[0], G2[1], G2[2], G2[3])

    elif option == "10":
        word = input("Palavra a ser verificada: ")
        if CYK.run((terminals, variables, initial, rules), word):
            print("Palavra aceita!")
        else:
            print("Palavra rejeitada!")

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
    print("\n".join(map(lambda x: x[0] + " -> " + "".join(x[1]), r)))


def showMenuFor(fileName):
    fullFile = FileManager.readFileWith('./examples/' + fileName)
    FileManager.extractGrammar(fullFile, terminals, variables, initial, rules)
    return showMenu()

def start():
    fileName = FileManager.askForFileName()
    fullFile = FileManager.readFileWith(fileName)
    FileManager.extractGrammar(fullFile, terminals, variables, initial, rules)
