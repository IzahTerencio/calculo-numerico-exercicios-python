# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 09:40:35 2021

@author: izahterencio
"""

def main():
    num1 = int(input('Informe o primeiro número: '))
    num2 = int(input('Informe o segundo número: '))
    
    mdc_valor = mdc(num1,num2)
    mmc_valor = mmc(num1,num2,mdc_valor)
    
    print('O MMC dos números {} e {} é: {}'.format(num1,num2,mmc_valor))
    
#Função responsável por calcular o MDC entre dois números:
def mdc(num1,num2):
    div_comum = 1
    mdc = div_comum

    while (div_comum <=num1):
        if ((num1%div_comum == 0) and (num2%div_comum == 0)):
            mdc = div_comum
        
        div_comum = div_comum+1
    
    return mdc

#Função responsável por calcular o MMC entre dois números
def mmc(num1,num2,mdc):
    mmc = (num1*num2)/(mdc)
    return mmc

#Chamada da função principal
if __name__ == "__main__":
    main()