# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 14:23:19 2021

@author: izahterencio
"""

numero = int(input('Informe um número: '))
resto = numero%2

if resto == 0:
    print('O número {} é PAR!'.format(numero))
else:
    print('O nuúmero {} é ÍMPAR!'.format(numero))