st1 = 'abcd';
st2 = st1.upper()

if 'b' in st1.lower():
    print('ok')

st3 = '   abc   '
print(st3.strip())
print(st3.lstrip())
print(st3.rstrip())
sum = 0
st4 = '1,2,3,4'
for i in st4.split(','):
    sum += int(i)
print(sum)
print(st4.split())

st5 = '''안녕하세요 파이썬 교육입니다.\n안녕하세요 파이썬 파이썬 교육입니다. 
안녕하세요 파이썬 파이썬 파이썬 교육입니다.\n안녕하세요 파이썬 교육입니다.'''
c = 0;

for c in st5.split():
    print(c)
print('-----------------------------')
for li in st5.splitlines():
    print(li.count('파이썬'))
