# python_tutorial2.py - linear algebra and handling of data
# by Bjoern Malte Schaefer and Alessio Spurio Mancini

import numpy as np
import pylab as plt

plt.close()

# set up a matrix: initialise as empty, then set numbers
amatrix = np.zeros((2,2))
amatrix[0,1] = amatrix[1,0] = 1.0

# compute eigenvalues
w,v = np.linalg.eig(amatrix)
print(w)

# compute determinant
aux = np.linalg.det(amatrix)
print(aux)

# compute inverse
ainverse = np.linalg.inv(amatrix)
aux = np.dot(ainverse,amatrix)
print(aux)

# set up vector and initialize
bvector = np.zeros(2)
bvector[0] = 1.0
bvector[1] = 2.0

# compute norm
aux = np.linalg.norm(bvector)
print(aux)

# compute product between matrix and vector
aux = np.dot(amatrix,bvector)
print(aux)

# generate data and save
ndata = 1000
aux = np.random.normal(0.0,1.0,(ndata,2))
np.savetxt('./random_numbers.data',aux)

# read data
data = np.loadtxt('./random_numbers.data')

# cut out columns from the table
x = data[:,0]
y = data[:,1]

# plot data
plt.plot(x,y,'ro')

# nice plot: you can write latex directly
plt.xlabel('$x$-axis')
plt.ylabel('$y$-axis')

plt.xlim([-4,4])
plt.ylim([-4,4])

plt.axes().set_aspect('equal')

plt.show()
