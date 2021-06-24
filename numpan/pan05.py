import pandas as pd
import numpy as np

data = {'subject' : ['math', 'comp', 'phys', 'chem'], 'score': [100, 90, 85, 95], 'students': [94, 32, 83, 17]}
df = pd.DataFrame(data);

print(df)

x = pd.DataFrame(data, columns = ['subject', 'score', 'students', 'class'], index = ['one', 'two', 'three', 'four'])
x['class2'] = [1,2,3,4]
x['class'] = [1,2,3,4]
x.columns = ['a','s','d','f','g']
print(x)

print(x.columns)
print(x[['a','s','d']].values.tolist())

print(x.loc['two',['s','g']])

x3 = x[['s','d','g']]
print(x3)
