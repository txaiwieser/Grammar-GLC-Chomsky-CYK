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

# Subword é uma tupla (index, str) que representa uma subpalavra
# da entrada do algoritmo de CYK.
# Onde:
#   index: índice onde começa a subpalavra
#   str:   string contendo a subpalavra, de fato


def create(string):
    return (0, string)


def sliceInTwo(subword, middle):
    left = (subword[0], subword[1][:middle])
    right = (subword[0] + middle, subword[1][middle:])
    return (left, right)


def listAllSubdivisions(subword):
    subwordLen = len(subword[1])
    if subwordLen < 2:
        raise ValueError("Essa operação não é válida para substrings > 2")

    list = []
    for i in range(1, subwordLen):
        list.append(sliceInTwo(subword, i))

    return list