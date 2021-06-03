num1 = int(input('첫번째 숫자를 입력하세요....?'))
num2 = int(input('두번째 숫자를 입력하세요....?'))
num3 = int(input('세번째 숫자를 입력하세요....?'))
max1 = 0;
min1 = 0;
if not (num1 // 10 < 10 and num2 // 10 < 10 and num3 // 10 < 10) or (num1 > 0 and num2 > 0 and num3 > 0):
    exit(0);
if num1 > num2 and num1 > num3:
   max1 = num1
elif num2 > num1 and num2 > num3:
   max1 = num2
elif num3 > num2 and num3 > num1:
   max1 = num3
print('최대값 = ',max1)
if num1 < num2 and num1 < num3:
   min1 = num1
elif num2 < num1 and num2 < num3:
   min1 = num2
elif num3 < num2 and num3 < num1:
   min1 = num3
print('최소값 = ',min1)
print('최대값 - 최소값 = ',max1 - min1)
