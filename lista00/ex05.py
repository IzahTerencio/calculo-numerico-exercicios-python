# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 15:38:58 2021

@author: izahterencio
"""

#Crie um script em Python para determinar se um ano é ou não bissexto. Um ano
#N é bissexto seNé múltiplo de 400, ou então seNé múltiplo de quatro, mas não é
# múltiplo de 100. Por exemplo, 2012(múltiplo de 4, mas não múltiplo de 100) é
#bissexto, 1900 (múltiplo de quatro e de 100) não é bissexto,2000 (múltiplo de
#400) é bissexto).

n = int(input('Informe um ano: '))

if (n%400 == 0) or ((n%4 == 0) and (n%100 != 0)):
    print('O ano {} é BISSEXTO!'.format(n)) 
else:
    print('O ano {} NÃO É BISSEXTO!!'.format(n))