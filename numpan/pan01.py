import numpy as np
import pandas as pd;

print(pd.__version__)

data = [1,2,3,4,5];

ndata = np.array(data)
pdata = pd.Series(data)
print(ndata)
print(pdata.values)
print(pdata.index)

pdata2 = pd.Series(data, index=['A','B','C','D','E'])
print(pdata2['B'])

data2 = {'name':'Kim','ko':100,'en':75,'ma':60,'si':100};
pdata3 = pd.Series(data2)

pdata3.name = 'Score Name';
pdata3.index.name = 'Score Index Name';
print(pdata3)
print(pdata3['name'])