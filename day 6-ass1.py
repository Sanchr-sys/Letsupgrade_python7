###############BANK ACCOUNT#############

class Bank_Account:
    def __init__(self,Name,Balance,Withdraw):
        self.Name = Name
        self.Balance = Balance
        self.Withdraw = Withdraw

    def deposit(self):
        dep = input("Enter Amount to deposit = ")
        print("The deposited amount is = ", dep)
        if dep > '1000000':
            print("Sorry customer, maximum deposit allowed is 700000")
        else:
            print("Congratulations customer, amount deposited successfully")

    def withdrawal(self):
        Amount = self.Balance
        Balance = int(input("Please Enter Total Amount in your Account = "))
        Withdraw = int(input("Enter amount to withdraw = "))
        if Withdraw < Balance:
            print("Congratulations customer, amount Withdrawn successfully")
        else:
            print("Sorry Customer, you cant withdraw as value is more than available balance")

obj = Bank_Account('sanchal',0,0)
obj.deposit()
obj.withdrawal()
obj1 = Bank_Account('katy',0,0)
obj1.deposit()
obj1.withdrawal()
obj2 = Bank_Account('kristen',0,0)
obj2.deposit()
obj2.withdrawal()



