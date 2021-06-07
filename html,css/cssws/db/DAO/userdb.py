import sqlite3

from db.SQL.sql import Sql
from db.VO.uservo import UserVO
from db.Frame.sqlitedao import Sqlitedao

class UserDB(Sqlitedao):
    def __init__(self, dbName):
        super().__init__(dbName);

    def insert(self, u):
        cc = self.getConn();
        cc['cursor'].execute(Sql.insert_userdb,
                             (u.getId(),u.getPwd(),u.getName())
                             );
        cc['con'].commit();
        self.close(cc);
        print('%s 등록 되었습니다.' % u);
    def delete(self,id):
        print('%s 삭제 되었습니다.' % id);
        cc = self.getConn();
        cc['cursor'].execute(Sql.delete_userdb,(id,))

        cc['con'].commit();
        self.close(cc)
    def update(self, u):
        print('%s 수정 되었습니다.' % u);
        cc = self.getConn();
        cc['cursor'].execute(Sql.update_userdb,(u.getPwd(),u.getName(),u.getId()))
        cc['con'].commit();
        self.close(cc)

    def select(self, id):
        result = None;
        cc = self.getConn();
        cc['cursor'].execute(Sql.select_userdb , (id,));
        obj = cc['cursor'].fetchone();
        result = UserVO(obj[0],obj[1],obj[2]);
        self.close(cc);
        return result;
    def selectall(self):
        results = [];
        cc = self.getConn();
        cc['cursor'].execute(Sql.selectall_userdb);
        all = cc['cursor'].fetchall();
        for u in all:
            rs = UserVO(u[0],u[1],u[2]);
            results.append(rs);
        self.close(cc);
        return results;
# test table
if __name__ == '__main__':
    print('start test......')
    sqlitedao = Sqlitedao('shop')
    sqlitedao.makeTable();
    udb = UserDB('shop');
    # user = udb.select('id01')
    # print(user);
    # user = UserVO('id01','pwd01','james');
    # udb.insert(user);
    # user2 = UserVO('id02', 'pwd02', 'james2');
    # udb.insert(user2);
    #
    users = udb.selectall();
    for u in users:
        print(u)


    print('end test......')





