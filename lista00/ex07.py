# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 20:20:48 2021

@author: izahterencio
"""

import math

PERGUNTA = 'Informe um número: '
MENU = '1- SOMA \n2- MULTIPLICAÇÃO \n3- DIVISÃO \n4- SUBTRAÇÃO \n5- POTENCIAÇÃO \n6- SAIR \n'

print('--//BEM-VINDO(A)//-- \nQUAL OPERAÇÃO DESEJA? \n')
print(MENU)

resposta = int(input('Sua resposta: '))

while (resposta != 6):
    if (resposta == 1):
        s1 = float(input(PERGUNTA))
        s2 = float(input(PERGUNTA))
        soma = s1+s2
        print('{:.3f} + {:.3f} = {:.3f}'.format(s1,s2,soma))
    elif (resposta == 2):
        m1 = float(input(PERGUNTA))
        m2 = float(input(PERGUNTA))
        mult = m1*m2
        print('{:.3f} * {:.3f} = {:.3f}'.format(m1,m2,mult))
    elif (resposta == 3):
        d1 = float(input(PERGUNTA))
        d2 = float(input(PERGUNTA))
        div = d1/d2
        print('{:.3f} / {:.3f} = {:.3f}'.format(d1,d2,div))
    elif (resposta == 4):
        s1 = float(input(PERGUNTA))
        s2 = float(input(PERGUNTA))
        sub = s1-s2
        print('{:.3f} - {:.3f} = {:.3f}'.format(s1,s2,sub))
    else:
        base = float(input(PERGUNTA))
        expoente = float(input(PERGUNTA))
        pot = math.pow(base, expoente)
        print('{:.3f} ^ {:.3f} = {:.3f}'.format(base,expoente,pot))
    
    print('\nQUAL OPERAÇÃO DESEJA? \n',MENU)
    resposta = int(input('Sua resposta: '))