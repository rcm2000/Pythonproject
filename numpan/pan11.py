import pandas as pd
import numpy as np

data = [1,2,3,4];

s1 = pd.Series(data);
print(s1)

s2 = s1.copy()

print(s1+s2)

x = pd.DataFrame(np.arange(12).reshape(3, 4), columns = list('abcd'))
print(x)
xx = x.loc[1]
print(x + xx)
print(x.add(xx))
print(x + [9,9,9,9])

