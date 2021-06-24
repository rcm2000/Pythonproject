import pandas as pd
import numpy as np

t = pd.read_csv('test.csv');
print(t)

print(t.shape)
print(t.columns)
t1 = t.groupby(by=['pclass','sex'],as_index=True).mean()['age']
print(t1)