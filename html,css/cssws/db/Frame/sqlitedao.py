import sqlite3

from db.SQL.sql import Sql


class Sqlitedao:
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
        cc['cursor'].execute(Sql.make_itemdb);
        cc['cursor'].execute(Sql.make_userdb);
        cc['con'].commit();
        self.close(cc);