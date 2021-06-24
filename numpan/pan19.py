import pandas as pd
import numpy as np

df1 = pd.DataFrame(
    {'상품번호':['p2','P2','p3','P3'],
    '수량':['3,000','2,000','5,000','6,000']}
)

df1['상품번호'] = df1['상품번호'].str.upper();
df1['수량'] = df1['수량'].str.replace(',','')
df1 = df1.astype({'수량':float})
print(df1)
gbf1 = df1.groupby(by=['상품번호'],as_index = False).mean()
print(gbf1)

df1['고객번호'] = ['C1','C2','C2','C2']
print(df1)

df2 = df1.groupby(by=['고객번호','상품번호'],as_index=False).count()
print(df2)