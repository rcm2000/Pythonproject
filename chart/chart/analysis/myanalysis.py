import csv

from config.settings import DATA_DIRS


class MyAnalysis:

    def wm(self, year, month):
        f = open('data/ta.csv');
        data = csv.reader(f);
        header = next(data);
        htemp = [];
        ltemp = [];
        for row in data:
            if year == int(row[0].split('-')[0]) and month == int(row[0].split('-')[1]):
                ltemp.append(float(row[3]))
                htemp.append(float(row[4]))
        data = [{
            'name': '일별 최대 기온',
            'data': htemp
        },
            {
                'name': '일별 최저 기온',
                'data': ltemp
            }];
        print(data)
        return data

    def localage(self,target):
        f = open('data/age.csv');
        #f = open('../data/age.csv');
        data = csv.reader(f);
        header = next(data);
        cnt = [];
        mcnt = [];
        fcnt = [];
        for row in data:
            if target in row[0]:
                for i in row[3:104]:
                    cnt.append(int(i.replace(",","")));
                for i in row[106:207]:

                    mcnt.append(int(i.replace(",","")));
                for i in row[209:310]:

                    fcnt.append(int(i.replace(",", "")));
        data = [{
            'name':'male',
            'data': mcnt
        },{
            'name':'female',
            'data': fcnt
        }]
        print(data)
        return data

    def localage2(self,target):
        f = open('data/age.csv');
        #f = open('../data/age.csv');
        data = csv.reader(f);
        header = next(data);
        cnt = [];
        mcnt = [];
        fcnt = [];
        for row in data:
            if target in row[0]:
                # for i in row[3:104]:
                #     cnt.append(int(i.replace(",","")));
                for i in row[106:207]:

                    mcnt.append(-int(i.replace(",","")));
                for i in row[209:310]:

                    fcnt.append(int(i.replace(",", "")));
        data = [{
            'name':'male',
            'data': mcnt
        },{
            'name':'female',
            'data': fcnt
        }]
        print(data)
        return data

    def localage3(self,target):
        f = open(DATA_DIRS[0]+'\\age.csv');
        #f = open('../data/age.csv');
        data = csv.reader(f);
        header = next(data);
        cnt = 0;
        mcnt = 0;
        fcnt = 0;
        for row in data:
            if target in row[0]:
                cnt = int(row[1].replace(',',''));
                mcnt = int(row[105].replace(',',''));
                fcnt = int(row[208].replace(',',''));

        mper = mcnt / cnt * 100
        fper = fcnt / cnt * 100
        print(mper,fper)
        data = [{
            'name': 'Share',
            'data': [
                {'name': 'male', 'y': mper},
                {'name': 'female', 'y': fper}
            ]
        }]
        print(data)

        return data

    def subway(self,station,line):
        f = open(DATA_DIRS[0]+'\\subwayfee.csv');
        #f = open('../data/age.csv');
        data = csv.reader(f);
        header = next(data);
        cnt = [0,0,0,0];
        for row in data:
            if station in row[3] and line in row[1]:
                for i in range(4,8):
                    cnt[i-4] += int(row[i].replace(',',''));
        data = [{
            'name': 'Share',
            'data': [
                {'name': '유임승차', 'y': cnt[0]},
                {'name': '유임하차', 'y': cnt[1]},
                {'name': '무임승차', 'y': cnt[2]},
                {'name': '무임하차', 'y': cnt[3]},
            ]
        }]
        print(data)
        return data
    def iots(self):
        f = open(DATA_DIRS[0] + '\\mylog.csv');
        # f = open('../data/age.csv');
        data = csv.reader(f);
        header = next(data);
        for d in data:
            print(d)


if __name__ == '__main__':
    MyAnalysis().iots()