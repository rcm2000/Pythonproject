import pandas as pd
import numpy as np

data = {'subject' : ['math', 'comp', 'phys', 'chem'], 'score': [100, 90, 85, 95], 'students': [94, 32, 83, 17]}

df = pd.DataFrame(data)
df['score2'] = [90,85,75,33]
print(df)
print(df.iloc[0,[1,2]])
print('==================================')
# print(df[['score','score2']])
#
print(df.loc[0:2,['score','score2']])