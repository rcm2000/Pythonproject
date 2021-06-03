import random

def calc():
    a = 10;
    b = 20;
    result = a + b;
    return result;

def rand():
    num = random.randint(1,10);
    return num;

def calcsum(s):
    result = 0;
    for i in (1,11):
        result += i;
        return result;

a = int(input('1000을 곱할 수를 입력하시오'))
sum2 = calcsum(a)
print(sum2)
print(calc())
print(rand())