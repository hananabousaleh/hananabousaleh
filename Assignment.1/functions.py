import numpy as np

def gauss(x, a=1, b=0, c=1):
    """Gaussian function 
    
    parameters:
    x -- the variable to be manipulated (no default)
    a, b, c -- constants, can be adjusted. (defaults: a=c=1, b=0)
    
    """
    return (a*np.exp(-((x-b)**2)/(2*c**2)))