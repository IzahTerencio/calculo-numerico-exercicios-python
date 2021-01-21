# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 14:06:38 2021

@author: izahterencio
"""

import math

raio = float(input('Informe o raio do círculo: '))

area = ((math.pow(raio, 2)) * math.pi)

print('A área do círculo de raio {} é {}.'.format(raio,area))