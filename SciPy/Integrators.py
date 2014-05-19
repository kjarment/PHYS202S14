
from numpy import *
import numpy as np

def trapz(func,a,b,N):
    """
    In this function, we use the trapezoidal method of integrating in order
    to find the integral. Trapz takes 4 parameters: The function we are
    integrating, the starting point (a), the ending point (b), and the amount
    of trapezoids (or slices of the function) we are applying to the problem.
    We create h, the actual length of each trapezoid, and k which is an
    array that contains the number of the trapezoid we would like to look at.
    Next, we plug in all of our values into an algorithm, and we return 
    our result!
    """
    
    h = (b-a)/N
    k = np.arange(1,N)
    I = h*(0.5*func(a) + 0.5*func(b) + func(a+k*h).sum())
    return I

def simps(func,a,b,N):
    """
    In this function, we use Simpsons method in order to examine the integral.
    Simps takes the same parameters as trapz, and we create close to the same
    amount of variables as well. We create several arrays in order to slice 
    up our function at many points in order to make Simpsons rule apply.
    After we declare all of our variables, we plug them all into the algorithm
    and return the final answer.
    """
    
    h = (b-a)/N
    k1 = np.arange(1,N/2+1)
    k2 = np.arange(1,N/2)
    I = (1./3.)*h*(func(a) + func(b) + 4.*func(a+(2*k1-1)*h).sum() + 2.*func(a+2*k2*h).sum())
    return I