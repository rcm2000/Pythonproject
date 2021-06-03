data = [10,20,30,30,30,40,50]

print(data.index(40));
print(data.count(30))

for i in range(0,data.count(30)) :
    data.remove(30)
print(data)
