import numpy as np

theta=np.linspace(0,2*np.pi,100)
for ang in theta:
	print(np.cos(ang),np.sin(ang))
