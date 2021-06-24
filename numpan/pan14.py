import pandas as pd
import numpy as np

x1 = pd.DataFrame(np.random.randint(0, 100, (3, 4)), columns = list('ABCD'), index = np.arange(3))
x2 = pd.DataFrame(np.random.randint(100, 200, (3, 4)), columns = list('ABCD'), index = np.arange(3)+3)
x22 = pd.DataFrame(np.random.randint(100, 200, (3, 4)), columns = list('ABCD'), index = np.arange(3))

print(x1)
print(x2)


x3 = pd.concat([x1,x22],axis = 1)
print(x3)

