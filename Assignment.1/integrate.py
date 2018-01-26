import functions as f
import numpy as np

def sym_gauss_int_sqr(xb, n=10):
    y=np.linspace(-xb,xb,n)
    trapezoids = 0
    for i in y:
        trapezoids +=((1/n)*((f.gauss(i, c=np.sqrt(0.5))+f.gauss(i-1, c=np.sqrt(0.5)))/2))
    return (np.square(trapezoids))
