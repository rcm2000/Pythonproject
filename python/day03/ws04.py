y = False
for i in range(1,11):
    if y == True:
        break
    for j in range(1,11):
        if i == 3 and j == 5:
            y = True
            break
        print(i,':',j);
    print('---------------')

