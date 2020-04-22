import numpy as np
import matplotlib.pyplot as plt
import math
from PIL import Image
im = Image.open(r"download.png")
a = np.array(im)
c = a.flatten()
print(c)
