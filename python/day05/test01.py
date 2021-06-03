import re

s = 'python programming'

print(len(s))
print(s.find('th'))
print(s.rfind('o'))
print(s.index("p"))
print(s.count('o'))
print(s[:6])
result = ('g' in s)
print(result,'입니다')

st2 = 'abc123jj412j314'
st3 = '123'

print(st2.islower())
if st2.islower():
    print(st2.upper())

print(st2[0:2].isalpha(),st3.isnumeric())
a = re.findall('\d+',st2)
print(a)