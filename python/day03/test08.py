print('start................')

while True:
    cmd = input('input commend.....');
    if cmd == "q":
        print('bye')
        break
    elif cmd == 'i':
        print('insert data')
    elif cmd == 'd':
        print('delete data')
    elif cmd == 's':
        y = input('input year...')
        print(y, "    select data")

print('end................')