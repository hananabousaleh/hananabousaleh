import functions as f
import numpy as np

def sym_gauss_int_sqr(xb, n=10):
    """  
    This function calculates the area underneath the gaussian function (imported
    through functions.py) for constant c= sqrt(0.5) using the trapezoidal rule.
    
    Returns the area squared.
    paramters:
    xb -- the upper bound for the interval to be integrated over. Assumed the number 
            being passed through is positive. the negative of this variable will 
            be the lower bound of the interval
    n -- constant, represents the number of grid cells in direction x to be used
            in the numberical integration. optional argument, default is 10.
    
    """
    y=np.linspace(-xb,xb,n)
    trapezoids = 0
    for i in y:
        h1=f.gauss(i, c=np.sqrt(0.5))
        h2=f.gauss(i+1, c=np.sqrt(0.5))
        trapezoids +=(((xb)/(n-1))*((h1+h2)))
    return (trapezoids**2)
