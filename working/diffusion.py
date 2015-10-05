# IPython script for the solution of the diffusion equation using
# finite differences.

import numpy  
import math                     
from matplotlib import pyplot    
from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16

def diffusion(nx,tt):
    """Solve the diffusion equation.
    
    Produces a plot of the results
    
    Parameters
    ----------
    
    nx : integer
        number of internal grid points
    tt : float
        total time interval of simulation
		
    Returns
    -------
    
    None : none
    """
    dx = 2./(nx-1)

    nu    = 0.3   # the value of diffusivity
    sigma = .2    # <= 0.5
    dt    = sigma*dx**2/nu 
    nt = int(math.floor(tt/dt)) # Calcula o numero de passos para dar o mesmo 
                                # tempo total
    print("dt = ", dt, ". ", nt, "time steps.")

    x = numpy.linspace(0,2,nx)
    ubound = numpy.where(x >= 0.5)
    lbound = numpy.where(x <= 1)
    u = numpy.ones(nx)      
    u[numpy.intersect1d(lbound, ubound)] = 2  
    un = numpy.ones(nx) # Observe que as c.c.s esstao implicitamente
                        # estabelecidas pois os valores da primeira
                        # posicao e da ultima posicao nao sao
                        # atualizados. Veja abaixo que o o array e'
                        # parametrizado em u[1:-1], ou seja, vai da
                        # segunda posicao 'a penultima. Com isso, os
                        # valores dos dois ultimos nos ficam em 1.0.

    for n in range(nt):  
        un = u.copy() 
        u[1:-1] = un[1:-1] + nu*dt/dx**2*(un[2:] -2*un[1:-1] +un[0:-2]) 
        
    pyplot.plot(x, u, color='#003366', ls='--', lw=3)
    pyplot.ylim(0,2.5);
    pyplot.show()

# Teste
diffusion(41,0.1)


