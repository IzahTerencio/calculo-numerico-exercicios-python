# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 13:50:32 2021

@author: izahterencio
"""

from itertools import combinations

def main():
    n = int(input('Informe o elemento final do conjunto A, considerando que este é formado pelos números naturais: '))
    lista_conjunto = []
    i = 0;
    
    #adiciona elementos dinamicamente à lista, de acordo com a entrada inicial do usuário
    while(i<n):
        lista_conjunto.insert(i, i+1)
        i += 1
    
    print('O conjunto A formado é: {}'.format(lista_conjunto))
    print('Os subconjuntos de A são:')
    print(list(combinations(lista_conjunto, 3)))
    
if __name__ == '__main__':
    main()