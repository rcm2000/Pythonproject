import pandas as pd

df = pd.read_csv('train.csv');
# print(df)

df2 = df['Survived'].sum()
sv = df[df['Survived']==1]['Sex'].value_counts()
dead = df[df['Survived']==0]['Sex'].value_counts()
print(sv)
print(dead)

df3 = df.groupby(by=['Survived','Age'],as_index=True).count()
print(df3)

df4 = df.groupby(by=['Pclass','Sex'],as_index=True).mean()['Survived']
print(df4)

df5 = df[df['Age'] > 60].groupby(by=['Sex'],as_index=True).mean()['Survived']
print(df5)

