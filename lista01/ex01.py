# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 21:04:45 2021

@author: izahterencio
"""

import math

# Função principal
def main():
    numero = input('Informe um número: ')
    base_inicial = int(input('Informe a base na qual o número está: '))
    base_final = int(input('Informe para qual base o número será convertido: '))
    
    if (base_final == 10):
        numero_convertido = to_dec(numero, base_inicial)



        print('O número correspondente em decimal é: {:8f}'.format(numero_convertido))
    elif (base_inicial == 10):
        numero_decimal = float(numero)
        numero_convertido = dec_to_any(numero_decimal, base_final)
        print('O número correspondente na base {} é {}'.format(base_final, numero_convertido))
    else:
        numero_dec = to_dec(numero, base_inicial)
        numero_final = dec_to_any(numero_dec, base_final)
        print('O número {} convertido para a base {} é: {}'.format(numero, base_final, numero_final))
    
    
# Dado um número decimal e a base final para a qual ele deve ser convertido,
# realiza a devida conversão
def dec_to_any(n, b):
    parte_inteira = math.trunc(n)
    parte_fracionaria = n - parte_inteira
    
    # Trabalhando primeiro a parte inteira do número:
    resultado = parte_inteira // b
    resto = parte_inteira % b
    pt_inteira_covertida = ""
    while (resultado != 0):
        if (resto == 10):
            pt_inteira_covertida = pt_inteira_covertida + "A"
            resto = resultado % b
            resultado = resultado // b
        elif (resto == 11):
            pt_inteira_covertida = pt_inteira_covertida + "B"
            resto = resultado % b
            resultado = resultado // b
        elif (resto == 12):
            pt_inteira_covertida = pt_inteira_covertida + "C"
            resto = resultado % b
            resultado = resultado // b
        elif (resto == 13):
            pt_inteira_covertida = pt_inteira_covertida + "D"
            resto = resultado % b
            resultado = resultado // b
        elif (resto == 14):
            pt_inteira_covertida = pt_inteira_covertida + "E"
            resto = resultado % b
            resultado = resultado // b
        elif (resto == 15):
            pt_inteira_covertida = pt_inteira_covertida + "F"
            resto = resultado % b
            resultado = resultado // b
        else:
            pt_inteira_covertida = pt_inteira_covertida + str(resto)
            resto = resultado % b
            resultado = resultado // b
        
    if (resultado == 0):
        if (resto == 10):
            pt_inteira_covertida = pt_inteira_covertida + "A"
        elif (resto == 11):
            pt_inteira_covertida = pt_inteira_covertida + "B" 
        elif (resto == 12):
            pt_inteira_covertida = pt_inteira_covertida + "C"
        elif (resto == 13):
            pt_inteira_covertida = pt_inteira_covertida + "D"
        elif (resto == 14):
            pt_inteira_covertida = pt_inteira_covertida + "E"
        elif (resto == 15):
            pt_inteira_covertida = pt_inteira_covertida + "F"
        else:
            pt_inteira_covertida = pt_inteira_covertida + str(resto)
    #print(pt_inteira_covertida)
    
    produto = parte_fracionaria * b
    cont = 0
    aux = 0.0
    pt_fracionaria_convertida = ""
    parte_truncada = ""
    while ((produto!=0) and (cont<=8)):
        if (produto >= 1):
            parte_truncada = math.trunc(produto)
            
            if (parte_truncada == 10):
                pt_fracionaria_convertida = pt_fracionaria_convertida + "A"
                aux = math.trunc(produto)
                produto = (produto - aux)*b
                cont += 1
            elif (parte_truncada == 11):
                pt_fracionaria_convertida = pt_fracionaria_convertida + "B"
                aux = math.trunc(produto)
                produto = (produto - aux)*b
                cont += 1
            elif (parte_truncada == 12):
                pt_fracionaria_convertida = pt_fracionaria_convertida + "C"
                aux = math.trunc(produto)
                produto = (produto - aux)*b
                cont += 1
            elif (parte_truncada == 13):
                pt_fracionaria_convertida = pt_fracionaria_convertida + "D"
                aux = math.trunc(produto)
                produto = (produto - aux)*b
                cont += 1
            elif (parte_truncada == 14):
                pt_fracionaria_convertida = pt_fracionaria_convertida + "E"
                aux = math.trunc(produto)
                produto = (produto - aux)*b
                cont += 1
            elif (parte_truncada == 15):
                pt_fracionaria_convertida = pt_fracionaria_convertida + "F"
                aux = math.trunc(produto)
                produto = (produto - aux)*b
                cont += 1
            else:
                pt_fracionaria_convertida = pt_fracionaria_convertida + str(parte_truncada)
                aux = math.trunc(produto)
                produto = (produto - aux)*b
                cont += 1
        else:
            pt_fracionaria_convertida = pt_fracionaria_convertida + '0'
            aux = produto
            produto = aux * b
            cont += 1
    
    pt_inteira_ordenada = ""
    i = len(pt_inteira_covertida) - 1
    while (i >= 0):
        pt_inteira_ordenada = pt_inteira_ordenada + pt_inteira_covertida[i]
        i -= 1
        
    if (pt_fracionaria_convertida == ""):
        numero_final = pt_inteira_ordenada
    else:
        numero_final = pt_inteira_ordenada + "." + pt_fracionaria_convertida

    return(numero_final)

    
# Função responsável por separar a parte inteira do número de ponto flutuante
# da parte fracionária, alocando as respectivas partes em strings diferentes.
def separador(n, b):
    parte_inteira = ""
    parte_fracionaria = ""
    cont = 0
    cont2 = 0
    
    for letra in n:
        if (letra == '.'):
            break
        else:
            parte_inteira = parte_inteira + letra
            cont += 1
            
    for i in range((cont+1), len(n)):
        parte_fracionaria = parte_fracionaria + n[i]
        cont2 += 1
    
    # Bloco que define a parte inteira do número convertido 
    numero_convertido = 0.0
    indice = 0
    i = cont-1
    while(i >= 0):
        numero_convertido = numero_convertido + condicional_hexadec(n, indice, b, i)
        indice += 1
        i -= 1

    # bloco que define a parte fracionária do número convertido
    exp = -1
    for j in range((cont+1), len(n)):
        numero_convertido = numero_convertido + condicional_hexadec(n, j, b, exp)
        exp -= 1
    return(numero_convertido)
    
    
# Esta função contém uM conjunto de condições específicas para a conversão de
# números hexadecimais em número decimais, ocasionando reutilização de código
def condicional_hexadec(n, indice, b, i):
    numero_convertido = 0.0
    
    if (n[indice] == 'A'):
        numero_convertido = numero_convertido + (10*(b**(i)))
    elif (n[indice] == 'B'):
        numero_convertido = numero_convertido + (11*(b**(i)))
    elif (n[indice] == 'C'):
        numero_convertido = numero_convertido + (12*(b**(i)))
    elif (n[indice] == 'D'):
        numero_convertido = numero_convertido + (13*(b**(i)))
    elif (n[indice] == 'E'):
        numero_convertido = numero_convertido + (14*(b**(i)))
    elif (n[indice] == 'F'):
        numero_convertido = numero_convertido + (15*(b**(i)))
    else:
        numero_convertido = numero_convertido + ((int(n[indice]))*(b**(i)))
        
    return(numero_convertido)


# Função que converte um número de determinada base para seu correspondente
# em decimal    
def to_dec(n, b):
    if (b == 16):
        numero_convertido = separador(n, b)
        return(numero_convertido)
    else:
        numero_convertido = separador(n, b)   
        return(numero_convertido)
    
    
# Chamada à função principal
if __name__ == '__main__':
    main()