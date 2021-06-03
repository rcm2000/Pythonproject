from DAO.itemdb import ItemDB
from DAO.userdb import UserDB
from VO.uservo import UserVO
from Frame.sqlitedao import Sqlitedao
print('start.....');

#Table 생성(UserDB, ItemDB)
sqlitedao = Sqlitedao('shop')
sqlitedao.makeTable();

udb = UserDB('shop');
idb = ItemDB('shop')

while True:
    cmd = input('Input command (i,d,u,s,sa,q)')
    if cmd == 'q':
        print('bye.....')
        break
    elif cmd == 'i':
        print('Insert')
        id = input('Id를 입력하십시오....')
        pwd = input('pwd를 입력하십시오....')
        name = input('name을 입력하십시오....')
        user = UserVO(id,pwd,name)
        udb.insert(user)
        print('유저 정보가 입력 되었습니다')
    elif cmd == 'd':
        print('Delete')
        id = input('Id를 입력하십시오....')
        udb.delete(id)
    elif cmd == 'u':
        print('Update')
        id = input('수정할 Id를 입력하십시오....')
        pwd = input('pwd를 입력하십시오....')
        name = input('name을 입력하십시오....')
        user = UserVO(id, pwd, name)
        udb.update(user)
    elif cmd == 's':
        print('Select')
        id = input('Id를 입력하십시오....')
        s_id = udb.select(id)
        print(s_id)
    elif cmd == 'sa':
        print('Select All')
        s_idall = udb.selectall()
        for i in s_idall:
            print(i)

print('end.....');