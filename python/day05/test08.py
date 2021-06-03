data =['2021-05-24',20,30,40]
sum = 0;
for i in data[1:4]:
    sum += i
    print(i)
print('%s의 평균온도는 %f도입니다.'%(data[0],sum/len(data[1:4])))

d1 = [1,2,3,4,5]
temp = d1.copy()
del temp[0]
print(d1)
print(temp)
