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

# Plotando o sinal original
a =  fig.add_subplot(2, 1, 1)
a.stem(n, x(n), "k-", "ko", "k-")
a.set_xlim([ -4., 4. ])
a.set_ylim([ -3, 3 ])
xlabel('n')
ylabel('x[n]')
title('Sinal original x[n] = cos(n) + sin(n) + sin(n) * cos(n)')
a.set_xticks(n)
savefig("funcao-decomposta-original.png", bbox_inches='tight')