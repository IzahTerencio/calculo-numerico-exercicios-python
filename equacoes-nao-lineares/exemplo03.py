import numpy as np
import matplotlib.pyplot as plot

def f(x):
    return (x**3 - 9*x**2 + 22*x - 15)

def derivada(x):
    #print('3*{}**2 - 18*{} + 22'.format(x,x))
    return (3*x**2 - 18*x + 22)

intervalo = np.linspace(0.5, 1.5)
print(intervalo)

plot.plot(intervalo, f(intervalo))
#plot.plot(intervalo, derivada(intervalo))
plot.title('Gráfico 1')
plot.xlabel('eixo x')
plot.ylabel('eixo y')

plot.grid()
plot.show()

