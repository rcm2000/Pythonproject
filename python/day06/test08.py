dic = {'IE':28.5,'FF':10.3,'Chrome':38.9}
print(type(dic))
print(len(dic))
print(dic)
print(dic['IE'])
print(dic.get('Chrome'))
print('IE' in dic)

dic['IE'] = 29.5
dic['EG'] = 10.5
print(dic)
