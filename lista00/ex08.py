# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 09:11:22 2021

@author: izahterencio
"""
#Escreva um script em Python capaz de calcular o máximo divisor comum (MDC) de
#dois números.

print('---CÁLCULO DE MDC---')
num1 = int(input('Informe o peirmeiro número: '))
num2 = int(input('Informe o segundo número: '))

div_comum = 1
mdc = div_comum

while (div_comum <=num1):
    if ((num1%div_comum == 0) and (num2%div_comum == 0)):
        mdc = div_comum
        
    div_comum = div_comum+1
        
print('O maior divisor comum de {} e {} é: {}'.format(num1,num2,mdc))