from Derivative import *

# przy wprowadzaniu funkcji pamiętać o dodawaniu nawiasów
customFunction = buildParseTree("( (  x ^ 2 ) + ( 2 * x ) )")
derivativeTree = derivative(customFunction, 'x')

# KONTROLNIE ZWRACA WARTOŚCI DRZEWA RÓŻNICZKI (ZALEŻNE OD FUNKCJI WPISANEJ dodać kolejne printy)
print(derivativeTree.getRootVal())
print(derivativeTree.getLeftChild().getRootVal())
print(derivativeTree.getRightChild().getRootVal())

