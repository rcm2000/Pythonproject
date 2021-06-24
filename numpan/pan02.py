import pandas as pd
import numpy as np

data = np.arange(0,5);
print(data)
idx = ['b','a','e','c','d']
pdata = pd.Series(data,index=idx)
print(pdata[1:3])
print(pdata[pdata>2].values)
pdata2 = pdata.reindex(np.sort(np.array(idx)))
print(pdata2)
idx.append('x')
idx.append('y')
pdata3 = pdata.reindex(np.sort(np.array(idx)),fill_value=0)
print(np.average(pdata3))

