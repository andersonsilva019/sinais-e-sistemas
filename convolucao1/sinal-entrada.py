# Importa as bibliotecas necessárias
from numpy import *
from pylab import *
 
################################################################################
# Impulso unitário
def delta(n):
    return where(n==0, 1, 0)

# sinal x[n]
def x(n):
    return delta(n) + delta(n - 1) + delta(n - 2) + delta(n - 3)

# sinal h[n]
def h(n):
    return 2*delta(n) + 2*delta(n - 1) + 2*delta(n - 2) + 2*delta(n - 3)
 
################################################################################
n = arange(-1, 7, 1)
y = h(n) + h(n - 1) + h(n - 2) + h(n - 3)
################################################################################
# Plotando o gráfico
fig = figure(1)
fig.set_size_inches((10., 8.))
 
a = fig.add_subplot(3, 2, 1)
a.stem(n, x(n), "k-", "ko", "k-")
a.set_xlim([ -2, 6 ])
a.set_ylim([ 0, 1.5 ])
a.set_title('Sinal de entrada x[n]')
a.set_ylabel("$x[n]$", rotation="horizontal")
a.set_xticks(n)
a.set_xlabel('n')
a.set_xticklabels(n)

savefig("conv-in-1.png", bbox_inches='tight')