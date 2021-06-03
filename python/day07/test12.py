st = input('input number');
try:
    num = int(st)
    result = num * 100;
    print('%d , %d'%(num,result))
except:
    print('invalid number..try again')

print('end.........')
