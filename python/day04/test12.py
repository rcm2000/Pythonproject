st1 = 'cjdauddl93@naver.co.kr'

print(len(st1))
print(st1.find('@'))
aa = st1.find('@')
bb = st1.find('.')
print(st1.rfind('.'))

id = st1[0:aa]
domain = st1[aa+1:bb]
print(id)
print(domain)