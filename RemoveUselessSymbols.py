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


def doesGenerateTerminalOrV1Element(rule, terminals, V1):
    for symbol in rule[1]:
        if not (symbol in terminals or symbol in V1):
            return False
    return True


def allVariablesAreInVx(rule, variables, Vx):
    if rule[0] not in Vx:
        return False

    for symbol in rule[1]:
        if symbol in variables and symbol not in Vx:
            return False

    return True


def allTerminalsAreInTx(rule, terminals, Tx):
    for symbol in rule[1]:
        if symbol in terminals and symbol not in Tx:
            return False

    return True

def firstStep(terminals, variables, initial, rules):
    V1 = set()
    P1 = set()

    while True:
        oldLenV1 = len(V1)
        for rule in rules:
            if doesGenerateTerminalOrV1Element(rule, terminals, V1):
                V1.add(rule[0])
        if not (len(V1) > oldLenV1):
            break

    for rule in rules:
        if allVariablesAreInVx(rule, variables, V1):
            P1.add(rule)

    return secondStep(terminals, V1, initial, P1)


def secondStep(terminals, variables, initial, rules):
    T2 = set()
    V2 = initial.copy()
    P2 = set()

    while True:
        oldLenT2 = len(T2)
        oldLenV2 = len(V2)

        for rule in rules:
            if rule[0] in V2:
                for symbol in rule[1]:
                    if symbol in variables:
                        V2.add(symbol)
                    elif symbol in terminals:
                        T2.add(symbol)

        if not (len(V2) > oldLenV2 and len(T2) > oldLenT2):
            break

    for rule in rules:
        if allVariablesAreInVx(rule, variables, V2):
            if allTerminalsAreInTx(rule, terminals, T2):
                P2.add(rule)

    return (T2, V2, initial, P2)

def removeUselessSymbols(terminals, variables, initial, rules):
    return firstStep(terminals, variables, initial, rules)