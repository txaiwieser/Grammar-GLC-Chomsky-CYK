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
    option = input("Escolha uma opção: ")
    option = str(option)
    out = "0"

    if option == "1":
        GrammarReader.start()
        out = GrammarReader.showMenu()
    else:
        print("Exit")

    if out == "-1":
        showMenu()


showIntro()
showMenu()