num1 = int(input('첫번째 숫자를 입력하세요...?'))
num2 = int(input('두번째 숫자를 입력하세요...?'))

max = 0;
if not (num1 // 10 < 1 and num2 // 10 < 1 and num1 > 0 and num2 > 0 ):
    print('bye')
    exit(0)
if num1 == num2:
    max = num1
elif num1 > num2:
    max = num1
    print('최댓값은',max,'입니다.')

else:
    max = num2
    print('최댓값은', max, '입니다.')

