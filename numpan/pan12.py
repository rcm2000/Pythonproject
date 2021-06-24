import pandas as pd
import numpy as np

data = [[1.4, np.nan], [8.3, -2.1], [0.02, -1.11], [np.nan, np.nan]]
x = pd.DataFrame(data, columns=['one', 'two'], index=['a', 'b', 'c', 'd'])
print(x)
print(x.mean())
print(x.mean(axis = 1))

data = {
    'name':['james1','james2','james3','james4','james5'],
    'ko': [100, 90, 89, 99, 89],
    'en': [99, 91, 87, 89, 81],
    'ma': [80, 92, 88, 99, 87],
    'si': [99, 100, 87, 93, 86],

}
df = pd.DataFrame(data)


df.index = data['name']
del df['name']

print(df)
# print(df.mean(axis = 1))
# avr1 = df.mean(axis = 1)
# sum1 = df.sum(axis = 1)
# df['avr1'] = avr1
# df['sum1'] = sum1
# avr2 = df.mean()
# sum2 = df.sum()
# df.loc['avr2'] = avr2
# df.loc['sum2'] = sum2
# print(df)
#
#
# df2 = df.loc[df['ko'] > df.loc['avr2']['ko']]
# df2 = df2.drop('sum2', axis = 0)
# print(df2)
#
# df3 = df.loc[df['avr1'] > df.loc['avr2']['avr1']]
# df3 = df3.drop('sum2', axis = 0)
# print(df3)
# # df2 = df.loc[df['ko'] > 90]
#
# print(new_df)


print(df.loc[df['ko'] > df['ko'].mean()])
print(df)
print(df.min())
print(df.max())
print(df.min(axis = 1))
print(df.max(axis = 1))
print(df.idxmin())
print(df.idxmax())
df5 = df.idxmax()
df5 = pd.DataFrame(df5, columns=['name'])
print(df5)
df5['score'] = df.max()
print(df5)
print('---------------------------------------------')
# print(dict(df5))

dict1 = {}
print(df5['name'].values.tolist())
print(df5['score'].values.tolist())
dict1['name'] = df5['name'].values.tolist()
dict1['score'] = df5['score'].values.tolist()
dict2 = {df5.columns[0]:df5['name'].tolist(),df5.columns[1]:df5['score'].tolist()}
print(dict1)
print(dict2)






