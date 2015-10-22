import numpy  

def BFDResidual(nu, dx, u):
    """Computes the residual of the 1-D diffusion equation
    spatially discretized by backward finite differences.
    
    Computes (nu/dx^2)*(u_{i+1}-2*u_i+u_{i-1}) where

    Parameters
    ----------
    * c  : float
        [in] Diffusivity
    * dx : float
        [in] Spatial grid step
    * u  : array of floats
        [in] Array of state variables
		
    Returns
    -------    
    Res : array
        Array with the residual
    """
    return (nu/dx**2)*(u[2:] -2*u[1:-1] +u[:-2])


def DuBFDResidual(nu, dx, u):
    """Computes the Jacobian (residual derivative relative to state
    variables) of the 1-D diffusion equation spatially
    discretized by backward finite differences.
        
    Parameters
    ----------
    * nu  : float
        [in] Diffusivity
    * dx : float
        [in] Spatial grid step
    * u  : array of floats
        [in] Array of state variables
		
    Returns
    -------    
    DR : matrix
        [out] Matrix with the derivative of residual in the state variables
    """

    return (nu/dx**2)*( -2.*numpy.eye(len(u)) + numpy.eye(len(u), k=-1) + numpy.eye(len(u), k=1))
 
