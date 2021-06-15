import csv

import numpy as np
import matplotlib.pyplot as plt
from config.settings import DATA_DIRS

class P230:
    def p248(self,loc):
        f = open(DATA_DIRS[0] + '\\age2.csv')
        data = csv.reader(f)
        next(data)

        data = list(data)
        data3 = []
        for row in data:
            if loc in row[0]:
                home = np.array(row[3:],dtype=int)
                home2 = home / int(row[2].replace(',',''))
        min = 999;
        result_name = '';
        result = None;
        for row in data:
            away = np.array(row[3:],dtype=int)
            away2 = away / int(row[2].replace(',', ''))
            s = np.sum(np.abs(home2 - away2))
            if s < min and loc not in row[0] :
                min = s
                result_name = row[0]
                result = away2

        data3 = ({
            'name': loc,
            'data': home2.tolist()
        },{
            'name': result_name,
            'data': away2.tolist()
        })
        print(data3)
        return data3
    def p231(self):
        f = open(DATA_DIRS[0] + '\\age3.csv')
        data = csv.reader(f)
        next(data)
        data = list(data)
        data1 = []
        data2 = []
        data3 = []
        max = 0;
        for row in data[1:]:
            babys = np.array(row[3:9],dtype=int)
            data2.append(babys.tolist())
            data1.append(row[0])
        for i in range(0,len(data1)):
            data3.append({
            'name': data1[i],
            'data': data2[i]
            })
        print(data3)
        return data3


 #28번째
    def p232(self):
        f = open(DATA_DIRS[0] + '\\age4.csv')
        data = csv.reader(f)
        next(data)
        data = list(data)
        data1 = []
        data2 = []
        data3 = []
        pop_list1 = [];
        max = 0;
        for row in data[1:]:
            data1.append(row[0])
            data2.append(int(row[1]))
            data2.append(int(row[14]))
            data2.append(int(row[27]))
            data3.append(data2)
            data2 = []

        for i in range(0,len(data1)):
            pop_list1.append({
            'name': data1[i],
            'data': data3[i]
            })
        print(pop_list1)
        return pop_list1











if __name__ == '__main__':
    P230().p248('신림동')


