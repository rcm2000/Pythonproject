import csv

import numpy as np
import matplotlib.pyplot as plt


class P230:
    def p248(self,loc):
        f = open('age2.csv')
        data = csv.reader(f)
        next(data)

        data = list(data)

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
        print(result_name)
        print(result)
        # for i in data:
        #
        #     home2 = np.array(i[3:])
        # print(home2)
        # print(len(home))
        plt.plot(home2)
        plt.plot(result)
        plt.legend()
        plt.show()

    def p231(self):
        f = open('age3.csv')
        data = csv.reader(f)
        next(data)
        data = list(data)
        sum_baby = []
        max = 0;
        for row in data[1:]:
            babys = np.sum(np.array(row[3:9],dtype=int))
            sum_baby.append(babys)
            if babys > max:
                max = babys
                result_name = row[0]
                result = babys
        print(result_name)
        print(result)

 #28번째
    def p232(self):
        f = open('age4.csv')
        data = csv.reader(f)
        next(data)
        data = list(data)
        pop_list1 = [];
        max = 0;
        for row in data[1:]:
            sum1 = int(row[27]) - int(row[1])
            pop_list1.append(int(row[27])-int(row[1]))
            if sum1 > max :
                max = sum1
                result_name = row[0]
                result = max

        pop_list1 = np.array(pop_list1)
        print(result_name)
        print(result)






# [ -3681   -485   1041 -14665  -8877  -5215  -8507   1285 -11109 -14156
#  -20715  -3362   1860  -3187  -9934 -16764    -89  -2184  11702  -4983
#   -6897  -8825  -3133   1325  32397]
#





if __name__ == '__main__':
    P230().p231()
    P230().p232()

