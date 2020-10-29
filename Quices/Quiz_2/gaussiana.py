import numpy as np
import matplotlib.pyplot as plt
# cuadratura de Gauss de dos puntos
def integraCuadGauss2p(funcionx,a,b):
    x0 = -1/np.sqrt(3)
    x1 = -x0
    xa = (b+a)/2 + (b-a)/2*(x0)
    xb = (b+a)/2 + (b-a)/2*(x1)
    area = ((b-a)/2)*(funcionx(xa) + funcionx(xb))
    return(area)
# INGRESO
fx = lambda x: x * np.exp(x)
# intervalo de integración
a = 1
b = 2
tramos = 10000
# PROCEDIMIENTO
muestras = tramos+1
xi = np.linspace(a,b,muestras)
area = 0
for i in range(tramos):
    deltaA = integraCuadGauss2p(fx,xi[i],xi[i+1])
    area = area + deltaA
# SALIDA
print('Integral: {:.32f}'.format(area))