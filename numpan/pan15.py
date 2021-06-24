import pandas as pd
import numpy as np

x1 = pd.DataFrame(np.random.randint(10, 100, (3, 4)), columns = list('ABCD'), index = list('abc'))
x2 = pd.DataFrame(np.random.randint(10, 100, (3, 4)), columns = list('ABCD'), index = list('def'))



x3 = pd.concat([x1,x2],ignore_index= True)
dt = pd.date_range('20210614', periods=6)
x3.index = dt
print(x3)



