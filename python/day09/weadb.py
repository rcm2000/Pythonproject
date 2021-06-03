# userdb.py Control 역할
import sqlite3

from sql import Sql
from weavo import WeadbVO


class WeaDB:
    def __init__(self, dbName):
        self.__dbName = dbName;
    def getConn(self):
        con = sqlite3.connect(self.__dbName);
        cursor = con.cursor();
        return {'con':con,'cursor':cursor};

    def close(self, cc):
        if cc['cursor'] != None:
            cc['cursor'].close();
        if cc['con'] != None:
            cc['con'].close();

    def makeTable(self):
        cc = self.getConn();
        cc['cursor'].execute(Sql.make_weatdb);
        cc['con'].commit();
        self.close(cc);

    def insert(self, w):
        cc = self.getConn();
        cc['cursor'].execute(Sql.insert_weatdb,(w.getCity(),w.getProvince(),w.getTmn(),w.getTmx(),w.getDate)
                             );
        cc['con'].commit();
        self.close(cc);
        print('%s 등록 되었습니다.' %w);
    def delete(self,city):
        print('%d 삭제 되었습니다.' % city);
        cc = self.getConn()
        cc['cursor'].execute(Sql.delete_weatdb, (city,))
        cc['con'].commit()
        self.close(cc)
    def deleteall(self):
        print('전부 삭제 되었습니다.')
        cc = self.getConn()
        cc['cursor'].execute(Sql.deleteall_weatdb)
        cc['con'].commit()
        self.close(cc)
    def update(self, w):
        print('%s 수정 되었습니다.' % w);
        cc = self.getConn();
        cc['cursor'].execute(Sql.update_weatdb,(w.getProvince(),w.getTmn(),w.getTmx(),w.getDate,w.getCity))
        cc['con'].commit();
        self.close(cc)
    def select(self, city):
        # 해당 id 의 데이터를 가지고 와서 uservo를 만들어서 리턴한다.
        result = None;
        cc = self.getConn();
        cc['cursor'].execute(Sql.select_weatdb,(city,));
        obj = cc['cursor'].fetchone();
        result = WeadbVO(obj[0], obj[1], obj[2],obj[3],obj[4]);
        self.close(cc);
        return result;
    def selectall(self):
        results = [];
        cc = self.getConn();
        cc['cursor'].execute(Sql.selectall_weatdb);
        all = cc['cursor'].fetchall();
        for i in all:
            rs = WeadbVO(i[0],i[1],i[2],i[3],i[4])
            results.append(rs)
        self.close(cc)
        return results;