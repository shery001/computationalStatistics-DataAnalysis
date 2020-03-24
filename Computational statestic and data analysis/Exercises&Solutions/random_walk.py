# random_walk.py - performs a Gauss-random walk in 2 dimensions
# by Bjoern Malte Schaefer, GSFP+/Heidelberg, bjoern.malte.schaefer@uni-heidelberg.de

import numpy as np
import scipy as sp
import pylab as plt

lim = 100					# plotting range
step = 1000					# number of steps
rep = 100					# number of walks

plt.close()
goal = np.zeros([2,rep])

for i in range(0,rep):
	a = np.random.normal(0.0,1.0,step)	# draw Gaussian random numbers
	x = np.cumsum(a)			# build cumulative sum for x-direction
	b = np.random.normal(0.0,1.0,step)	# draw Gaussian random numbers
	y = np.cumsum(b)			# build cumulative sum for y-direction
	cstring = [i/rep,0,1-i/rep]		# set colour depending on loop index
	#plt.plot(x,y,'b-',color=cstring)	# plot each walk in a different colour
	goal[0,i] = x[-1]			# memorise end point coordinates
	goal[1,i] = y[-1]
	
plt.plot(goal[0,:],goal[1,:],'yo')		# draw end point coordinates
sigma = np.std(goal,axis=1)			# measure sigma
print(sigma)

r = sigma[0]**2 + sigma[1]**2			# compute radius and draw circle
r = np.sqrt(r)
circ = plt.Circle((0.0,0.0),radius=r,color='k',fill=False)
fig=plt.figure(1)
ax = fig.add_subplot(1,1,1)
ax.add_patch(circ)

plt.title('diffusive processes and random walks')
plt.xlim([-lim,+lim])				# set plotting range
plt.ylim([-lim,+lim])
plt.xlabel('$x$-axis')
plt.ylabel('$y$-axis')
plt.axes().set_aspect('equal')			# set equal axis ratio
plt.show()					# show plot
