import pandas as pd
import numpy as np


data = {'subject' : ['math', 'comp', 'phys', 'chem'], 'score': [100, 95, 80, 90], 'students': [87, 39, 50, 72]}

df = pd.DataFrame(data, columns = ['subject', 'score', 'students', 'class'])
df2 = df.copy()

print(df)
del df2['class']
print(df2['score']/df2['students'])
df2['average'] = df2['score']/df2['students']
print(df2)
df3 = df2.dropna()
print(df3)





