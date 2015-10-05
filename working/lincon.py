# IPython script for the solution of the linear convection equation using
# finite differences.

import numpy  
import math                     
from matplotlib import pyplot    
from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16

def linearconv(nx,tt):
    """Solve the linear convection equation.
    
    Solves the equation d_t u + c d_x u = 0 where 
    * the wavespeed c is set to 1
    * the domain is x \in [0, 2]
    * The total time step is givem and the number of steps is adjusted 
      accordingly to the  \Delta t computed using the CFL 0.5
    * the initial data is the hat function
    
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
    dx = 2/(nx-1)
    c = 1
    sigma = 0.5 # sigma <=1.0, quanto mais pr�ximo do maximo 1.0, observei 
                # menor dissipacao numerica. Menor numero de iteracoes?
    x = numpy.linspace(0,2,nx)
    
    dt = sigma*dx/c
    nt = int(math.floor(tt/dt)) # Calcula o numero de passos para dar o mesmo 
                                # tempo total
    print(nt)

    u = numpy.ones(nx) 
    lbound = numpy.where(x >= 0.5)
    ubound = numpy.where(x <= 1)
    u[numpy.intersect1d(lbound, ubound)]=2 

    un = numpy.ones(nx)

    for n in range(nt):  
        un = u.copy() 
        u[1:] = un[1:] -c*dt/dx*(un[1:] -un[0:-1]) 
        u[0] = 1.0    # C.C. Observe que so e' necessaria do lado esquerdo.
        
    pyplot.plot(x, u, color='#003366', ls='--', lw=3)
    pyplot.ylim(0,2.5)
    pyplot.show()

# Teste
linearconv(101,0.5)


