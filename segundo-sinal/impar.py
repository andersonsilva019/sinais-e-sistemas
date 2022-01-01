from math  import *
from numpy import *
from pylab import *

# sinal x[n] = cos(n) + sin(n) + sin(n) * cos(n)
def x(n):
    return cos(n) + sin(n) + sin(n) * cos(n)
 
fig = figure(1)
fig.set_size_inches((8., 8.))

# Cria as funções a serem plotadas.
n = arange(-4., 5.)
xp = 0.5 * (x(n) + x(-n))
xi = 0.5 * (x(n) - x(-n))

# Plotando o sinal impar.
a =  fig.add_subplot(2, 1, 1)
a.stem(n, xi, "k-", "ko", "k-")
a.set_xlim([ -4., 4. ])
a.set_ylim([ -2, 2 ])
a.set_xlabel('n')
a.set_ylabel("$x_i[n]$ ", rotation="horizontal")
a.set_title("Sinal original $x[n] = \cos(n) + \sin(n) + \sin(n) \cdot \cos(n)$")
a.set_xticks(n)
savefig("funcao-decomposta-impar.png", bbox_inches='tight')