sub1 = int(input('1과목의 성적을 입력하세요...?'));
sub2 = int(input('2과목의 성적을 입력하세요...?'));
sub3 = int(input('3과목의 성적을 입력하세요...?'));
sub4 = int(input('4과목의 성적을 입력하세요...?'));

if (sub1 + sub2 + sub3 + sub4)/4 >= 96:
    print((sub1 + sub2 + sub3 + sub4)/4)
    print('A+학점 입니다.')
elif (sub1 + sub2 + sub3 + sub4) / 4 >= 91:
        print((sub1 + sub2 + sub3 + sub4) / 4)
        print('A학점 입니다.')
elif (sub1 + sub2 + sub3 + sub4)/4 >= 86:
    print((sub1 + sub2 + sub3 + sub4)/4)
    print('B+학점 입니다.')
elif (sub1 + sub2 + sub3 + sub4) / 4 >= 81:
    print((sub1 + sub2 + sub3 + sub4) / 4)
    print('B학점 입니다.')
elif (sub1 + sub2 + sub3 + sub4)/4 >= 76:
    print((sub1 + sub2 + sub3 + sub4)/4)
    print('C+학점 입니다.')
elif (sub1 + sub2 + sub3 + sub4)/4 >= 71:
    print((sub1 + sub2 + sub3 + sub4)/4)
    print('C학점 입니다.')
elif (sub1 + sub2 + sub3 + sub4)/4 >= 66:
    print((sub1 + sub2 + sub3 + sub4)/4)
    print('D+학점 입니다.')
elif (sub1 + sub2 + sub3 + sub4)/4 >= 61:
    print((sub1 + sub2 + sub3 + sub4)/4)
    print('D학점 입니다.')
else:
    print((sub1 + sub2 + sub3 + sub4)/4)
    print('F학점 입니다.')

print('---------------------------------');
