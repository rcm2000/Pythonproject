import pandas as pd
import numpy as np

datas = np.random.randint(10,100,(6,4));
print(datas)
df = pd.DataFrame(datas)
df.columns = ['score1','score2','score3','score4']
df.index = ['서울','경기','부산','인천','대구','대전']
#index = pd.date_range('20210114', periods=6)
print(df)
