import pandas as pd
import numpy as np

x1 = pd.Series([0, 1, 2])
x2 = pd.Series([3, 4, 5])
x3 = pd.Series([6, 7, 8])

x4 = pd.concat([x1, x2, x3], axis = 1, keys=['a','b','c'])
print(x4)

df1 = pd.DataFrame(np.arange(12).reshape(3, 4), columns = list('ABCD'), index = np.arange(3))

print(df1)

x5 = pd.concat([df1,x4['a']],axis=1,ignore_index=True)
print(x5)
df3 = df1.append(x4['a'])
print(df3)
