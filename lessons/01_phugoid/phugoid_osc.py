import numpy 
from matplotlib import pyplot

def euler_step(u, f, dt):
    """Returns u_{n+1} of the Euler's method.
    
    Parameters
    ----------
    u : array of 
		problem variables.
	f: function of u
    dt : float
        time increment.
        
    Returns
    -------
    err : numpy array
		u_{n+1} of the Euler's method.
    """
    return u + dt * f(u)

# Tempo total e passo de tempo
T = 100.0
dt = 0.01

# Calcula o numero de valores discretos de tempo. Soma 1 ao numero de 
# intervalos para ter o ponto na extremidade do intervalo. 
# Observar comando 'int'
N = int(T/dt)+1

# Na propria documentacao nao se recomenda usar numpy.arange para intervalos
# de reais pois o final do intervalo e' aberto.
t = numpy.linspace(0.0, T, N)

# Initial conditions
z0 = 100.  #altitude
v  = 10   #upward velocity resulting from gust
zt = 100.
g  = 9.81

# Vetor de 2 posicoes para armazenar o estado na integracao temporal
u = numpy.array([z0, v])

# Equacao do problema
def f(u):
	return numpy.array([u[1], g*(1-u[0]/zt)])

# initialize an array to hold the changing vertical position values
z = numpy.zeros(N) # Vetor para armazenar resultados para gerar graficos
z[0] = z0  

# time-loop using Euler's method
for n in range(1,N):
	u = euler_step(u, f, dt)
	z[n] = u[0] #armazena posicao para gerar grafico

# Graficos
#------------------------------------------------------------------------------
# http://nbviewer.ipython.org/github/AJRenold/ipython/blob/1.x/examples/notebooks/Part%203%20-%20Plotting%20with%20Matplotlib.ipynb
#
# Comando para configurar a saida dos graficos. No caso de notebooks, essa e' 
# a forma mais conveniente pois direcionada a saida para dentro do proprio 
# notebook. Se estiver trabalhando dentro da linha de comando, usar sem '
# inline' pois a instalacao ja configurou a saida correta (janela externa).
#
# SO FUNCIONA INTERATIVAMENTE.
#
#%matplotlib #inline 
#------------------------------------------------------------------------------

pyplot.figure(figsize=(10,4))   #set plot size
pyplot.ylim(40,160)             #y-axis plot limits
pyplot.tick_params(axis='both', labelsize=14) #increase font size for ticks
pyplot.xlabel('t', fontsize=14) #x label
pyplot.ylabel('z', fontsize=14) #y label
pyplot.plot(t,z, 'k-'); # observar este ';'
pyplot.show()
