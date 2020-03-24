# large_numbers1.py - law of large numbers
# by Bjoern Malte Schaefer and Alessio Spurio Mancini, Heidelberg University

# please note: the Chebyshev-inequality is the law of large numbers for a single sample!

# test the law of large numbers by simulating an experiment. do this by extracting a sample of nsample random numbers from a Gaussian distribution with mean = 0 and sigma = 1.0 and taking the mean of every realisation. set a value epsilon and verify directly on your sample the inequality of the law of large numbers. this can be done by repeating the experiment and counting how often a sample exceeds epsilon.

import numpy as np
import pylab as plt

rep = 1000
nsample = 7
sigma = 1.0
epsilon = 0.4

# carry out numerical experiment
count = 0
for i in range(0,rep):
	aux = np.random.normal(0.0,sigma,nsample)
	mu = np.mean(aux)
	if(abs(mu) > epsilon): count += 1;

# compute the relative occurrence of the "too large" estimates mu
result = count / rep

# Chebyshev-bound for the law of large numbers
bound = sigma**2 / nsample / epsilon**2

print(result,bound)
