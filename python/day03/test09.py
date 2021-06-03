import random

print('start................')

num = random.randint(1,10);
while True:
    cmd = input('input number...(q:exit)');
    if cmd == "q":
        print('bye')
        break
    else:
        int_num = int(cmd)
        if  int_num == num :
            print('정답~!')
            exit(0)
        if int_num != num:
                print('땡 다시입력해 보세요~!')


print('end................')