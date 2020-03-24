# python_tutorial3.py - define functions and solve equations of the type g(x) = y for x numerically
# by Bjoern Malte Schaefer and Alessio Spurio Mancini

import numpy as np
import scipy.optimize as so
 
def exponential(x,y):
	result = np.exp(x) - y
	return(result)

y = 2.0
x = so.fsolve(exponential,1.0,args=(y,))
print(x,np.exp(x),y)