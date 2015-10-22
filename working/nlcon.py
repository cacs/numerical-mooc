import numpy  

def BFDResidual(dx, u):
    """Computes the residual of the 1-D nonlinear convection equation
    spatially discretized by backward finite differences.
    
    Computes -(u_i/dx)*(u_i-u_{i-1}) where

    Parameters
    ----------
    * dx : float
        [in] Spatial grid step
    * u  : array of floats
        [in] Array of state variables
		
    Returns
    -------    
    Res : array
        Array with the residual
    """
    return (-u[1:]/dx)*(u[1:] -u[:-1])


def DuBFDResidual(dx, u):
    """Computes the Jacobian (residual derivative relative to state
    variables) of the 1-D linear convection equation spatially
    discretized by backward finite differences.
    
    Computes -(c/dx)*d_u(u_i-u_{i-1}) where

    Parameters
    ----------
    * dx : float
        [in] Spatial grid step
    * u  : array of floats
        [in] Array of state variables
		
    Returns
    -------    
    DR : matrix
        [out] Matrix with the derivative of residual in the state variables
    """

    DR = numpy.zeros( (len(u), len(u)) )
    i  = numpy.arange( 1, len(u)-1 )
    DR[i, i] = 2*u[1:-1]-u[:-2]
    DR[i[1:],i[:-1]] = -u[2:-1]
    
    return (-1./dx)*DR
 
