#!/usr/bin/python

# dicionario en python para asociar clave valor
numbers = {
    'a': 50,
    'b': 24,
    'c': 5,
    'd': 1,
    'e': 2,
    'f': 8
}

ecu1 = (numbers['a'] + (numbers['b'] / numbers['c'])) / (numbers['d'] + (numbers['e'] / numbers['f']))
ecu2 = numbers['a'] - (numbers['b'] / (numbers['c'] - numbers['d']))
#Intercambiando valores
ecu1 += ecu2
ecu2 = ecu1 - ecu2
ecu1 = ecu1 - ecu2  

#Impresion de resultados junto a formula
print("(numbers['a'] + (numbers['b'] / numbers['c'])) / (numbers['d'] + (numbers['e'] / numbers['f'])) =  {} \nnumbers['a'] - (numbers['b'] / (numbers['c'] - numbers['d'])) = {}".format(ecu1, ecu2))
