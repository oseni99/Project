# trying to create a simple banking operation with OOP 
# this is a mistake 
#class bank 
import random 
random.seed(42)
class Bank():
    address = "627 West Battle Street,Talladega,Alabama"
    bank = "Talladega Western Bank"
    def __init__(self,name,ssn):
        self.name = name 
        self.ssn = ssn 
        self.balance = 0.0 
        assert isinstance(self.name,str), "It has to be a name please"
        assert isinstance(self.ssn,int), "Can you enter the correct length and format"

    def deposit(self,amount):
        self.balance+=amount 
       
    def acct_balance(self):
        print(f"User {self.name}, your balance is {self.balance}")

    def withdraw(self,amount):
        if amount < self.balance:
            self.balance-= amount
            print("Here is your withdrawal {self}")
        else:
            print("Insuficient Funds")
        
    
    def account_number(self):
        #self.randoms = randoms
        
        mylst = [0,1,2,3,4,5,6,7,8,9]
        x = random.choices(population=mylst,k=9)
        print("-".join(map(str,x)))

    

print(f"Welcome to {Bank.bank}")

name = str(input("Enter your name: "))
socials = int(input("Enter your ssn to proceed"))

b = Bank(name,socials)
print(f"You have succesfully registered to {Bank.bank}")



while True:
    choice = int(input("Which account type do you want: \n1.Savings \n2.Checking"))
    if choice == 1:
        print("Savings Account Created Succesfully")
        account_creation = True 
    elif choice == 2:
        print("Checking Account Succesfully Created")
        account_creation = True 
    else:
        print("Can you kindly choose?")
    break 

while account_creation:
    print("Here is your account number: ")
    b.account_number()
    break
    

while True:
        amount = float(input("How much do you want to deposit: "))
        if isinstance(amount,float):
                b.deposit 
                print("Deposit Confirmed!")
                break
        else:
            print("Ivalid Figure \nCan you kindly enter a figure?")
            break

while True:
        print("Do you want to check your balance? \tYes or \tNo")
        choice = input("").capitalize()
        if choice == "Yes":
              b.acct_balance
              break 
        else:
             print("Thank you for banking with us!")


           
            
            
    #import os 
#print(os.getcwd())
