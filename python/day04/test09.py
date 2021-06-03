import math

data = 0;
num =0
def func():
    global num;
    data = 100;
    num = 200;
    return data;

result = func();
print(result);
print(data);
print(num);
maxdata = max(8,9,10,22,37,200)
print(maxdata)
print(sum([1,2,3,4]))
print(math.pow(2,3))