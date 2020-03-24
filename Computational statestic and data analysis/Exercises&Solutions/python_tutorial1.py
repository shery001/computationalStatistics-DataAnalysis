# collection of python commands
# by Bjoern Malte Schaefer and Alessio Spurio Mancini

# import numpy and matplotlib
import numpy as np
import pylab as plt

# close plotting window
plt.close()

# generate an empty vector with rep entries
rep = 20
a = np.zeros(rep)

# write numbers into the vector
for i in range(0,rep):
	a[i] = i
	
# print vector
print(a)

# generate random numbers
mu = 0.0
sigma = 1.0
nsample = 10000
aux = np.random.normal(mu,sigma,nsample)
#aux = np.random.uniform(-1.0,1.0,nsample)

# plot histogram and a Gaussian on top
bins = 30
n,x,p = plt.hist(aux,bins,normed=1)
y = plt.normpdf(x,mu,sigma)
plt.plot(x,y,'g--',linewidth=1.5)

# make plot nice
plt.xlabel('random number $x$')
plt.ylabel('probability $p(x)$')

plt.show()