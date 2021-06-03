def convert(st,opt):
    result = '';
    sp = st1.split('-')

    if opt == 1:
        result = '%s년%s월%s일' % (sp[0], sp[1], sp[2])
    elif opt == 2:
        result = '%s월%s일%s년' % (sp[1], sp[2], sp[0])
    elif opt == 3:
        result = '%s일%s월%s년' % (sp[2], sp[1], sp[0])
    #result = (st[0:4]+'년'+st[5:7]+'월'+st[-2:]+'일')

    return result

st1 = '2021-05-24'
n = int(input('타입을 입력하시오(1/2/3)'))
print(convert(st1,n))
