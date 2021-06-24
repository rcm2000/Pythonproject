import numpy as np
import pandas as pd;
from matplotlib import pyplot as plt
# 한글 폰트 사용을 위해서 세팅
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table',header=0,index_col=0)


summer = df[1].iloc[1:,:5]
summer.columns = ['경기수','금','은','동','합계']
sort_summer = summer.sort_values('금',ascending=False)
sort_summer.to_csv('./sort_summer.csv',sep=',');
# print(sort_summer)

sort_summer = sort_summer.astype(float)
medal = sort_summer.div(sort_summer['경기수'],axis = 0)
del medal['경기수']
medal = medal.dropna() # 총합계가 0이여서 분모가 0으로 NaN이 된것들 제거
print(medal)
gmedal = medal.sort_values('금',ascending=False)
smedal = medal.sort_values('은',ascending=False)
gmedal = gmedal['금'][1:11]
smedal = smedal['은'][1:11]

data = pd.concat([gmedal,smedal],axis=1)
data = data.transpose()
print(data)
data.T.plot();
plt.show();


# del medal['경기수']
# del medal['합계']
# medal = medal.dropna() # 총합계가 0이여서 분모가 0으로 NaN이 된것들 제거
# print(medal)
#
#
# gmedal = medal.sort_values('금',ascending=True)
# print(gmedal)