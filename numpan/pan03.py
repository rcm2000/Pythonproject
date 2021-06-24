import pandas as pd
import numpy as np

data1 = ['A',2];
data2 = ['B',4];

df1 = pd.DataFrame([data1,data2]);
print(df1)

data = {'subject' : ['math', 'comp', 'phys', 'chem'], 'score': [100, 90, 85, 95], 'students': [94, 32, 83, 17]}
df2 = pd.DataFrame(data)
print(df2)
print(df2['score'].values)
print(df2.shape)
print(df2.shape[0])
print(df2.shape[1])

df3 = pd.DataFrame(df2 , columns=['students','score','subject'])
print(df3['students'][2])
print(df3[df3['students']>50])

dict1 = {'math': {1:94, 2:82}, 'comp': {1:48, 3:43, 2:83}}
df4 = pd.DataFrame(dict1)
print(df4)