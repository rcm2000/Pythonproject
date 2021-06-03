import random
temp1 = [];
for a in range(1,21):
    num = random.randint(1,9)
    temp1.append(num)
print(temp1)
num1 = input('1 ~ 9 까지의 숫자중 하나를 입력하세요.')
if not (len(num1) < 2 and num1.isnumeric() == False) :
    num2 = int(num1)
    print('같은수는 %d개 입니다' %temp1.count(num2))
else:
    print('다시 시도하세요')


