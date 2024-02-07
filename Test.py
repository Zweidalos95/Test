import numpy as np
#import matplotlib.pyplot as plt

theta=np.linspace(0,2*np.pi,100)
for ang in theta:
	print(np.cos(ang),np.sin(ang))


#plt.plot(np.cos(theta),np.sin(theta))
#plt.savefig('Try.jpg')

plt.show()