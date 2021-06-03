num1 = int(input('첫번째 숫자를 입력하세요'))
num2 = int(input('두번째 숫자를 입력하세요'))

op = input("연산자를 입력하세요")

def plus(num1,num2):
    return num1+num2
def minus(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2

if op == "+":
    print('두 수의 합은')
    print(plus(num1,num2))
elif op == "-":
    print('두 수의 차는')
    print(minus(num1,num2))
elif op == "*":
    print('두 수의 곱은')
    print(multiply(num1,num2))
elif op == "/":
    print('두 수의 나눗셈은')
    print(division(num1,num2))
else:
    print('다시 입력해 주세요.')


