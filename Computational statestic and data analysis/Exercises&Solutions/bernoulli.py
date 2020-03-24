

import numpy as np
import scipy.special as sp
import scipy.stats as st
import pylab as plt

n = 30
p = 0.5
nsample = 10000

plt.close()

# draw distribution
k = np.linspace(0,n,n+1)
bernoulli = nsample * sp.binom(n,k) * p**k * (1.0 - p)**(n-k)
plt.plot(k,bernoulli,'r-')

# draw samples and plot
aux = np.random.binomial(n,p,nsample)
plt.hist(aux,n)

# compute asymmetry
asym = st.skew(aux) / np.var(aux)**1.5
print(asym)

plt.xlabel('$k$-values')
plt.ylabel(r'probability $B(n,p,k) \times n_\mathrm{sample}$')

lim = n * p + 3 * n * p * (1.0 - p)
plt.xlim([0,lim])

plt.show()
