score = [
['2019-01-03',10,12,14,10],
['2020-02-03',12,12,14,11],
['2020-03-03',13,13,15,12],
['2020-03-03',14,14,16,13],
['2020-04-03',15,15,17,14]
]
sum1 = 0
sum2 = 0
le1 = 0
le2 = 0
for i in score:
    if i[0].startswith('2019'):
        sum1 += sum(i[1:])
        le1 += len(i) - 1
    elif i[0].startswith('2020'):
        sum2 += sum(i[1:])
        le2 += len(i) - 1
print('2019년 평균온도 : %.2f' % (sum1 / le1))
print('2020년 평균온도 : %.2f' % (sum2 / le2))
#     if i[0].startswith('2019'):
#         for j in i[1:]:
#             sum1 += j
#         le1 += len(i)-1
#     elif i[0].startswith('2020'):
#         for j in i[1:]:
#             sum2 += j
#         le2 += len(i)-1
# print('2019년 평균온도 : %.2f' %(sum1/le1))
# print('2020년 평균온도 : %.2f' %(sum2/le2))
#






    # print('%s %.2f'%(i[0],sum/(len(i)-1)))