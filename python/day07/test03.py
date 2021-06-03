datas = ['a','b','c','d','e','f']

for c in datas:
    print(c)

for i in range(0,len(datas)):
    print(datas[i])

for no, c in enumerate(datas,1):
    print('순번: %d, 값 : %d' %(no,c))