import bs4
import pandas as pd
import numpy as np
import requests


from config.settings import DATA_DIRS


class Titanic:
    def t1(self,option):
        df = pd.read_csv(DATA_DIRS[0]+'\\train.csv');
        print(df)
        df2 = df.groupby(by=['Survived', option ],as_index = True).count()['Name']
        df3 = df2.unstack() #멀티 인덱스 해제
        print(df3)
        data = []
        for i in range(len(df3.columns)):
            data.append({
            'name': str(df3.columns[i]),
            'data': list(df3.iloc[:,i])
        })

        print(data)
        return data



class Galaxy:
    def g1(self):
        df = pd.read_csv(DATA_DIRS[0]+'\\spstat1.csv',encoding='euc-kr');

        print(df)

class Naver:
    def n1(self):
        df = pd.read_html('https://finance.naver.com/marketindex/?tabSel=materials#tab_section',encoding='euc-kr');


        df1 = df[2]
        df1 = df1.loc[:,['상품명','현재가','전일비','등락율']]
        df1.index = df1['상품명']
        del df1['상품명']

        ind = df1.index.to_list()
        price = df1['현재가'].astype(float).to_list()
        per1 = df1['전일비'].astype(float).to_list()
        df1['등락율'] = df1['등락율'].map(lambda x : x.replace('%',''))
        per2 = df1['등락율'].astype(float).to_list()
        data = [{
            'name': '현재가',
            'type': 'column',
            'yAxis': 1,
            'data': price,
            'tooltip': {
                'valueSuffix': ' 원'
            }

        }, {
            'name': '전일 비',
            'type': 'spline',
            'yAxis': 2,
            'data': per1,
            'marker': {
                'enabled': 'false'
            },
            'dashStyle': 'shortdot',
            'tooltip': {
                'valueSuffix': ' %'
            }

        }, {
            'name': '등락율',
            'type': 'spline',
            'data': per2,
            'tooltip': {
                'valueSuffix': ' %'
            }
        }]
        result = ind,data
        return result
class Open:
    def o1(self,startdt,enddt):
        url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=tDmcn3ZUmi4AshfL2fx58guDwaqt7%2BvOUYW%2B84DDNp4LvjUMJJYd38X0wis4cp2AVIuGbLSdHGeFx3Kta6YMQQ%3D%3D&pageNo=1&numOfRows=100&startCreateDt='+startdt+'&endCreateDt='+enddt
        result = requests.get(url)
        response = result.text.encode('utf-8')
        xml_obj = bs4.BeautifulSoup(response,'lxml-xml')
        rows = xml_obj.find_all('item')
        #print(np.float(rows[0].find('accDefRate').text));


        result = []
        nameList = []
        columnList = []


        rowslen = len(rows)
        print(rowslen)
        for i in range(rowslen):
            item = rows[i].find_all()
            itemdata = []
            for j in range(0, len(item)):
                if i == 0:
                    nameList.append(item[j].name)
                text = item[j].text
                itemdata.append(text)
            result.append(itemdata)

        data = pd.DataFrame(result,columns=nameList)
        data3 = data.loc[:,['deathCnt','stateDt','decideCnt','clearCnt']]
        data3.index = data3['stateDt']
        del data3['stateDt']
        print(data3)
        l1 = list(reversed(data3.index.to_list()))
        data = [{
                'name': '누적 사망자 수',
                'data': list(reversed(list(data3.iloc[:, 0].astype(int))))
            },{
                'name': '누적 확진자 수',
                'data': list(reversed(list(data3.iloc[:, 1].astype(int))))
            },{
                'name': '격리 해제',
                'data': list(reversed(list(data3.iloc[:, 2].astype(int))))
            }]

        result = l1,data
        print(result[0])
        return result


class myanalysis:
    def d1(self,year,sido,gugun):


        df = pd.read_json('http://apis.data.go.kr/B552061/AccidentDeath/getRestTrafficAccidentDeath?serviceKey=tDmcn3ZUmi4AshfL2fx58guDwaqt7%2BvOUYW%2B84DDNp4LvjUMJJYd38X0wis4cp2AVIuGbLSdHGeFx3Kta6YMQQ%3D%3D&searchYear='+year+'&siDo='+sido+'&guGun='+gugun+'&type=json&numOfRows=100&pageNo=1')
        del df['resultCode']
        del df['resultMsg']
        del df['pageNo']
        # print(df)
        # print(df.columns)
        df1 = df['items']
        df2 = pd.DataFrame(df1[0])
        df3 = df2.loc[:,['occrrnc_dt','dth_dnv_cnt','injpsn_cnt','lo_crd','la_crd']]
        df3['occrrnc_dt'] = df3['occrrnc_dt'].str[:6]
        df4 = df3.groupby(by=['occrrnc_dt'],as_index=False).sum()
        print(df4)
        month = df4['occrrnc_dt'].to_list()
        dth = df4['dth_dnv_cnt'].to_list()
        inj = df4['injpsn_cnt'].to_list()

        data = [{
        'name': '부상자 수',
        'type': 'column',
        'yAxis': 1,
        'data': inj,
        'tooltip': {
            'valueSuffix': ' 명'
        }

    }, {
        'name': '사망자 수',
        'type': 'spline',
        'data': dth,
        'tooltip': {
            'valueSuffix': ' 명'
        }
    }]
        result = month, data
        print(result[0],result[1])
        return result




if __name__ == '__main__':
    Naver().n1()
