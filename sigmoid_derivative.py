import numpy as np
import math
import matplotlib.pyplot as plt
def sigmoid(x):
    z = 1/(1 + np.exp(-x))
    return z;

    
x = np.linspace(-5,5,50)
z = sigmoid(x)
k = z*(1-z)
plt.plot(x,k)
plt.show()
