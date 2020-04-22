import numpy as np
import math
import matplotlib.pyplot as plt
x = np.linspace(-5,5,50)
z = 1/(1 + np.exp(-x))
plt.plot(x,z)
plt.show()
