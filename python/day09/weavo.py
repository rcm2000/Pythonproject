class WeadbVO:
    def __init__(self,city,province,tmn,tmx,date):
        self.__city = city;
        self.__province = province;
        self.__tmn = tmn;
        self.__tmx = tmx;
        self.__date = date;
    def __str__(self):
        return '%s, %s, %.2f %.2f %s' % (self.__city,self.__province,self.__tmn,self.__tmx,self.__date);
    def getCity(self):
        return self.__city;
    def getProvince(self):
        return self.__province;
    def setProvince(self, province):
        self.__province = province;
    def getTmn(self):
        return self.__tmn;
    def setTmn(self, tmn):
        self.__tmn = tmn;
    def getTmx(self):
        return self.__tmx;
    def setTmx(self, tmx):
        self.__tmx = tmx;
    def getDate(self):
        return self.__date;
