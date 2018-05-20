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


def generateClosure(var, variables, rules, closure):
    for rule in rules:
        if var is rule[0]:
            if len(rule[1]) is 1 and rule[1][0] in variables:
                closure.add(rule[1][0])


def initializeNewRules(rules, variables):
    P1 = set()

    for rule in rules:
        if len(rule[1]) is 1:
            if rule[1][0] not in variables:
                P1.add(rule)
        else:
            P1.add(rule)
    return P1


def secondStep(variables, rules, closures):
    P1 = initializeNewRules(rules, variables)

    for var in variables:
        if closures[var]:
            for closure in closures[var]:
                for rule in rules:
                    if closure is rule[0]:
                        if len(rule[1]) is 1:
                            if rule[1][0] not in variables:
                                P1.add((var, rule[1]))
                        else:
                            P1.add((var, rule[1]))

    return P1


def firstStep(variables, rules):
    closures = {}
    for var in variables:
        closures[var] = set()
        generateClosure(var, variables, rules, closures[var])

    return secondStep(variables, rules, closures)


def generate(terminals, variables, initial, rules):
    return terminals, variables, initial, firstStep(variables, rules)