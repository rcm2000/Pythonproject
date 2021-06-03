import cal
try:
    data = cal.calc(-2)
    print(data);
except ZeroDivisionError:
    print('0으로는 나눌 수 없습니다')
except ValueError:
    print('음수로는 나눌 수 없습니다')


