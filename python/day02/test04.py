num1 = input('첫번째 수를 입력하세요...')
num2 = input('두번째 수를 입력하세요...')
result = int(num1) + int(num2)
if result % 2 == 0:
    print('짝수 입니다')
elif result % 2 == 1:
    print('홀수 입니다')
else:
   print('다시 확인해 주세요.')
