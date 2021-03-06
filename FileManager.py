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

import re


def askForFileName():
    option = input("Informe o nome do arquivo a ser usado: ")
    return str(option)


def readFileWith(name):
    arq = open(name, 'r')
    return arq.readlines()


def findCharInsideBrackets(string):
    selection = re.search(r"\[ ([A-Za-z]+) \]", string)
    if selection is not None:
        return selection.group(1)
    else:
        return None


def findAndRemoveCharInsideBrackets(string):
    selection = re.search(r"\[ ([A-Za-z]+) \]", string)
    if selection is not None:
        return string[:selection.start()] + string[selection.end():]
    else:
        return None


def extractGrammar(fileString, terminals, variables, initial, rules):
    current = None
    for line in fileString:
        if line.startswith('#Terminais'):
            current = "terminals"
        elif line.startswith('#Variaveis'):
            current = "variables"
        elif line.startswith('#Inicial'):
            current = "initial"
        elif line.startswith('#Regras'):
            current = "rules"
        else:
            char = findCharInsideBrackets(line)

            if current == "terminals":
                terminals.add(char)
            elif current == "variables":
                variables.add(char)
            elif current == "initial":
                initial.add(char)
            elif current == "rules":
                char = findCharInsideBrackets(line)
                line = findAndRemoveCharInsideBrackets(line)
                var = char
                char = findCharInsideBrackets(line)
                line = findAndRemoveCharInsideBrackets(line)
                prods = []
                while char is not None:
                    prods.append(char)
                    char = findCharInsideBrackets(line)
                    line = findAndRemoveCharInsideBrackets(line)

                if len(prods) == 1 and prods[0] == "V":
                    prods = []

                rules.add((var, tuple(prods)))
            else:
                print("Unknown line type")
