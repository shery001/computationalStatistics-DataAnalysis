# large_numbers2.py - tests out the law of large numbers with a numerical experiment
# by Bjoern Malte Schaefer, Centre for Astronomy, Heidelberg University

# test the law of large numbers. first, repeatedly draw a sample of nsample numbers from a uniform distribution, for rep times. take the mean of every realisation and plot the distribution. repeat the same for an ever increasing nsample and in doing this verify the law of large numbers.

import numpy as np
import pylab as plt

# define sample size and repetitions
nsample = 30
rep = 10000
a = np.zeros(rep)

# loops over all repetitions
for i in range(0,rep):					
	aux = np.random.uniform(-1.0,1.0,nsample)
	a[i] = np.mean(aux)
	
n,x,p = plt.hist(a,40,normed=1)
sigma = np.std(a)
print(sigma*np.sqrt(nsample))

y = plt.normpdf(x,0.0,sigma)
plt.plot(x, y, 'g--', linewidth=1.5,label='best fitting Gaussian')				

plt.xlabel('estimate')
plt.ylabel('distribution of the estimates')
plt.xlim([-1.0, +1.0])
plt.title('law of large numbers in a numerical experiment')
plt.show()
