# sum1 = 0;
# sum2 = 0;
# cnt1 = 0;
# cnt2 = 0;
# for i in range(1,101):
#     if i % 2 == 1:
#         sum1 += i
#         cnt1 += 1
#     else:
#         sum2 += i
#         cnt2 += 1
# print(cnt1)
# print(cnt2)
# print(sum1)
# print(sum2)
# print(sum1/cnt1)
# print(sum2/cnt2)
cnt2 = 0;
cnt3 = 0;
cnt5 = 0;
sum2 = 0;
sum3 = 0;
sum5 = 0;
for i in range(1,1001):
    if i % 2 == 0:
        sum2 += i
        cnt2 += 1
    if i % 3 == 0:
        sum3 += i
        cnt3 += 1
    if i % 5 == 0:
        sum5 += i
        cnt5 += 1

print(cnt2)
print(cnt3)
print(cnt5)
print(sum2)
print(sum3)
print(sum5)
print(sum2/cnt2)
print(sum3/cnt3)
print(sum5/cnt5)