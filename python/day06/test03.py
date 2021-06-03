import random

temp1 = [];
temp2 = [];

while True:
    num = random.randint(1,10)
    if num not in temp1:
        temp1.append(num);
    if len(temp1) == 10:
        break



print(temp1)
print(sorted(temp1))

