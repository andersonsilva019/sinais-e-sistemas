from math  import *
from numpy import *
from pylab import *

# sinal x[n] = 3*n + 5
def x(n):
    return 3*n + 5
 
fig = figure(1)
fig.set_size_inches((8., 8.))

# Cria as funções a serem plotadas.
n = arange(-4., 5.)
xp = 0.5 * (x(n) + x(-n))
xi = 0.5 * (x(n) - x(-n))

# Plotando o sinal x[n].
a =  fig.add_subplot(2, 1, 1)
a.stem(n, x(n), "k-", "ko", "k-")
a.set_xlim([ -4., 4. ])
a.set_ylim([ -10, 20 ])
a.set_xlabel('n')
a.set_ylabel("$x[n]$ ", rotation="horizontal")
a.set_title("Sinal original $x[n] = 3n + 5$")
a.set_xticks(n)
savefig("funcao-decomposta-original.png", bbox_inches='tight')