import pandas as pd
import numpy as np

s1 = pd.date_range('20210114', periods=6)
print(s1)
s1 = np.random.permutation(s1)
print(s1)
s2 = list('DBCA')
y = pd.DataFrame(np.random.randint(0, 100, (6, 4)), index=s1, columns=s2)
print(y)

y1 = y.sort_index(axis=0,ascending=False)
print(y1)
y1 = y.sort_index(axis=1,ascending=True)
print(y1)
y3 = y.sort_values(by='A' ,ascending=False)
print(y3)

y['E'] = np.random.choice(6,6,replace=True)
print(y)
print(y['E'].unique())
print('-----------------------------------------')
yy = y.transpose()
print(yy)
print(yy.loc['E'].isin([2]))
