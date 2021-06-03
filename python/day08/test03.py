from value import Account

acc1 = Account(10000,3.2);
acc2 = Account(20000,3.1);
print(acc1)
print(acc2)

acc1.deposit(5000)
print(acc1)
try:
    acc1.withdraw(-30000)
except ValueError as v :
    print(v.args[0])

print(acc1)
a = acc1.inter()
print('%s, %.2f' %(acc1,a))

