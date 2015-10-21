import numpy  

def BFDResidual(c, dx, u)
    """Computes the residual of the 1-D linear convection equation
    spatially discretized by backward finite differences.
    
    Computes -(c/dx)*(u_i-u_{i-1}) where

    Parameters
    ----------
    * c  : float
        [in] Wavespeed
    * dx : float
        [in] Spatial grid step
    * u  : array of floats
        [in] Array of state variables
		
    Returns
    -------    
    Res : array
        Array with the residual
    """
    return -c/dx*(u[1:] -u[:-1])


def DuBFDResidual(c, dx, u)
    """Computes the Jacobian (residual derivative relative to state
    variables) of the 1-D linear convection equation spatially
    discretized by backward finite differences.
    
    Computes -(c/dx)*d_u(u_i-u_{i-1}) where

    Parameters
    ----------
    * c  : float
        [in] Wavespeed
    * dx : float
        [in] Spatial grid step
    * u  : array of floats
        [in] Array of state variables
		
    Returns
    -------    
    DR : matrix
        [out] Matrix with the derivative of residual in the state variables
    """

    return -c/dx*( numpy.eye(len(u)) - numpy.eye(len(u), k=-1) )
 
