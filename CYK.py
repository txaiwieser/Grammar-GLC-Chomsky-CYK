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

import NormalFormOfChomsky
import Subword


def run(grammar, word):
    wordlen = len(word)

    # Palavra vazia deve ser rejeitada sempre porque gramáticas na FNC não aceitam a palavra vazia
    if wordlen == 0: return False

    # Passo 0: colocar a gramática na FNC
    grammar = NormalFormOfChomsky.generate(grammar[0], grammar[1], grammar[2], grammar[3])

    # Passo 1: criar dicionário que relaciona o rabo (tail) das produções com a cabeça (head) delas
    inverted = createInvertedTable(grammar)

    # Passo 2: criar matriz triangular do tamanho da palavra e a matriz auxiliar
    matrix = createMatrix(word)
    auxMatrix = createAuxMatrix(word)

    # Passo 3: preencher a primeira fileira da matriz e verificar se ela é valida
    # (e preencher a primeira fileira da matriz auxiliar tb)
    if not fillFirstRow(matrix, inverted, word):
        return False # erro, a palavra contém um terminal nada a ver; não é aceita

    fillFirstRowAuxMatrix(auxMatrix, matrix, word)

    # Passo 4: algoritmo principal
    if wordlen > 1:
        for row in range(1, wordlen):
            for col in range(0, wordlen - row):
                subword = (col, word[col:col + row + 1])
                divisions = Subword.listAllSubdivisions(subword)
                for slice in divisions:
                    leftSet = findSetOfSubword(matrix, slice[0])
                    rightSet = findSetOfSubword(matrix, slice[1])
                    product = cartesianProduct(leftSet, rightSet)
                    for tail in product:
                        if tail in inverted:
                            generators = inverted[tail]
                            matrix[row][col] |= generators

                            #coisas extras para preencher a matriz auxiliar
                            for variable in generators:
                                if variable in auxMatrix[row][col]:
                                    auxMatrix[row][col][variable] |= {slice, }
                                else:
                                    auxMatrix[row][col][variable] = {slice, }

    # Imprimindo as matrizes
    print("Matriz do algoritmo:")
    printMatrix(matrix)
    print("\nMatriz auxiliar:")
    printMatrix(auxMatrix)
    print("\n")

    # Passo 5: checar se a palavra foi aceita
    if isAccepted(word, grammar, matrix):

        # Passo 6: criar e imprimir as árvores de derivação
        generateParseTrees(word, matrix, auxMatrix, grammar, inverted)
        return True

    return False


def createInvertedTable(grammar):
    inverted = {}
    rules = grammar[3]
    for rule in rules:
        head = rule[0]
        tail = rule[1]
        if tail in inverted:
            inverted[tail].add(head)
        else:
            inverted[tail] = {head, }

    return inverted


def createMatrix(word):
    wordlen = len(word)
    return [[set() for col in range(wordlen - row)] for row in range(wordlen)]


def createAuxMatrix(word):
    wordlen = len(word)
    return [[{} for col in range(wordlen - row)] for row in range(wordlen)]


def printMatrix(matrix):
    for row in reversed(matrix):
        print(row)


def fillFirstRow(matrix, inverted, word):
    for i in range(len(word)):
        terminal = (word[i], )
        if terminal in inverted:
            matrix[0][i] |= inverted[terminal]
        else:
            return False

    return True


def fillFirstRowAuxMatrix(auxMatrix, matrix, word):
    for i in range(len(word)):
        varSet = matrix[0][i]
        for variable in varSet:
            auxMatrix[0][i][variable] = ((i, word[i]), (i+1, ""))


def findSetOfSubword(matrix, subword):
    return matrix[len(subword[1]) - 1][subword[0]]


def cartesianProduct(a, b):
    return set([(x, y) for x in a for y in b])


def getInitial(grammar):
    for initial in grammar[2]: return initial


