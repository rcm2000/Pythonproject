import matplotlib.pyplot as plt
import numpy as np
import pandas as pd;
# 한글 폰트 사용을 위해서 세팅
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

df = pd.read_html('https://finance.naver.com/sise/lastsearch2.nhn',encoding='euc-kr')

stock = df[1].dropna(axis=0)
stock.index = stock['종목명']
del stock['종목명']
data = stock.loc[:,['등락률','검색비율']]
data = data.transpose()



s1 = data.loc['등락률']
s2 = data.loc['검색비율']
s3 = s1.map(lambda x : x.replace('%',''))
s3 = s3.map(lambda x : x.replace('+',''))
s4 = s2.map(lambda x : x.replace('%',''))
data2 = pd.concat([s3,s4],axis=1)
data2 = data2.transpose()
data3 = data2.astype(float)
print(data3)
data3.T.plot();
plt.show();












