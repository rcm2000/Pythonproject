def insert(id,psw,name):
    print('inserted data......')
def select1(id):
    print('selected 1 data .....')
    return [id, 'pwdxx','jamesxx']
def select():
    print('selected data......')
    datas = [['id01','pw01','james1']
        ,['id02','pw02','james2']
        ,['id03','pw03','james3']
        ,['id04','pw04','james4']];
    return datas;
def update(id,psw,name):
    print('updated data......')
def delete(id):
    print('deleted data......')

while True:
    cmd = input('input cmd(i,s,s1,u,d,q)......')
    if cmd == 'q':
        print('bye')
        break;
    elif cmd == 'i':
        id = input('input ID...?')
        psw = input('input PSW...?')
        name = input('input Name...?')
        insert(id,psw,name)
    elif cmd == 's':
        users = select();
        for u in users:
            print(u)
    elif cmd == 'u':
        id = input('input ID...?')
        psw = input('input PSW...?')
        name = input('input Name...?')
        update(id, psw, name);
    elif cmd == 'd':
        id = input('input ID...?')
        delete(id)
    elif cmd == 's1':
        id = input('input ID...?')
        user = select1(id);
        print(user)




print('End Program...')
