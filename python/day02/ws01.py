wage = int(input("직원의 월급을 입력하세요....."))
taxm = wage * (3.8/100);
ins = (wage - taxm) * (10.2/100);
wage2 = wage - (taxm + ins)
sal = wage2 * 12
print(" 월급 :" ,wage2,"연봉 : ",sal);
if sal < 30000000:
    print('삐빅 "사원"입니다.')
elif sal < 50000000:
    print('삐빅 "대리"입니다.')
elif sal < 80000000:
    print('삐빅 "과장" 입니다.')



