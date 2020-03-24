# gauss_rejection.py - generates Gaussian random numbers using the rejection method
# by Bjoern Malte Schaefer and Alessio Spurio Mancini

import numpy as np
import pylab as plt

plt.close()

nsample = 10000
mmax = 4.0
mmin = -mmax

def gauss(x):
	result = np.exp(-x**2 / 2.0) / np.sqrt(2.0 * np.pi)
	return(result)
	
gmax = gauss(0.0)

xs = np.zeros(nsample)

for i in range(0,nsample):
	aux = 10.0
	pro = 0.0
	while(aux > gauss(pro)):
		pro = np.random.uniform(mmin,mmax)
		aux = np.random.uniform(0,gmax)
	xs[i] = pro

plt.hist(xs,30,normed=True,label='samples')

x = np.linspace(mmin,mmax,101)
y = gauss(x)
plt.plot(x,y,'r-',label='Gaussian distribution')

plt.xlabel('samples $x$')
plt.ylabel('distribution $p(x)\mathrm{d}x$')

plt.legend(loc='upper right')
plt.show()
