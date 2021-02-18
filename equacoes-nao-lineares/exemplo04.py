import numpy as np
import matplotlib.pyplot as pp

def eval_f(fx, x):
    print(eval(fx))
    return eval(fx)

def plot(fx, a, b):
    xx = np.linspace(a, b)
    pp.plot(xx, eval_f(fx, xx))
    pp.grid()
    pp.show()

func = input('Informe a função: ')
a = float(input('Informe o início do intervalo: '))
b = float(input('Informe o final do intervalo: '))
plot(func, a, b)