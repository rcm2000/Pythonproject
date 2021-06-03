class Sql:
    make_wdb = ''' CREATE TABLE IF NOT EXISTS WEATHERDB (
        id integer primary key autoincrement, 
        province text , city text, date text, forecast text, min real, max real)
    '''
    insert_wdb = '''insert into WEATHERDB (province, city, date, forecast, min, max) values (?,?,date(?),?,?,?)'''
    delete_weatdb = ''' DELETE  FROM  WEATHERDB  WHERE  CITY=? ''';
    deleteall_weatdb = ''' DELETE  FROM  WEATHERDB '''
    select_weatdb = ''' SELECT  *  FROM  WEATHERDB  WHERE CITY=? ''';
    selectall_weatdb = ''' SELECT  * FROM WEATHERDB ''';


















# class Sql:
#     make_weatdb = ''' CREATE  TABLE  IF NOT EXISTS WEADB3 (
#         CITY  TEXT  PRIMARY KEY,
#         PROVINCE  TEXT,
#         TMN REAL,
#         TMX REAL,
#         DATE TEXT
#
#     ) ''';
#     insert_weatdb = ''' INSERT  INTO  WEADB3 VALUES (?,?,?,?,?) ''';
#     update_weatdb = ''' UPDATE  WEADB3  SET  PROVINCE=?, TMN =?, TMX =?, DATE=? WHERE  CITY=? ''';
    delete_weatdb = ''' DELETE  FROM  WEADB3  WHERE  CITY=? ''';
    deleteall_weatdb = ''' DELETE  FROM  WEADB3 '''
    select_weatdb = ''' SELECT  *  FROM  WEADB3  WHERE CITY=? ''';
    selectall_weatdb = ''' SELECT  * FROM WEADB3 ''';

