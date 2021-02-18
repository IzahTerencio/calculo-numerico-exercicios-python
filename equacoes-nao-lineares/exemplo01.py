import numpy as np
import matplotlib.pyplot as plot

def f(x):
    return (x**3 - 9*x**2 + 22*x - 15)

intervalo = np.linspace(1, 6)
print(intervalo)
plot.plot(intervalo, f(intervalo))
plot.title('Gráfico 1')
plot.xlabel('eixo x')
plot.ylabel('eixo y')
plot.grid()
plot.show()