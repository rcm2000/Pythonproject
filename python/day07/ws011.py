import csv
f = open('.csv');
data = csv.reader(f);
header = next(data);
# data 구조를 [, []]로 만들기
list_data = list(data)
k = [];
vv = ['Seoul'];
v = [];
kv = [];
#print(list_data)
for i in range(0, len(list_data)):
    lc1 = list_data[i]
    k.append(lc1[0][0:3])
    v.append(lc1[2])
# 문제 이해를 잘못했네..........
list_nd = ['name', 'data'];
new_v = list(map(float, v))
# print(new_v)
list_v = [vv[0],new_v[:]]
dict_c = dict(zip(list_nd, list_v))
print(dict_c)
