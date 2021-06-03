class Code:
    E01 = '잔액부족'
    E02 = '출금금액 마이너스 오류'

class Account:
    def __init__(self,balance,interest):
        self.__balance = balance;
        self.__interest = interest;
    def getBalance(self):
        return self.__balance;
    def getInterest(self):
        return self.__interest;
    def setInterest(self,interest):
        self.__interest = interest;
    def __str__(self):
        return 'balaance : %d, Interest = %.2f' % (self.__balance,self.__interest)
    def deposit(self,money):
        self.__balance += money;
    def withdraw(self,money):
        if money > self.__balance:
            raise ValueError(Code.E01)
        elif money < 0:
            raise ValueError(Code.E02)
        else:
            self.__balance -= money;
    def inter(self):
        inter1 = self.__balance * (self.__interest/100)
        return inter1


class Car:
    def __init__(self,name,color,size):
        self.name = name;
        self.color = color
        self.size = size
    def __str__(self):
        return '%s, %s, %d' %(self.name,self.color,self.size)
    def go(self):
        return '%s (이)가 출발합니다.' %(self.name)
    def stop(self):
        return '%s (이)가 정지합니다.' %(self.name)