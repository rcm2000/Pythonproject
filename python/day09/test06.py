from urllib import *

from urllib import request

import bs4

taget = request.urlopen('https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108');
soup = bs4.BeautifulSoup(taget,'html.parser');

for st in soup.select('location'):
    province = st.select_one('province').string
    city = st.select_one('city').string
    data = st.select_one('data').string
    for st2 in st.select('data'):
        wf = st2.select_one('tmn').string
        tmEf = st2.select_one('tmx').string
        print(city,province,tmEf,wf)



