from weadb import WeaDB
from weavo import WeadbVO
from urllib import request

import bs4

taget = request.urlopen('https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108');
soup = bs4.BeautifulSoup(taget,'html.parser');

print('start ...');

wdb = WeaDB('Weather');
wdb.makeTable()

while True:
    cmd = input('Input Command(i,d,u,s,sa,q)');
    if cmd == 'q':
        print('bye');
        break;
    elif cmd == 'i':
        print('Insert');
        # for st in soup.select('location'):
        #     province = st.select_one('province').string
        #     city = st.select_one('city').string
        #     data = st.select_one('data').string
        #     for st2 in st.select('data'):
        #         wf = st2.select_one('tmn').string
        #         tmEf = st2.select_one('tmx').string

        city = input('input city..');
        province = input('input province..');
        tmn = float(input('input tmn..'));
        tmx = float(input('input tmx..'));
        date = input('input date..');
        whe = WeadbVO(city,province,tmn,tmx,date);
        wdb.insert(whe);
    elif cmd == 'd':
        print('Delete');
        city = input('input city..');
        wdb.delete(city);
    elif cmd == 'da':
        print('Delete All');
        wdb.deleteall();
    elif cmd == 'u':
        print('Update');
        city = input('input city..');
        province = input('input province..');
        tmn = float(input('input tmn..'));
        tmx = float(input('input tmx..'));
        date = input('input date..');
        whe = WeadbVO(city,province,tmn,tmx,date);
        wdb.update(whe);
    elif cmd == 's':
        print('Select');
        city = input('input id..');
        ir = wdb.select(city);
        print(ir);
    elif cmd == 'sa':
        print('Select All');
        irs = wdb.selectall();
        for i in irs:
            print(i);

print('end ...');