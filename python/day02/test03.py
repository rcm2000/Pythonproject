num1 = int(input('input number1...?'));
num2 = int(input('input number2...?'));
op = input('input op(+ - * /)...?');
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "/":
    result = num1 / num2
elif op == "*":
    result = num1 * num2
else :
    print('죄송합니다 다시입력해주세요.')
print(result)
