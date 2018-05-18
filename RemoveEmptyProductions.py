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

def ruleHasOnlyElementsOfVE(rule, VE):
    for symbol in rule[1]:
        if symbol not in VE:
            return False

    return True


def firstStep(terminals, variables, initial, rules):
    VE = set()
    for rule in rules:
        if len(rule[1]) == 0:
            VE.add(rule[0])

    while True:
        oldLenVE = len(VE)

        for rule in rules:
            if ruleHasOnlyElementsOfVE(rule, VE):
                VE.add(rule[0])

        if not (len(VE) > oldLenVE):
            break

    return secondStep(VE, terminals, variables, initial, rules)


def addRemovedXRuleIfNeeded(rule, VE, P1):
    for symbol in rule[1]:
        if symbol in VE:
            asList = list(rule[1])
            asList.remove(symbol)
            asTuple = tuple(asList)
            newRule = (rule[0], asTuple)
            P1.add(newRule)
            break


def secondStep(VE, terminals, variables, initial, rules):
    P1 = set()
    for rule in rules:
        if len(rule[1]) != 0:
            P1.add(rule)


    while True:
        oldLenP1 = len(P1)

        P1new = set()

        for rule in P1:
            if (len(rule[1]) > 1):
                addRemovedXRuleIfNeeded(rule, VE, P1new)

        P1 |= P1new

        if not (len(P1) > oldLenP1):
            break

    return thirdStep(VE, terminals, variables, initial, P1)


def thirdStep(VE, terminals, variables, initial, rules):
    if (initial <= VE):
        for symbol in initial:
            rules.add((symbol, ()))
            break

    return (terminals, variables, initial, rules)


def removeEmptyProductions(terminals, variables, initial, rules):
    return firstStep(terminals, variables, initial, rules)