score = [
['2019-01-03',10,12,14,10],
['2020-02-03',12,12,14,11],
['2020-03-03',13,13,15,12],
['2020-03-03',14,14,16,13],
['2020-04-03',15,15,17,14]
]
a = []
for i in score:
    avg = 0;
    if i[0].startswith('2020'):
         avg += sum(i[1:]) / (len(i)-1)
         a.append(avg)
print(a)
print('2020년도 일평균 최고값 : %.2f 최저값 : %.2f 최고값 - 최저값 : %.2f' %(max(a),min(a),(max(a)-min(a))))
