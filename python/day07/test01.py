import random

datas = {2,1,3,5,4}
print(datas)

datas.add(6)
print(datas)
datas.remove(2)
print(datas)
print(len(datas))

a = list(datas)
print(a)

nums = set();
while len(nums) < 6:
    n = random.randint(1,45)
    nums.add(n)
print(nums)

s1 = {1,2,3,4}
s2 = {3,4,5,6}

print(s1-s2)