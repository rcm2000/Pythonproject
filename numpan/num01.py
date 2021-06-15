import random

import matplotlib.pyplot as plt
import numpy as np


print(np.random.choice(10,6,replace=False))

dice = np.random.choice(6,10)

plt.hist(dice,bins=6)
plt.show()