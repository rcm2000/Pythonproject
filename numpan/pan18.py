import pandas as pd
import numpy as np

x = {'subj': ['math', 'comp', 'phys', 'chem', 'biol'], 'score': [100, 95, 85, 75, 80], 'avg': [95.2, 66.1, 69.5, 86.8, 91.2]}
df1 = pd.DataFrame(x, index=list('abcde'))
df2 = df1.reindex(list('abcdef'))

print(df2)

df2.to_csv('./df2.csv',sep=',',na_rep='NaN');
df2.to_csv('./df2_ind.csv',sep='|',na_rep='NaN',index=False,);

rdf1 = pd.read_csv('./df2_ind.csv',sep='|',header=None)
print(rdf1)


df1 = pd.DataFrame(
    {'상품번호':['p1','P2','p3','P4'],
    '수량':['3,000','2,000','5,000','6,000']}
)
print(df1)

df1['상품번호'] = df1['상품번호'].str.upper()
df1['상품번호'] = df1['상품번호'].str.strip('P')
df1 = df1['수량'].str.replace(',','')
df1 = df1.astype(float)
print(df1)
