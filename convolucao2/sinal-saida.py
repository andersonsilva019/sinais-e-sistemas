# Importa as bibliotecas necessárias
from numpy import *
from pylab import *
 
################################################################################
# Impulso unitário
def delta(n):
    return where(n==0, 1, 0)
# sinal x[n]
def x(n):
    return delta(n + 1) + 2*delta(n) + delta(n - 1)

# sinal h[n]
def h(n):
    return delta(n + 3) + delta(n + 2) + delta(n + 1) + 2*delta(n) + delta(n - 1) + delta(n - 2) + delta(n - 3)
 
################################################################################
n = arange(-4, 6, 1)
y = h(n + 1) + 2*h(n) + h(n - 1)
################################################################################
# Plotando o gráfico
fig = figure(1)
fig.set_size_inches((10., 8.))
 
a = fig.add_subplot(3, 2, 3)
a.stem(n, y, "k-", "ko", "k-")
a.set_xlim([ -2, 6 ])
a.set_ylim([ 0, 6.5 ])
a.set_title("$Sinal y[n] = x[n] * h[n]$")
a.set_ylabel("$y[n]$", rotation="horizontal")
a.set_xlabel('n')
a.set_xticks(arange(-5, 6, 1))
a.set_xticklabels(arange(-5, 6, 1))

savefig("conv-out-2.png", bbox_inches='tight')