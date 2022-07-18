print("********** Welcome to Banking System **********")
class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age 
        self.gender = gender
    def show_details(self):
        print("Personal Details")
        print()
        print("Name - ",self.name)
        print("Age - ",self.age)
        print("Gender - ",self.gender)
class Bank(User):
    def __init__(self,name,age,gender):
        super(). __init__(name,age,gender)
        self.balance = 0
    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print(f"Amount balance has been updated = ${self.balance}")
    def withdraw(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print(f"Insufficient Funds! Balance Avilable ${self.balance}")
        else:
            self.balance = self.balance-self.amount
            print(f"Amount balance has been updated = ${self.balance}")
    def view_balance(self):
        self.show_details()
        print(f"Amount balance has been updated = ${self.balance}")
        
#data = Bank(name,age,gender)
name = str(input("Enter name: "))
age = int(input("Enter your age: "))
gender = str(input("Enter your gender: "))
data = Bank(name,age,gender)
print()
while True:
    print("1.Deposit Amount\n2.Withdraw Amount\n3.View Balance\n4.Exit")
    op = int(input("Enter opreation number: "))
    if op == 1:
        dmoney = int(input("Please Enter the Amount For Deposit: "))
        data.deposit(dmoney)
    elif op ==2:
        #data.deposit(dmoney)
        money = int(input("Please Enter the Amount For Withdraw:"))
        data.withdraw(money)
    elif op ==3:
        data.view_balance()
    elif op ==4:
        print("Thankyou so much using banking sevices")
        break 
        
    else:
        print("Invalid Number")
    
            