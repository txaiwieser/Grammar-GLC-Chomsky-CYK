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

import GrammarReader


def grammarReader():
    GrammarReader.start()
    return GrammarReader.showMenu()


def grammarExampleOne():
    print('exemplo 1')
    return GrammarReader.showMenuFor('gramatica_exemplo1.txt')


def grammarExampleTwo():
    return GrammarReader.showMenuFor('gramatica_exemplo2.txt')


def grammarExampleThree():
    return GrammarReader.showMenuFor('gramatica_exemplo3.txt')


def grammarExampleFour():
    return GrammarReader.showMenuFor('gramatica_exemplo4.txt')


def grammarExampleFive():
    return GrammarReader.showMenuFor('gramatica_exemplo5.txt')


def showIntro():
    print(
        """
    	#########################################################################
    	##                                                                     ##
    	##                         Trabalho Prático                            ##
    	##                   Linguagens Formais e Autômatos                    ##
    	##                                                                     ##
    	#########################################################################
    	"""
    )


def showMenu():
    print("1 - Leitor da Gramática")
    print("2 - Ler Gramática Exemplo 1")
    print("3 - Ler Gramática Exemplo 2")
    print("4 - Ler Gramática Exemplo 3")
    print("5 - Ler Gramática Exemplo 4")
    print("6 - Ler Gramática Exemplo 5")

    option = input("Escolha uma opção: ")
    option = str(option)
    out = "0"

    if option == "1":
        out = grammarReader()
    elif option == "2":
        out = grammarExampleOne()
    elif option == "3":
        out = grammarExampleTwo()
    elif option == "4":
        out = grammarExampleThree()
    elif option == "5":
        out = grammarExampleFour()
    elif option == "6":
        out = grammarExampleFive()
    else:
        print("Exit")

    if out == "-1":
        showMenu()


showIntro()
showMenu()
