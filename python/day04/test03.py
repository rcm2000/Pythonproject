def calc(a,b,c):
    result = 0;
    if c == '+':
        result = a + b;
    elif c == '-':
        result = a - b;
    elif c == '*':
        result = a * b;
    elif c == '/':
        result = a / b;
    else:
        print('다시 입력해 주세요')
        exit(0)

    return result;

a = int(input('첫번째 숫자를 입력하시오'))
b = int(input('두번째 숫자를 입력하시오'))
c = input('연산자를 입력하시오(+,-,*,/)')
print(calc(a,b,c))