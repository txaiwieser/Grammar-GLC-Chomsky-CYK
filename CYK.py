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

import Subword

def run(grammar, word):
    wordlen = len(word)

    # Palavra vazia deve ser rejeitada sempre porque gramáticas na FNC não aceitam a palavra vazia
    if wordlen == 0: return False

    # Passo 1: criar dicionário que relaciona o rabo (tail) das produções com a cabeça (head) delas
    inverted = createInvertedTable(grammar)

    # Passo 2: criar matriz triangular do tamanho da palavra
    matrix = createMatrix(word)

    # Passo 3: preencher a primeira fileira da matriz e verificar se ela é valida
    if not fillFirstRow(matrix, inverted, word):
        return False # erro, a palavra contém um terminal nada a ver; não é aceita

    # Passo 4: algoritmo principal
    if wordlen > 1:
        for row in range(1, wordlen):
            for col in range(0, wordlen - row):
                subword = (col, word[col:col + row + 1])
                divisions = Subword.listAllSubdivisions(subword)
                for slice in divisions:
                    leftSet = findSetOfSubword(matrix, slice[0])
                    rightSet = findSetOfSubword(matrix, slice[1])
                    product = pseudoCartesianProduct(leftSet, rightSet)
                    for tail in product:
                        if tail in inverted:
                            matrix[row][col] |= inverted[tail]

    printMatrix(matrix)

    # Passo 5: checar se a palavra foi aceita
    for initial in grammar[2]:
        return initial in matrix[wordlen - 1][0]

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


def findSetOfSubword(matrix, subword):
    return matrix[len(subword[1]) - 1][subword[0]]


def pseudoCartesianProduct(a, b):
    if len(a) == 0: return b
    if len(b) == 0: return a

    return set([(x, y) for x in a for y in b])