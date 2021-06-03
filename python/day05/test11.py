score = [
[90,80,100,92],
[91,81,100,91],
[92,82,100,92],
[93,83,100,93],
[94,84,100,94]
         ]
# print(len(score))
# print(score[1:3])

sum = 0
sum2 = 0
le = 0
for i in score:
    for j in i:
        sum += j
        sum2 += j
        le += 1
    print(sum)
    print(sum/len(i))
    sum = 0
print(sum2)
print(le)
print(sum2/le)



