# userdb.py Control 역할
import sqlite3

from SQL.sql import Sql
from VO.itemvo import ItemVO
from Frame.sqlitedao import Sqlitedao

class ItemDB(Sqlitedao):


    def __init__(self, dbName):
        super().__init__(dbName);

    def insert(self, item):
        cc = self.getConn();
        cc['cursor'].execute(Sql.insert_itemdb,
                             (item.getName(),item.getPrice())
                             );
        cc['con'].commit();
        self.close(cc);
        print('%s 등록 되었습니다.' % item);
    def delete(self,id):
        print('%d 삭제 되었습니다.' % id);
        cc = self.getConn()
        cc['cursor'].execute(Sql.delete_itemdb, (id,))
        cc['con'].commit()
        self.close(cc)
    def update(self, item):
        print('%s 수정 되었습니다.' % item);
        cc = self.getConn();
        cc['cursor'].execute(Sql.update_itemdb, (item.getName(), item.getPrice(),item.getId()))
        cc['con'].commit();
        self.close(cc)
    def select(self, id):
        # 해당 id 의 데이터를 가지고 와서 uservo를 만들어서 리턴한다.
        result = None;
        cc = self.getConn();
        cc['cursor'].execute(Sql.select_itemdb,(id,));
        obj = cc['cursor'].fetchone();
        result = ItemVO(obj[0], obj[1], obj[2],obj[3]);
        self.close(cc);
        return result;
    def selectall(self):
        results = [];
        cc = self.getConn();
        cc['cursor'].execute(Sql.selectall_itemdb);
        all = cc['cursor'].fetchall();
        for i in all:
            rs = ItemVO(i[0],i[1],i[2],i[3])
            results.append(rs)
        self.close(cc)
        return results;





