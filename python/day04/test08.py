def score(name,*s,**option):
    """이 함수는 이름 , 점수, 평균여부를 입력하세요"""
    print(name)
    sum = 0;
    for i in s:
        sum += i
    print(sum)
    if option['avg'] == 1:
        print(sum/len(s))

help(score);
score('Lee',88,99,100,68,avg=True);
print('----------------------')
score('Kim',88,99,100,avg=False);
