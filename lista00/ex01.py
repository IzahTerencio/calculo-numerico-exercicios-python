import math

a = float(input('Informe um valor para A: '))
b = float(input('Informe um valor para B: '))
c = float(input('Informe um valor para C: '))
print('\n')

n = ((a+b*c) - (math.sqrt(a*b*c)))/(2*c + b)
    
print('N = ', n)