import random

num = random.randint(1,10)
cnt = 1;
while True:
    if cnt > 5:
        print("게임 fail! 다시 도전하세요")
        re = input('게임을 다시 도전하시겠습니까?(Y/N)...')
        if re == 'Y':
            cnt = 1
            num = random.randint(1, 10)
            continue
        if re == 'N':
            print('다음에 도전하세요~!')
            break
        else:
            print('Y와 N만 입력가능합니다.')
            continue
    print(cnt,"회차 도전~!")
    a = int(input('1~10까지의 숫자중 하나를 입력하시오.'))
    if not (a <= 10 and a > 0):
        print('1~10까지의 숫자만 입력가능합니다.')
        continue
    if num == a:
        print('정답입니다~!')
        exit(0)

    elif num > a:
        print('땡 다시입력하세요~! (UP)')
        cnt += 1
    else :
        print('땡 다시입력하세요~! (DOWN)')
        cnt += 1
