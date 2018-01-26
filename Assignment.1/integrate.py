import functions as f
import numpy as np

def sym_gauss_int_sqr(xb, n=10):
    y=linspace(-xb,xb,n)
    trapezoids = 0
    for i in y:
        trapezoids +=((1/n)*((f.gauss(i)+f.gauss(i-1))/2))
    return trapezoids**2
