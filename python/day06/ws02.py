#당첨금은 램덤??? 무작위로 고르라는것 혹은 선정?
import random
temp1 = [];
a = []

def insert(a):
    n1 = 0;
    print('우선 나의 로또번호 6자리를 입력합니다.')
    while True:
        n1 += 1
        n = input('%d 번째 숫자를 입력하세요.'%n1)

        if n.isnumeric() == False or (int(n) <= 0) or (int(n) >= 46) or (int(n) in a)  :  # 1~45를 벗어나거나 중복된것 제외
            print("=> 중복된 번호를 넣었거나 잘못된 번호를 넣었습니다. 다시 입력해주세요.")
            n1 -= 1
            continue
        else:
            a.append(n)
        if len(a) == 6:
            break
    return a;
def rand(temp1):
    temp1 = [];
    while True:
        n = random.randint(1, 45)
        if not n in temp1:
             temp1.append(n)
        if len(temp1) == 6:
             break
    return temp1

def match(a,temp1):
    bb = set(a).copy()
    cc = set(temp1).copy()
    dd = bb&cc
    if len(dd) == 0:
        print("%d개 맞췄습니다 꽝~! 상금 0원 ㅠㅠ"%len(dd))
    elif len(dd) == 1:
        print("%d개 맞췄습니다 6등 상금 백만원"%len(dd))
    elif len(dd) == 2:
        print("%d개 맞췄습니다 5등 상금 이백만원"%len(dd))
    elif len(dd) == 3:
        print("%d개 맞췄습니다 4등 상금 오백만원"%len(dd))
    elif len(dd) == 4:
        print("%d개 맞췄습니다 3등 상금 삼천만원"%len(dd))
    elif len(dd) == 5:
        print("%d개 맞췄습니다 2등 상금 이억원"%len(dd))
    elif len(dd) == 6:
        print("%d개 맞췄습니다 1등 상금 십억원!!"%len(dd))


print("=> 로또 프로그램을 실행합니다...")
a1 = rand(temp1)
a2 = insert(a)

while True:

    #print(a1) # 확인용
    #print(a2) # 확인용

    print("===========================")
    print("1. 이번주 로또 번호를 봅니다.")
    print("2. 나의 로또 번호를 봅니다.")
    print("3. 이번주 번호와 내 로또번호를 비교 확인합니다.")
    print("4. 프로그램을 종료합니다.")
    print('5. 번호를 섞고 다시 도전합니다.')
    num = int(input('번호를 입력하세요.......?'))
    if num == 1:
        print("이번주 로또 번호 = %s" %a1)
    elif num == 2:
        print("나의 로또 번호 = %s" %a2)
    elif num == 3:
        print(sorted(a1))
        print(sorted(a2))
        a3 = set(a1) & set(a2)
        print('맞춘 번호 : %s'%a3)
        match(a1,a2)
    elif num == 4:
        print("프로그램을 종료합니다...")
        break
    elif num == 5:
        print("번호를 섞고 다시 도전합니다.....")
        temp1 = [];
        a = [];
        a1 = rand(temp1)
        a2 = insert(a)
        continue
    else:
        print('번호를 다시 확인하여 주세요~!')

    print()


# while True:
#     while True:
#         n = random.randint(1, 45)
#         if not n in temp1:
#             temp1.append(n)
#         if len(temp1) == 6:
#             break
#     print(temp1)
#     print(insert(a))
#     print(match(a,temp1))
#     restart = input('다시 시작하려면 1번을 입력하세요');
#     if restart == '1':
#         n = [];
#         continue
#     else:
#         break












# import random
# temp1 = [];
# num = 0;
# for a in range(1,7):
#     num = random.randint(1,45)
#     temp1.append(num)
#
# print(temp1)
# lis = [];
# for i in range(1,7):
#     a = input('6자리 수중 %d 번째 수를 입력하세요!' %i)
#     if not a.isnumeric() == False:
#         lis.append(int(a))
#     else:
#         i = 0
#         print('1~45까지의 숫자만 입력가능합니다.')
#         break
# print(lis)



