import pandas as pd
import numpy as np


data = {'subject' : ['math', 'comp', 'phys', 'chem'], 'score': [100, 95, 80, 90], 'students': [87, 39, 50, 72]}

df = pd.DataFrame(data, columns = ['subject', 'score', 'students', 'class'])
df.index = ['one','two','three','four']
print(df)
print(df.shape)

df2 = pd.DataFrame(data)
print(df2)
df2.loc[df2.shape[0]] = ['kor',80,42];
print(df2)
df2.loc['gd'] = ['eng',86,97];
print(df2)
df2['score2'] = [98,77,84,64,98,98]
print(df2)

df3 = df2.drop([1,2])
print(df3)

