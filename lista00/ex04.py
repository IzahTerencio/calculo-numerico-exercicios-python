# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 15:19:50 2021

@author: izahterencio
"""

def from_seconds(sec):
    minutos = sec//60
    sec = sec%60
    horas = minutos//60
    minutos = minutos%60
    
    print('{}h {}min {}sec'.format(horas,minutos,sec))
    
def from_hours(h,m,s):
    horas = h*60*60
    minutos = m*60
    tempo_total = horas + minutos + s
    
    print('{}h {}min {}s equivalem a {}s'.format(h,m,s,tempo_total))

if __name__ == '__main__':
    t_segundos = int(input('Informe o tempo desejado em SEGUNDOS: '))
    from_seconds(t_segundos)
    print('Agora informe horas, minutos e segundos, em ordem \n')
    thoras = int(input('Horas:'))
    tmins = int(input('Minutos:'))
    tsec = int(input('Segundos:'))
    from_hours(thoras, tmins, tsec)