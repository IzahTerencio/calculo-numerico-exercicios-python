# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 17:10:41 2021

@author: izahterencio
"""

from itertools import permutations

def main():
    a = int(input('Informe a quantidade de elementos do conjunto A: '))
    lista_conjuto = []
    j = 0
    
    while (j<a):
        lista_conjuto.insert(j, j+1)
        j += 1
      
    print('O conjuto A possui os seguintes elementos:')
    print(lista_conjuto)
    
    nlista = permutations(lista_conjuto, 3)
    
    print('As combinações dos elementos do conjuto A são:')
    for c in list(nlista):
        print(c)
    
if __name__ == '__main__':
    main()