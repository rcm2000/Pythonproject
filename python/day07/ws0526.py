import csv

import numpy as np

f = open('c:\\mydata\\ta_20210526162630.csv');
data = csv.reader(f);
header = next(data)
print(header)
print('-----------------------------')
avg_tmp =[];
sum1 = 0;
avg1 = 0;
n=0
i = 1;
bre = 0
while i < 13:
    if i == 12:
        avg_tmp.append(sum1 / n)
        break
    for row in data:
        if int(row[0].split('-')[1]) == i:
            sum1 += float(row[2])
            n += 1
        elif int(row[0].split('-')[1]) != i:
            avg_tmp.append(sum1/n)
            i += 1
            sum1 = float(row[2]);
            n = 1;

result = list(np.round(avg_tmp,2))
print(result)










# for row in data:
#     if row[0].split('-')[1] == '01':
#         a1.append(float(row[2]))
#     elif row[0].split('-')[1] == '02':
#         a2.append(float(row[2]))
#     elif row[0].split('-')[1] == '03':
#         a3.append(float(row[2]))
#     elif row[0].split('-')[1] == '04':
#         a4.append(float(row[2]))
#     elif row[0].split('-')[1] == '05':
#         a5.append(float(row[2]))
#     elif row[0].split('-')[1] == '06':
#         a6.append(float(row[2]))
#     elif row[0].split('-')[1] == '07':
#         a7.append(float(row[2]))
#     elif row[0].split('-')[1] == '08':
#         a8.append(float(row[2]))
#     elif row[0].split('-')[1] == '09':
#         a9.append(float(row[2]))
#     elif row[0].split('-')[1] == '10':
#         a10.append(float(row[2]))
#     elif row[0].split('-')[1] == '11':
#         a11.append(float(row[2]))
#     elif row[0].split('-')[1] == '12':
#         a12.append(float(row[2]))
#
# avg_tmp.append(sum(a1)/len(a1))
# avg_tmp.append(sum(a2)/len(a2))
# avg_tmp.append(sum(a3)/len(a3))
# avg_tmp.append(sum(a4)/len(a4))
# avg_tmp.append(sum(a5)/len(a5))
# avg_tmp.append(sum(a6)/len(a6))
# avg_tmp.append(sum(a7)/len(a7))
# avg_tmp.append(sum(a8)/len(a8))
# avg_tmp.append(sum(a9)/len(a9))
# avg_tmp.append(sum(a10)/len(a10))
# avg_tmp.append(sum(a11)/len(a11))
# avg_tmp.append(sum(a12)/len(a12))
# print(np.round(avg_tmp,2))
# result = list(np.round(avg_tmp,2))
# print(result)
# f.close()




