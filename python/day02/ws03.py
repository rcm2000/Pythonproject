import math

num1 = float(input('직각삼각형의 가로의 길이를 입력하세요....?'))
num2 = float(input('직각삼각형의 세로의 길이를 입력하세요....?'))
if not (num1 > 0 and num2 > 0):
    exit(0)
a = num1**2
b = num2**2
c = a + b
print("나머지 한 변의 길이 = ",math.sqrt(c))

