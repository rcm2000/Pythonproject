import csv


class Tempa:
    def aj05(self):
        f = open('C:\\PycharmProjects\\js\\ta.csv');
        data = csv.reader(f);
        header = next(data);
        tempa = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
        for row in data:
            for i in range(2010, 2021):
                if i == int(row[0].split('-')[0]):
                    tempa[i - 2010] += float(row[2]);

        for i in range(0, len(tempa)):
            tempa[i] = tempa[i] / 365;

        data = [{
            'name': '년도별 평균 기온',
            'data': tempa
            }];
        return data;


    # 서울의 월평균 기온을 구하시오
    def aj04(self, year, month,cmd):
        f = open('C:\\PycharmProjects\\js\\ta.csv');
        data1 = csv.reader(f);
        header = next(data1);
        htemp = [];
        ltemp = [];
        for row in data1:
            if year == int(row[0].split('-')[0]) and month == int(row[0].split('-')[1]):
                ltemp.append(float(row[3]))
                htemp.append(float(row[4]))
        if cmd == 'h':
            data = [{
                'name': '일별 최대 기온',
             'data': htemp
            }];
        elif cmd == 'l':
            data = [{
                'name': '일별 최저 기온',
             'data': ltemp
            }];
        elif cmd == 'a':
            data = [{
                'name': '일별 최대 기온',
                'data': htemp
            },
                {
                'name': '일별 최저 기온',
                'data': ltemp
            }];

        return data;
    def aj06(self,year,cmd):
        f = open('C:\\PycharmProjects\\js\\ta.csv');
        data = csv.reader(f);
        header = next(data);
        tempm = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
        a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
        for row in data:
            if year == int(row[0].split('-')[0]) :
                for i in range(1,13):
                    if i == int(row[0].split('-')[1]):
                        tempm[i-1] += float(row[2]);
                        a[i-1] += 1
        for i in range(0, len(tempm)):
            tempm[i] = tempm[i] / a[i];



        if cmd == 'e':
            data = [{
                'name': '각 년도 별 월평균 기온',
                'data': tempm
            }];

        if cmd == 'a':

            data = [{
                'name': '각 년도 별 월평균 기온',
                'data': tempm
            }];

        return data



        # for i in range(0, len(tempm)):
        #     tempm[i] = tempm[i] / 12;








if __name__ == '__main__':
    Tempa().aj06(2012);