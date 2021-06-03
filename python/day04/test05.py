def calc(c,*n):
    result = 0;
    if c == '+':
        result = n[0] + n[1];
    elif c == '-':
        result = n[0] - n[1];
    elif c == '*':
        result = n[0] * n[1];
    elif c == '/':
        result = n[0] / n[1];
    else:
        print('다시 입력해 주세요')
        exit(0)

    return result;

n1 = int(input('첫번째 숫자를 입력하시오'))
n2 = int(input('두번째 숫자를 입력하시오'))
c = input('연산자를 입력하시오(+,-,*,/)')
print(calc(c,n1,n2))