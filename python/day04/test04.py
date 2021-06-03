def calc(*n):
    sum = 0;
    avr = 0;
    for i in n:
        sum += i
    avr = sum/len(n)
    return avr;


r1 = calc(10,20,30,72,80);
r2 = calc(1,2,3);
print(r1)
print(r2)