def isAccepted(word, grammar, matrix):
    return getInitial(grammar) in matrix[len(word) - 1][0]


# parse tree node: (variable, slice)


def generateParseTrees(word, matrix, auxMatrix, grammar, inverted):
    stackList = []

    initial = getInitial(grammar)
    dictInitial = auxMatrix[len(word) - 1][0]

    # Existe um caso especial, especialíssimo, o dicionário auxiliar de S não conterá a chave S
    # (ao mesmo tempo que a palavra É ACEITA), esse caso é quando a palavra é um terminal.
    # Dessa forma, como a palavra-terminal é aceita, só precisamos imprimir S->a, onde a é a palavra-terminal
    # Esse caso especial não quebra o algoritmo pq generateParseTrees só é chamada quando a palavra é aceita
    if not (initial in dictInitial):
        print(initial + "->" + word)
        return

    initialSlices = dictInitial[initial]
    for slice in initialSlices:
        stackList.append(([(initial, slice, 0), ], []))

    print(stackList)
    print("\n")

    while len(stackList) > 0:
        stackAndStrList = stackList.pop()
        strList = stackAndStrList[1]
        processParseTree(stackAndStrList, matrix, auxMatrix, inverted, stackList)
        for str in strList:
            print(str, end='')

        print("\n", end='')


def getFirst(set):
    for item in set:
        return item


def processParseTree(stackAndStr, matrix, auxMatrix, inverted, stackList):
    stack = stackAndStr[0]
    strList = stackAndStr[1]
    while len(stack) > 0:
        node = stack.pop()

        variable = node[0]
        slice = node[1]
        ident = node[2]

        printIdent(ident, strList)

        strList.append(variable)

        if type(slice[0]) is int:
            strList.append("->" + slice[1] + "\n")
            continue

        leftSet = findSetOfSubword(matrix, slice[0])
        rightSet = findSetOfSubword(matrix, slice[1])
        product = cartesianProduct(leftSet, rightSet)
        isFirstIteration = True
        for tail in product:
            if tail in inverted:
                generators = inverted[tail]
                if variable in generators:

                    if isFirstIteration:
                        parseTreeLoop(auxMatrix, ident, slice, stack, strList, tail, stackList)
                        isFirstIteration = False
                    else:
                        strList2 = list(strList)
                        stack2 = list(stack)
                        parseTreeLoop(auxMatrix, ident, slice, stack2, strList2, tail, stackList)
                        stackList.append((stack2, strList2))


def parseTreeLoop(auxMatrix, ident, slice, stack, strList, tail, stackList):
    strList.append("->" + tail[0] + tail[1] + "\n")
    leftDict = findSetOfSubword(auxMatrix, slice[0])
    rightDict = findSetOfSubword(auxMatrix, slice[1])

    rightOptions = rightDict[tail[1]]
    leftOptions = leftDict[tail[0]]

    #print("options")
    #print("left: " + str(rightOptions))
    #print("right: " + str(leftOptions))

    #createEndlessPossibilities(ident, leftOptions, rightOptions, stack, strList, tail)

    choosenOne = (getFirst(leftOptions), getFirst(rightOptions))
    pushStack(choosenOne, ident, stack, tail)


def createEndlessPossibilities(ident, leftOptions, rightOptions, stack, strList, tail):
    options = cartesianProduct(leftOptions, rightOptions)
    isFirstIteration = True
    for option in options:
        if isFirstIteration:
            pushStack(option, ident, stack, tail)
            isFirstIteration = False
        else:
            strList2 = list(strList)
            stack2 = list(stack)
            # pushStack(option, ident, stack2, tail)
            # stackList.append((stack2, strList2))


def pushStack(choosenOne, ident, stack, tail):
    stack.append((tail[1], choosenOne[1], ident + 3))
    stack.append((tail[0], choosenOne[0], ident + 3))


def printIdent(ident, strList):
    for i in range(ident):
        strList.append(" ")