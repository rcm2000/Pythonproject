import csv
try:

    f = open('111.csv');
    data = csv.reader(f);
    print(type(data))
    for row in data:
        print(row)
except:
    print('File not found...');
finally:
    if f != None:
        f.close()
