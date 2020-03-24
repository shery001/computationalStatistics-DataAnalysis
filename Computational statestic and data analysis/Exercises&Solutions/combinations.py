# combinations.py - combinations of pairs of Gaussian random numbers
# by Bjoern Malte Schaefer, GSFP+/Heidelberg, bjoern.malte.schaefer@uni-heidelberg.de

import numpy as np
import pylab as plt

sigma = 1.0
rep = 100000
a = np.zeros(rep)

for i in range(0,rep):
	x = np.random.normal(0.0,sigma,1)
	y = np.random.normal(0.0,sigma,1)
	a[i] = x + y
	# a[i] = x * y

plt.close()
n,x,p = plt.hist(a,100,normed=1)
y = plt.normpdf(x,0.0,sigma)
plt.plot(x,y,'g--',linewidth=1.5,label='original Gaussian')

plt.title('combinations of Gaussian random numbers')

plt.xlabel('sum $x+y$ or product $x\cdot y$ of two Gaussian numbers $x$ and $y$')
plt.ylabel('distribution')

plt.xlim([-3,3])
plt.show()