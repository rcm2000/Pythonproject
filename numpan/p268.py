import matplotlib.pyplot as plt
import numpy as np
import pandas as pd;

df = pd.read_csv('./age2.csv',encoding='euc-kr',index_col=0)
df2 = df.div(df.iloc[:,0],axis = 0)
df2 = df2.iloc[:,2:]

# name = '신대방'
# df_loc = df2[df2.index.str.contains(name)]
# df_loc = df_loc.dropna()
# x = df2.sub(df_loc.iloc[0],axis = 1)
# x = np.power(x,2)
# x = x.dropna()
# print(x)
# y = x.sum(axis = 1)
# result = y.sort_values().index[0:6];
# ddf = df2.loc[result]
# ddf.T.plot()
# plt.show()


name = '신대방제1동';
df_loc = df2[df2.index.str.contains(name)];
print(df_loc);
# 신대방 지역의 데이터 빼기 전체 데이터의 최소값
x = df2.sub(df_loc.iloc[0],axis=1);
x = np.power(x,2);
result = x.sum(axis=1);
result = result.sort_values();
result = result[result > 0];
result = result[:5];
print(result.index);
ddf = df2.loc[result.index];
ddf = pd.concat([ddf,df_loc])
print(ddf)



# ddf.T.plot();
# plt.show();
