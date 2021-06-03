import csv
# datas = ['1','2','']
#
# sum1 = 0;
# for d in datas:
#     if d == None or d == '':
#         continue
#     num = int(d)
#     sum1 += num
# print(sum1)
# # 더웠던날 추웠던날

f = open('c:\\mydata\\ta_20210526162630.csv');
data = csv.reader(f);
header = next(data)
print(header)
print('-----------------------------')

max = 0.0;
max_date = '';
min = 0.0;
min_date = '';
for row in data:
    if max < float(row[4]):
        max = float(row[4])
        max_date = row[0]
    if min > float(row[3]):
        min = float(row[3])
        min_date = row[0]
print('%s , %.2f' %(max_date,max))
print('%s , %.2f' %(min_date,min))
f.close()



