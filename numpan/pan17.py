import pandas as pd
import numpy as np

df1 = pd.DataFrame({'a': [10, 11, 12, 13], 'b': [20, 21, 22, 23]}, index = [0, 1, 2, 3])
df2 = pd.DataFrame({'c': [32, 33, 34, 35], 'd': [42, 43, 44, 45]}, index = [2, 3, 4, 5])
print(df1)
print(df2)

print(df1.join(df2, how='inner'))
df4 = pd.concat([df1,df2])
print(df4)