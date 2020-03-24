# gauss_inversion.py - generates Gaussian random numbers using the inversion method
# by Bjoern Malte Schaefer and Alessio Spurio Mancini

import numpy as np
import scipy.special as sp
import scipy.optimize as so
import pylab as plt

plt.close()

nsample = 10000

def cumu_gauss(x,y):
	result = (1.0 + sp.erf(x/np.sqrt(2.0))) / 2.0 - y
	return(result)
	
def gauss(x):
	result = np.exp(-x**2 / 2.0) / np.sqrt(2.0 * np.pi)
	return(result)
	
x = np.linspace(-4,4,101)
y = gauss(x)
plt.plot(x,y,'r-',label='Gaussian distribution')

xs = np.zeros(nsample)
for i in range(0,nsample):
	ys = np.random.uniform(low=0.0,high=1.0)
	aux = so.fsolve(cumu_gauss,0.0,args=(ys,))
	xs[i] = aux

plt.hist(xs,30,normed=True,label='samples')

plt.xlabel('samples $x$')
plt.ylabel('distribution $p(x)\mathrm{d}x$')

plt.legend(loc='upper right')
plt.show()
