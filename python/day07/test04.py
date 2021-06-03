st = ['id','pws','name','age'];
data = ['id02','pwd01','james',30];

cust = zip(st,data)
print(dict(cust))
print(type(cust))
for s,d in cust:
    print('%s : %s' %(s,d));


