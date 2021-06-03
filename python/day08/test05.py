from value import Account
acc = None
while True:
    cmd = input('input cmd (c,s,d,w,q)')
    if cmd == 'c':
        if acc != None:
            print('이미 생성된 계좌가 있습니다.')
        else:
            print('Create your Acoount')
            money = int(input('금액을 입력하십시오.'))
            interest = float(input('이자를 입력하십시오.'))
            acc = Account(money,interest)
            print('계죄 생성 완료 , 계좌정보 : ' , acc)

    elif cmd == 's':
        if acc == None:
            print('계좌를 생성하고 다시 시도하세요.')
        else:
            print('select')
            print('계좌조회결과 : ' , acc)
    elif cmd == 'd':
        if acc == None:
            print('계좌를 생성하고 다시 시도하세요.')
        else:
            print('Deposit')
            d_money = int(input('입금하실 금액을 입력하십시오'))
            acc.deposit(d_money)
    elif cmd == 'w':
        if acc == None:
            print('계좌를 생성하고 다시 시도하세요.')
        else:
            print('Withdraw')
            w_money = int(input('출금하실 금액을 입력하십시오'))
            try:
                acc.withdraw(w_money)
            except ValueError as v:
                print(v.args[0])

    elif cmd == 'q':
        break

print('Bye...!!')

