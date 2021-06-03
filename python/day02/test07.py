num1 = int(input('두자리 숫자를 입력하세요....?'))
if num1 // 10 < 10 and num1 // 10 >= 1:
    pass
else:
    exit(0)
if num1 % 3 == 0 and num1 % 2 == 0 and num1 > 0:
    print('OK')
else:
    print('Fail')


