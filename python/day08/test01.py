balance = 8000;

def deposit(m):
    global balance;
    balance += m

def select():
    return balance

result = select();
print(result)
deposit(3000)
print(select())