sum1 = 0;
sum2 = 0;
for i in range(1,101):
    if i % 3 == 0:
        sum1 += i
    if i % 7 == 0:
        sum2 += i

print('3의 배수의 합 =',sum1,'7의 배수의 합 =', sum2)
print('두 수의 차 = ', sum1 - sum2)

