def lottogame(a):
    import random
    inputNums = []
    if a == 'a':
        # 번호 입력 받기(자동)
        while len(inputNums) < 6:
            num = random.randint(1, 45)
            if num not in inputNums:
                inputNums.append(num)
        print('자동완성번호:', inputNums)
    else:
        # 번호 입력 받기(수동)
        while len(inputNums) < 6:
            num = input('1 ~ 45 사이의 번호를 하나 입력하세요: ')
            if  num > 0 and num < 46:
                if num not in inputNums:
                    inputNums.append(num)
                else:
                    print('입력한', inputNums,'와 중복되지 않은 숫자로 다시 입력하세요.')
                    continue
            else:
                print('--- 1 ~ 45 사이의 숫자를 입력하세요. ---')
                continue
        print('수동완성번호:', inputNums)
    # 당첨 번호 생성
    lottoNums = []
    while len(lottoNums) < 6:
        num = random.randint(1, 45)
        if num not in lottoNums:
            lottoNums.append(num)
    # 보너스 번호 생성
    lottoBonusNum = []
    while len(lottoBonusNum) < 1:
        BonusNum = random.randint(1, 45)
        if BonusNum not in lottoBonusNum:
            lottoBonusNum.append(BonusNum)
    print('당첨번호:', lottoNums, ',','보너스번호:', lottoBonusNum)

    # 번호 매칭
    # 일반
    cnum = []
    for m in range(0, 6):
        if inputNums[m] in lottoNums:
            cnum.append(1)
        else:
            cnum.append(0)
    # print(cnum)
    # 보너스
    bnum = []
    for o in range(0, 6):
        if inputNums[o] in lottoBonusNum:
            bnum.append(1)
        else:
            bnum.append(0)
    # print(bnum)

    # 상금, 등수 정리
    if cnum.count(1) == 0:
        prizeMoney = 0
        prizeRank = 8
    elif cnum.count(1) == 1:
        prizeMoney = random.randrange(5000, 10000)
        prizeRank = 7
    elif cnum.count(1) == 2:
        prizeMoney = random.randrange(10001, 15000)
        prizeRank = 6
    elif cnum.count(1) == 3:
        prizeMoney = random.randrange(15001, 20000)
        prizeRank = 5
    elif cnum.count(1) == 4:
        prizeMoney = random.randrange(20001, 100000)
        prizeRank = 4
    elif cnum.count(1) == 5 and bnum.count(1) == 0:
        prizeMoney = random.randrange(100001, 1000000)
        prizeRank = 3
    elif cnum.count(1) == 5 and bnum.count(1) == 1:
        prizeMoney = random.randrange(1000001, 10000000)
        prizeRank = 2
    elif cnum.count(1) == 6:
        prizeMoney = random.randrange(10000001, 100000000)
        prizeRank = 1
    # 등수, 상금 출력
    return print('%d개 맞추셔서 %d등, %d원입니다.'% (cnum.count(1), prizeRank, prizeMoney))

lottogame(input('숫자를 자동으로 고르려면 a를 누르시고 수동으로 고르려면 a를 제외한 아무 키나 입력해주세요.'))
answer = input('게임을 다시 실행하시려면 y를 누르세요.')
while answer == 'y':
    lottogame(input('숫자를 자동으로 고르려면 a를 누르시고 수동으로 고르려면 a를 제외한 아무 키나 입력해주세요.'));
    answer = []
    answer = input('게임을 다시 실행하시려면 y를 누르세요.')