# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 15:58:46 2021

@author: izahterencio
"""

import math

a = float(input('Informe o valor de A, que acompanha o termo quadrático: '))
b = float(input('Informe o valor de B, que acompanha o termo linear: '))
c = float(input('Informe o valor de C, o termo independente: '))
print('\n')

if a == 0:
    print('Como A é IGUAL a zero, não há uma equação de segundo grau!!')
else:
    delta = math.pow(b, 2) - 4*a*c
    print('O valor de delta é {:.2f}'.format(delta))
    
    if delta<0:
        print('A equação não possui raízes reais!!')
    elif delta==0:
        r = ((-b) + math.sqrt(delta))/2*a
        print('A única raiz da equação é: {:.2f}'.format(r))
    else:
        r1 = ((-b) + math.sqrt(delta))/(2*a)
        r2 = ((-b) - math.sqrt(delta))/(2*a)
        print('A equação possui DUAS raízes distintas, que são: r1={:.2f} e r2={:.2f}'.format(r1,r2))