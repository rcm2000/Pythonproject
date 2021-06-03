s = ',';
st1 = 'abcdefg'
print(s.join(st1))

st2 = 'abc efg'
result = st2.replace('ef','xx')
print(result)

print('['+st2.ljust(10)+']')
print('['+st2.rjust(10)+']')
print('['+st2.center(10)+']')