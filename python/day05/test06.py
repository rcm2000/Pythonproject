num1 = 400
num2 = 10.1234
st1 = '결과입니다.'

print(num1,num2,st1)
print('실행화면은: %s %s %s'%(num1,num2,st1))

result = '실행화면은: %-10s %s %s %x'%(num1,num2,st1,num1)
print(result)

result2 = '[실행화면은:{0:10d},{1:f},{2:10s}]'.format(num1,num2,st1)
print(result2)