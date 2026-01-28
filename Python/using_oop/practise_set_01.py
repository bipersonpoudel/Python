# create a account class with 2 attribute balance and account No
# create a method for debit, credit and printing the balance


class Account:
    def __init__(self,balance,acc_no):
        self.balance=balance
        self.acc_no=acc_no

    def debit(self,amount):
        balance=self.balance-amount
        print(f"{amount} was deducted from your balance")
        print("Your remaining balance is ",balance)

    def credit(self,amount):
        balance=self.balance+amount
        print(f"{amount} was credited to your balance")
        print("Your remaining balance is ",balance)
    def printing_the_balance(self):
        balance=self.balance
        print("Your Balance is: ",balance)
customer1=Account(124563,24112312)
print("Your Current Balance is ",customer1.balance)
customer1.debit(1000)
customer1.credit(10000) 
customer1.printing_the_balance()