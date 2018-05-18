import FileManager
import RemoveEmptyProductions
import RemoveUselessSymbols
import ProductionsSubstituteVariables
import GrammarReader


def firstStep(terminals, variables, initial, rules):
    G1 = RemoveEmptyProductions.removeEmptyProductions(terminals, variables, initial, rules)
    G2 = RemoveUselessSymbols.removeUselessSymbols(G1[0], G1[1], G1[2], G1[3])
    return ProductionsSubstituteVariables.generate(G2[0], G2[1], G2[2], G2[3])


def substitute(newValue, oldValue, list):
    for idx, item in enumerate(list):
        if oldValue in item:
            list[idx] = newValue
    return list


def secondStep(terminals, variables, initial, rules):
    newVariables = list(variables)
    newRules = list(rules)

    for idx, rule in enumerate(newRules):
        if len(rule[1]) >= 2:
            for symbol in rule[1]:
                if symbol in terminals:
                    newSymbol = 'C' + symbol
                    newVariables.append(newSymbol)
                    newRules.append((newSymbol, tuple(symbol)))
                    ruleList = [rule[0], tuple(substitute(newSymbol, symbol, list(rule[1])))]
                    newRules[idx] = tuple(ruleList)



    return terminals, set(newVariables), initial, set(newRules)


def thirdStep(terminals, variables, initial, rules):
    newVariables = variables
    newRules = rules

    return terminals, newVariables, initial, newRules


def generate(terminals, variables, initial, rules):
    G1 = firstStep(terminals, variables, initial, rules)
    G2 = secondStep(G1[0], G1[1], G1[2], G1[3])
    G3 = thirdStep(G2[0], G2[1], G2[2], G2[3])
    GrammarReader.printGrammar(G3[0], G3[1], G3[2], G3[3])


terminals = set()
variables = set()
initial = set()
rules = set()

fullFile = FileManager.readFileWith('./examples/gramatica_exemplo1.txt')
FileManager.extractGrammar(fullFile, terminals, variables, initial, rules)

generate(terminals, variables, initial, rules)