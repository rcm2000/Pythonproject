import numpy as np

ldata = [1,2,3,4,5];

ndata = np.array(ldata)

print(ldata)
print(type(ldata))
print(ndata)
print(type(ndata))
print(ndata[2:])

#단위행렬
a = np.eye(3)
print(a)


print(ndata + 5)
print(list(ndata))

ndata3 = np.arange(-5,5);
print(ndata3)
print(ndata3 < 0)
print(ndata3[ndata3 < 0])
print(ndata3[ndata3 % 2 == 0])